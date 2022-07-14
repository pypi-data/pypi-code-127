from __future__ import annotations

import abc
import logging
from collections.abc import AsyncIterator, Mapping, Sequence
from contextlib import AbstractAsyncContextManager, asynccontextmanager
from dataclasses import dataclass
from types import TracebackType
from typing import Any

import aiohttp
from aiohttp import ClientResponseError
from yarl import URL

from .entities import (
    BucketsConfig,
    CloudProviderOptions,
    CloudProviderType,
    Cluster,
    CredentialsConfig,
    DisksConfig,
    DNSConfig,
    IngressConfig,
    MetricsConfig,
    MonitoringConfig,
    NodePool,
    NotificationType,
    OrchestratorConfig,
    RegistryConfig,
    ResourcePreset,
    SecretsConfig,
    StorageConfig,
)
from .factories import EntityFactory, PayloadFactory

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class _Endpoints:
    clusters: str = "clusters"
    cloud_providers: str = "cloud_providers"

    def cloud_provider_options(self, type: CloudProviderType) -> str:
        return f"{self.cloud_providers}/{type.value}"

    def cluster(self, cluster_name: str) -> str:
        return f"{self.clusters}/{cluster_name}"

    def node_pools(self, cluster_name: str) -> str:
        return f"{self.cluster(cluster_name)}/cloud_provider/node_pools"

    def node_pool(self, cluster_name: str, node_pool_name: str) -> str:
        return f"{self.node_pools(cluster_name)}/{node_pool_name}"

    def storages(self, cluster_name: str) -> str:
        return f"{self.cluster(cluster_name)}/cloud_provider/storages"

    def storage(self, cluster_name: str, storage_name: str) -> str:
        return f"{self.storages(cluster_name)}/{storage_name}"

    def notifications(self, cluster_name: str) -> str:
        return f"{self.cluster(cluster_name)}/notifications"

    def resource_presets(self, cluster_name: str) -> str:
        return f"{self.cluster(cluster_name)}/orchestrator/resource_presets"

    def resource_preset(self, cluster_name: str, preset_name: str) -> str:
        return f"{self.resource_presets(cluster_name)}/{preset_name}"


class ConfigClientBase:
    def __init__(self) -> None:
        self._endpoints = _Endpoints()
        self._entity_factory = EntityFactory()
        self._payload_factory = PayloadFactory()

    @abc.abstractmethod
    def _request(
        self,
        method: str,
        path: str,
        json: dict[str, Any] | None = None,
        params: Mapping[str, str] | None = None,
    ) -> AbstractAsyncContextManager[aiohttp.ClientResponse]:
        pass

    async def list_cloud_provider_options(self) -> list[CloudProviderOptions]:
        path = self._endpoints.cloud_providers
        async with self._request("GET", path) as response:
            resp_payload = await response.json()
            result: list[CloudProviderOptions] = []
            for k, v in resp_payload.items():
                result.append(
                    self._entity_factory.create_cloud_provider_options(
                        CloudProviderType(k), v
                    )
                )
            return result

    async def get_cloud_provider_options(
        self, type: CloudProviderType
    ) -> CloudProviderOptions:
        path = self._endpoints.cloud_provider_options(type)
        async with self._request("GET", path) as response:
            resp_payload = await response.json()
            return self._entity_factory.create_cloud_provider_options(
                type, resp_payload
            )

    async def list_clusters(self) -> Sequence[Cluster]:
        async with self._request("GET", self._endpoints.clusters) as response:
            payload = await response.json()
            return [self._entity_factory.create_cluster(p) for p in payload]

    async def get_cluster(self, name: str) -> Cluster:
        async with self._request("GET", self._endpoints.cluster(name)) as response:
            payload = await response.json()
            return self._entity_factory.create_cluster(payload)

    async def create_blank_cluster(
        self,
        name: str,
        service_token: str,
        *,
        ignore_existing: bool = False,
    ) -> Cluster:
        payload = {"name": name, "token": service_token}
        try:
            async with self._request(
                "POST", self._endpoints.clusters, json=payload
            ) as resp:
                resp_payload = await resp.json()
                return self._entity_factory.create_cluster(resp_payload)
        except ClientResponseError as e:
            is_existing = e.status == 400 and "already exists" in e.message
            if not ignore_existing or is_existing:
                raise
        return await self.get_cluster(name)

    async def patch_cluster(
        self,
        name: str,
        *,
        credentials: CredentialsConfig | None = None,
        storage: StorageConfig | None = None,
        registry: RegistryConfig | None = None,
        orchestrator: OrchestratorConfig | None = None,
        monitoring: MonitoringConfig | None = None,
        secrets: SecretsConfig | None = None,
        metrics: MetricsConfig | None = None,
        disks: DisksConfig | None = None,
        buckets: BucketsConfig | None = None,
        ingress: IngressConfig | None = None,
        dns: DNSConfig | None = None,
    ) -> Cluster:
        path = self._endpoints.cluster(name)
        payload: dict[str, Any] = {}
        if credentials:
            payload["credentials"] = self._payload_factory.create_credentials(
                credentials
            )
        if storage:
            payload["storage"] = self._payload_factory.create_storage(storage)
        if registry:
            payload["registry"] = self._payload_factory.create_registry(registry)
        if orchestrator:
            payload["orchestrator"] = self._payload_factory.create_orchestrator(
                orchestrator
            )
        if monitoring:
            payload["monitoring"] = self._payload_factory.create_monitoring(monitoring)
        if secrets:
            payload["secrets"] = self._payload_factory.create_secrets(secrets)
        if metrics:
            payload["metrics"] = self._payload_factory.create_metrics(metrics)
        if disks:
            payload["disks"] = self._payload_factory.create_disks(disks)
        if buckets:
            payload["buckets"] = self._payload_factory.create_buckets(buckets)
        if ingress:
            payload["ingress"] = self._payload_factory.create_ingress(ingress)
        if dns:
            payload["dns"] = self._payload_factory.create_dns(dns)
        async with self._request("PATCH", path, json=payload) as resp:
            resp_payload = await resp.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def delete_cluster(self, name: str) -> None:
        async with self._request("DELETE", self._endpoints.cluster(name)):
            pass

    async def add_storage(
        self,
        cluster_name: str,
        storage_name: str,
        size: int | None = None,
        *,
        start_deployment: bool = True,
        ignore_existing: bool = False,
    ) -> Cluster:
        try:
            path = self._endpoints.storages(cluster_name)
            payload: dict[str, Any] = {"name": storage_name}
            if size is not None:
                payload["size"] = size
            async with self._request(
                "POST",
                path,
                params={"start_deployment": str(start_deployment).lower()},
                json=payload,
            ) as response:
                resp_payload = await response.json()
                return self._entity_factory.create_cluster(resp_payload)
        except ClientResponseError as e:
            if not ignore_existing or e.status != 409:
                raise
        return await self.get_cluster(cluster_name)

    async def patch_storage(
        self,
        cluster_name: str,
        storage_name: str | None,
        ready: bool | None = None,
        *,
        ignore_not_found: bool = False,
    ) -> Cluster:
        try:
            if storage_name:
                path = self._endpoints.storage(cluster_name, storage_name)
            else:
                path = self._endpoints.storage(cluster_name, "default/entry")
            payload: dict[str, Any] = {}
            if ready is not None:
                payload["ready"] = ready
            async with self._request("PATCH", path, json=payload) as response:
                resp_payload = await response.json()
                return self._entity_factory.create_cluster(resp_payload)
        except ClientResponseError as e:
            if not ignore_not_found or e.status != 404:
                raise
        return await self.get_cluster(cluster_name)

    async def remove_storage(
        self,
        cluster_name: str,
        storage_name: str,
        *,
        start_deployment: bool = True,
        ignore_not_found: bool = False,
    ) -> Cluster:
        try:
            path = self._endpoints.storage(cluster_name, storage_name)
            async with self._request(
                "DELETE",
                path,
                params={"start_deployment": str(start_deployment).lower()},
            ) as response:
                resp_payload = await response.json()
                return self._entity_factory.create_cluster(resp_payload)
        except ClientResponseError as e:
            if not ignore_not_found or e.status != 404:
                raise
        return await self.get_cluster(cluster_name)

    async def get_node_pool(self, cluster_name: str, node_pool_name: str) -> NodePool:
        path = self._endpoints.node_pool(cluster_name, node_pool_name)
        async with self._request("GET", path) as response:
            resp_payload = await response.json()
            return self._entity_factory.create_node_pool(resp_payload)

    async def list_node_pools(self, cluster_name: str) -> list[NodePool]:
        path = self._endpoints.node_pools(cluster_name)
        async with self._request("GET", path) as response:
            resp_payload = await response.json()
            return [self._entity_factory.create_node_pool(n) for n in resp_payload]

    async def add_node_pool(
        self,
        cluster_name: str,
        node_pool: NodePool,
        *,
        start_deployment: bool = True,
    ) -> Cluster:
        """Add new node pool to the existing cluster.
        Cloud provider should be already set up.

        Make sure you use one of the available node pool templates by providing its ID,
            if the cluster is deployed in public cloud (AWS / GCP / Azure / VCD).

        Args:
            cluster_name (str): Name of the cluster within the platform.
            node_pool (NodePool): Node pool instance.
                For templates, you could use template.to_node_pool() method
            start_deployment (bool, optional): Start applying changes. Defaults to True.

        Returns:
            Cluster: Cluster instance with applied changes
        """
        path = self._endpoints.node_pools(cluster_name)
        payload = self._payload_factory.create_node_pool(node_pool)
        async with self._request(
            "POST",
            path,
            params={"start_deployment": str(start_deployment).lower()},
            json=payload,
        ) as response:
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def put_node_pool(
        self,
        cluster_name: str,
        node_pool: NodePool,
        *,
        start_deployment: bool = True,
    ) -> Cluster:
        path = self._endpoints.node_pool(cluster_name, node_pool.name)
        payload = self._payload_factory.create_node_pool(node_pool)
        async with self._request(
            "PUT",
            path,
            params={"start_deployment": str(start_deployment).lower()},
            json=payload,
        ) as response:
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def patch_node_pool(
        self,
        cluster_name: str,
        node_pool_name: str,
        *,
        idle_size: int | None = None,
    ) -> Cluster:
        path = self._endpoints.node_pool(cluster_name, node_pool_name)
        payload: dict[str, Any] = {}
        if idle_size is not None:
            payload["idle_size"] = idle_size
        async with self._request("PATCH", path, json=payload) as response:
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def delete_node_pool(
        self,
        cluster_name: str,
        node_pool_name: str,
        *,
        start_deployment: bool = True,
    ) -> Cluster:
        path = self._endpoints.node_pool(cluster_name, node_pool_name)
        async with self._request(
            "DELETE", path, params={"start_deployment": str(start_deployment).lower()}
        ) as response:
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def notify(
        self,
        cluster_name: str,
        notification_type: NotificationType,
        message: str | None = None,
    ) -> None:
        path = self._endpoints.notifications(cluster_name)
        payload = {"notification_type": notification_type.value}
        if message:
            payload["message"] = message
        async with self._request("POST", path, json=payload):
            pass

    async def list_resource_presets(self, cluster_name: str) -> list[ResourcePreset]:
        path = self._endpoints.resource_presets(cluster_name)
        async with self._request("GET", path) as response:
            resp_payload = await response.json()
            return [
                self._entity_factory.create_resource_preset(p) for p in resp_payload
            ]

    async def get_resource_preset(
        self, cluster_name: str, preset_name: str
    ) -> ResourcePreset:
        path = self._endpoints.resource_preset(cluster_name, preset_name)
        async with self._request("GET", path) as response:
            resp_payload = await response.json()
            return self._entity_factory.create_resource_preset(resp_payload)

    async def add_resource_preset(
        self, cluster_name: str, preset: ResourcePreset
    ) -> Cluster:
        path = self._endpoints.resource_presets(cluster_name)
        payload = self._payload_factory.create_resource_preset(preset)
        async with self._request("POST", path, json=payload) as response:
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def put_resource_preset(
        self, cluster_name: str, preset: ResourcePreset
    ) -> Cluster:
        path = self._endpoints.resource_preset(cluster_name, preset.name)
        payload = self._payload_factory.create_resource_preset(preset)
        async with self._request("PUT", path, json=payload) as response:
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)

    async def delete_resource_preset(
        self, cluster_name: str, preset_name: str
    ) -> Cluster:
        path = self._endpoints.resource_preset(cluster_name, preset_name)
        async with self._request("DELETE", path) as response:
            resp_payload = await response.json()
            return self._entity_factory.create_cluster(resp_payload)


class ConfigClient(ConfigClientBase):
    def __init__(
        self,
        url: URL,
        token: str | None = None,
        timeout: aiohttp.ClientTimeout = aiohttp.client.DEFAULT_TIMEOUT,
        trace_configs: Sequence[aiohttp.TraceConfig] = (),
    ):
        super().__init__()

        self._base_url = url / "api/v1"
        self._token = token
        self._timeout = timeout
        self._trace_configs = trace_configs
        self._client: aiohttp.ClientSession | None = None

    async def __aenter__(self) -> "ConfigClient":
        self._client = await self._create_http_client()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        assert self._client
        await self._client.close()

    async def _create_http_client(self) -> aiohttp.ClientSession:
        client = aiohttp.ClientSession(
            headers=self._create_headers(token=self._token),
            timeout=self._timeout,
            trace_configs=list(self._trace_configs),
        )
        return await client.__aenter__()

    def _create_headers(self, *, token: str | None = None) -> dict[str, str]:
        result = {}
        token = token or self._token
        if token:
            result["Authorization"] = f"Bearer {token}"
        return result

    @asynccontextmanager
    async def _request(
        self, method: str, path: str, **kwargs: Any
    ) -> AsyncIterator[aiohttp.ClientResponse]:
        assert self._client
        assert self._base_url
        url = self._base_url / path
        async with self._client.request(method, url, **kwargs) as response:
            response.raise_for_status()
            yield response
