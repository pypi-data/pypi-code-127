from typing import TYPE_CHECKING

from python_pachyderm.service import Service
import betterproto.lib.google.protobuf as bp_proto

if TYPE_CHECKING:
    from python_pachyderm.experimental.service import admin_proto

# bp_to_pb: bp_proto.Empty -> empty_pb2.Empty


class AdminMixin:
    """A mixin for admin-related functionality."""

    def inspect_cluster(self) -> "admin_proto.ClusterInfo":
        """Inspects a cluster.

        Returns
        -------
        admin_proto.ClusterInfo
            A protobuf object with info on the cluster.
        """
        return self._req(
            Service.ADMIN,
            "InspectCluster",
            req=bp_proto.Empty(),
        )
