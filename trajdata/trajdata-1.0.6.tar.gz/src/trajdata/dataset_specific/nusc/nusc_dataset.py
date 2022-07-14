from pathlib import Path
from typing import Dict, List, Optional, Tuple, Type, Union

import numpy as np
import pandas as pd
from nuscenes.map_expansion.map_api import NuScenesMap, locations
from nuscenes.nuscenes import NuScenes
from nuscenes.utils.splits import create_splits_scenes
from tqdm import tqdm

from trajdata.caching import EnvCache, SceneCache
from trajdata.data_structures.agent import (
    Agent,
    AgentMetadata,
    AgentType,
    FixedExtent,
    VariableExtent,
)
from trajdata.data_structures.environment import EnvMetadata
from trajdata.data_structures.map import MapMetadata
from trajdata.data_structures.scene_metadata import Scene, SceneMetadata
from trajdata.data_structures.scene_tag import SceneTag
from trajdata.dataset_specific.nusc import nusc_utils
from trajdata.dataset_specific.raw_dataset import RawDataset
from trajdata.dataset_specific.scene_records import NuscSceneRecord


class NuscDataset(RawDataset):
    def compute_metadata(self, env_name: str, data_dir: str) -> EnvMetadata:
        all_scene_splits: Dict[str, List[str]] = create_splits_scenes()
        if env_name == "nusc_trainval":
            nusc_scene_splits: Dict[str, List[str]] = {
                k: all_scene_splits[k] for k in ["train", "val"]
            }

            # nuScenes possibilities are the Cartesian product of these
            dataset_parts: List[Tuple[str, ...]] = [
                ("train", "val"),
                ("boston", "singapore"),
            ]
        elif env_name == "nusc_test":
            nusc_scene_splits: Dict[str, List[str]] = {
                k: all_scene_splits[k] for k in ["test"]
            }

            # nuScenes possibilities are the Cartesian product of these
            dataset_parts: List[Tuple[str, ...]] = [
                ("test", ),
                ("boston", "singapore"),
            ]
        elif env_name == "nusc_mini":
            nusc_scene_splits: Dict[str, List[str]] = {
                k: all_scene_splits[k] for k in ["mini_train", "mini_val"]
            }

            # nuScenes possibilities are the Cartesian product of these
            dataset_parts: List[Tuple[str, ...]] = [
                ("mini_train", "mini_val"),
                ("boston", "singapore"),
            ]

        # Inverting the dict from above, associating every scene with its data split.
        nusc_scene_split_map: Dict[str, str] = {
            v_elem: k for k, v in nusc_scene_splits.items() for v_elem in v
        }

        return EnvMetadata(
            name=env_name,
            data_dir=data_dir,
            dt=nusc_utils.NUSC_DT,
            parts=dataset_parts,
            scene_split_map=nusc_scene_split_map,
        )

    def load_dataset_obj(self, verbose: bool = False) -> None:
        if verbose:
            print(f"Loading {self.name} dataset...", flush=True)

        if self.name == "nusc_mini":
            version_str = "v1.0-mini"
        elif self.name == "nusc_trainval":
            version_str = "v1.0-trainval"
        elif self.name == "nusc_test":
            version_str = "v1.0-test"

        self.dataset_obj = NuScenes(
            version=version_str, dataroot=self.metadata.data_dir
        )

    def _get_matching_scenes_from_obj(
        self,
        scene_tag: SceneTag,
        scene_desc_contains: Optional[List[str]],
        env_cache: EnvCache,
    ) -> List[SceneMetadata]:
        all_scenes_list: List[NuscSceneRecord] = list()

        scenes_list: List[SceneMetadata] = list()
        for idx, scene_record in enumerate(self.dataset_obj.scene):
            scene_name: str = scene_record["name"]
            scene_desc: str = scene_record["description"].lower()
            scene_location: str = self.dataset_obj.get(
                "log", scene_record["log_token"]
            )["location"]
            scene_split: str = self.metadata.scene_split_map[scene_name]
            scene_length: int = scene_record["nbr_samples"]

            # Saving all scene records for later caching.
            all_scenes_list.append(
                NuscSceneRecord(
                    scene_name, scene_location, scene_length, scene_desc, idx
                )
            )

            if scene_location.split("-")[0] in scene_tag and scene_split in scene_tag:
                if scene_desc_contains is not None and not any(
                    desc_query in scene_desc for desc_query in scene_desc_contains
                ):
                    continue

                scene_metadata = SceneMetadata(
                    env_name=self.metadata.name,
                    name=scene_name,
                    dt=self.metadata.dt,
                    raw_data_idx=idx,
                )
                scenes_list.append(scene_metadata)

        self.cache_all_scenes_list(env_cache, all_scenes_list)
        return scenes_list

    def _get_matching_scenes_from_cache(
        self,
        scene_tag: SceneTag,
        scene_desc_contains: Optional[List[str]],
        env_cache: EnvCache,
    ) -> List[Scene]:
        all_scenes_list: List[NuscSceneRecord] = env_cache.load_env_scenes_list(
            self.name
        )

        scenes_list: List[SceneMetadata] = list()
        for scene_record in all_scenes_list:
            (
                scene_name,
                scene_location,
                scene_length,
                scene_desc,
                data_idx,
            ) = scene_record
            scene_split: str = self.metadata.scene_split_map[scene_name]

            if scene_location.split("-")[0] in scene_tag and scene_split in scene_tag:
                if scene_desc_contains is not None and not any(
                    desc_query in scene_desc for desc_query in scene_desc_contains
                ):
                    continue

                scene_metadata = Scene(
                    self.metadata,
                    scene_name,
                    scene_location,
                    scene_split,
                    scene_length,
                    data_idx,
                    None,  # This isn't used if everything is already cached.
                    scene_desc,
                )
                scenes_list.append(scene_metadata)

        return scenes_list

    def get_scene(self, scene_info: SceneMetadata) -> Scene:
        _, _, _, data_idx = scene_info

        scene_record = self.dataset_obj.scene[data_idx]
        scene_name: str = scene_record["name"]
        scene_desc: str = scene_record["description"].lower()
        scene_location: str = self.dataset_obj.get("log", scene_record["log_token"])[
            "location"
        ]
        scene_split: str = self.metadata.scene_split_map[scene_name]
        scene_length: int = scene_record["nbr_samples"]

        return Scene(
            self.metadata,
            scene_name,
            scene_location,
            scene_split,
            scene_length,
            data_idx,
            scene_record,
            scene_desc,
        )

    def get_agent_info(
        self, scene: Scene, cache_path: Path, cache_class: Type[SceneCache]
    ) -> Tuple[List[AgentMetadata], List[List[AgentMetadata]]]:
        ego_agent_info: AgentMetadata = AgentMetadata(
            name="ego",
            agent_type=AgentType.VEHICLE,
            first_timestep=0,
            last_timestep=scene.length_timesteps - 1,
            extent=FixedExtent(length=4.084, width=1.730, height=1.562),
        )

        agent_presence: List[List[AgentMetadata]] = [
            [ego_agent_info] for _ in range(scene.length_timesteps)
        ]

        agent_data_list: List[pd.DataFrame] = list()
        existing_agents: Dict[str, AgentMetadata] = dict()

        all_frames: List[Dict[str, Union[str, int]]] = list(
            nusc_utils.frame_iterator(self.dataset_obj, scene)
        )
        frame_idx_dict: Dict[str, int] = {
            frame_dict["token"]: idx for idx, frame_dict in enumerate(all_frames)
        }
        for frame_idx, frame_info in enumerate(all_frames):
            for agent_info in nusc_utils.agent_iterator(self.dataset_obj, frame_info):
                if agent_info["instance_token"] in existing_agents:
                    continue

                if not agent_info["next"]:
                    # There are some agents with only a single detection to them, we don't care about these.
                    continue

                agent: Agent = nusc_utils.agg_agent_data(
                    self.dataset_obj, agent_info, frame_idx, frame_idx_dict
                )

                for scene_ts in range(
                    agent.metadata.first_timestep, agent.metadata.last_timestep + 1
                ):
                    agent_presence[scene_ts].append(agent.metadata)

                existing_agents[agent.name] = agent.metadata

                agent_data_list.append(agent.data)

        ego_agent: Agent = nusc_utils.agg_ego_data(self.dataset_obj, scene)
        agent_data_list.append(ego_agent.data)

        agent_list: List[AgentMetadata] = [ego_agent_info] + list(
            existing_agents.values()
        )

        cache_class.save_agent_data(pd.concat(agent_data_list), cache_path, scene)

        return agent_list, agent_presence

    def cache_map(
        self,
        map_name: str,
        layer_names: List[str],
        cache_path: Path,
        map_cache_class: Type[SceneCache],
        resolution: int,
    ) -> None:
        """
        resolution is in pixels per meter.
        """
        if map_cache_class.is_map_cached(cache_path, self.name, map_name):
            return

        nusc_map: NuScenesMap = NuScenesMap(
            dataroot=self.metadata.data_dir, map_name=map_name
        )

        width_m, height_m = nusc_map.canvas_edge
        height_px, width_px = round(height_m * resolution), round(width_m * resolution)

        def layer_fn(layer_name: str) -> np.ndarray:
            # Getting rid of the channels dim by accessing index [0]
            return nusc_map.get_map_mask(
                patch_box=None,
                patch_angle=0,
                layer_names=[layer_name],
                canvas_size=(height_px, width_px),
            )[0].astype(np.bool)

        map_from_world: np.ndarray = np.array(
            [[resolution, 0.0, 0.0], [0.0, resolution, 0.0], [0.0, 0.0, 1.0]]
        )

        map_shape = (len(layer_names), height_px, width_px)
        map_info: MapMetadata = MapMetadata(
            name=map_name,
            shape=map_shape,
            layers=layer_names,
            layer_rgb_groups=([0, 1, 2], [3, 4], [5, 6]),
            resolution=resolution,
            map_from_world=map_from_world,
        )
        map_cache_class.cache_map_layers(cache_path, map_info, layer_fn, self.name)

    def cache_maps(
        self, cache_path: Path, map_cache_class: Type[SceneCache], resolution: int = 2
    ) -> None:
        """
        Stores rasterized maps to disk for later retrieval.

        Below are the map origins (south western corner, in [lat, lon]) for each of
        the 4 maps in nuScenes:
            boston-seaport: [42.336849169438615, -71.05785369873047]
            singapore-onenorth: [1.2882100868743724, 103.78475189208984]
            singapore-hollandvillage: [1.2993652317780957, 103.78217697143555]
            singapore-queenstown: [1.2782562240223188, 103.76741409301758]

        The dimensions of the maps are as follows ([width, height] in meters). They
        can also be found in nusc_utils.py
            singapore-onenorth:       [1585.6, 2025.0]
            singapore-hollandvillage: [2808.3, 2922.9]
            singapore-queenstown:     [3228.6, 3687.1]
            boston-seaport:           [2979.5, 2118.1]
        The rasterized semantic maps published with nuScenes v1.0 have a scale of 10px/m,
        hence the above numbers are the image dimensions divided by 10.

        nuScenes uses the same WGS 84 Web Mercator (EPSG:3857) projection as Google Maps/Earth.
        """
        layer_names: List[str] = [
            "lane",
            "road_segment",
            "drivable_area",
            "road_divider",
            "lane_divider",
            "ped_crossing",
            "walkway",
        ]
        for map_name in tqdm(locations, desc=f"Caching {self.name} Maps"):
            self.cache_map(
                map_name, layer_names, cache_path, map_cache_class, resolution
            )
