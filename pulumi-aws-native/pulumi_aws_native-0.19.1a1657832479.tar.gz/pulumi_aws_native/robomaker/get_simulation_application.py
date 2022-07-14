# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetSimulationApplicationResult',
    'AwaitableGetSimulationApplicationResult',
    'get_simulation_application',
    'get_simulation_application_output',
]

@pulumi.output_type
class GetSimulationApplicationResult:
    def __init__(__self__, arn=None, current_revision_id=None, environment=None, rendering_engine=None, robot_software_suite=None, simulation_software_suite=None, sources=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if current_revision_id and not isinstance(current_revision_id, str):
            raise TypeError("Expected argument 'current_revision_id' to be a str")
        pulumi.set(__self__, "current_revision_id", current_revision_id)
        if environment and not isinstance(environment, str):
            raise TypeError("Expected argument 'environment' to be a str")
        pulumi.set(__self__, "environment", environment)
        if rendering_engine and not isinstance(rendering_engine, dict):
            raise TypeError("Expected argument 'rendering_engine' to be a dict")
        pulumi.set(__self__, "rendering_engine", rendering_engine)
        if robot_software_suite and not isinstance(robot_software_suite, dict):
            raise TypeError("Expected argument 'robot_software_suite' to be a dict")
        pulumi.set(__self__, "robot_software_suite", robot_software_suite)
        if simulation_software_suite and not isinstance(simulation_software_suite, dict):
            raise TypeError("Expected argument 'simulation_software_suite' to be a dict")
        pulumi.set(__self__, "simulation_software_suite", simulation_software_suite)
        if sources and not isinstance(sources, list):
            raise TypeError("Expected argument 'sources' to be a list")
        pulumi.set(__self__, "sources", sources)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="currentRevisionId")
    def current_revision_id(self) -> Optional[str]:
        """
        The current revision id.
        """
        return pulumi.get(self, "current_revision_id")

    @property
    @pulumi.getter
    def environment(self) -> Optional[str]:
        """
        The URI of the Docker image for the robot application.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter(name="renderingEngine")
    def rendering_engine(self) -> Optional['outputs.SimulationApplicationRenderingEngine']:
        """
        The rendering engine for the simulation application.
        """
        return pulumi.get(self, "rendering_engine")

    @property
    @pulumi.getter(name="robotSoftwareSuite")
    def robot_software_suite(self) -> Optional['outputs.SimulationApplicationRobotSoftwareSuite']:
        """
        The robot software suite used by the simulation application.
        """
        return pulumi.get(self, "robot_software_suite")

    @property
    @pulumi.getter(name="simulationSoftwareSuite")
    def simulation_software_suite(self) -> Optional['outputs.SimulationApplicationSimulationSoftwareSuite']:
        """
        The simulation software suite used by the simulation application.
        """
        return pulumi.get(self, "simulation_software_suite")

    @property
    @pulumi.getter
    def sources(self) -> Optional[Sequence['outputs.SimulationApplicationSourceConfig']]:
        """
        The sources of the simulation application.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter
    def tags(self) -> Optional['outputs.SimulationApplicationTags']:
        return pulumi.get(self, "tags")


class AwaitableGetSimulationApplicationResult(GetSimulationApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSimulationApplicationResult(
            arn=self.arn,
            current_revision_id=self.current_revision_id,
            environment=self.environment,
            rendering_engine=self.rendering_engine,
            robot_software_suite=self.robot_software_suite,
            simulation_software_suite=self.simulation_software_suite,
            sources=self.sources,
            tags=self.tags)


def get_simulation_application(arn: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSimulationApplicationResult:
    """
    AWS::RoboMaker::SimulationApplication resource creates an AWS RoboMaker SimulationApplication. Simulation application can be used in AWS RoboMaker Simulation Jobs.
    """
    __args__ = dict()
    __args__['arn'] = arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:robomaker:getSimulationApplication', __args__, opts=opts, typ=GetSimulationApplicationResult).value

    return AwaitableGetSimulationApplicationResult(
        arn=__ret__.arn,
        current_revision_id=__ret__.current_revision_id,
        environment=__ret__.environment,
        rendering_engine=__ret__.rendering_engine,
        robot_software_suite=__ret__.robot_software_suite,
        simulation_software_suite=__ret__.simulation_software_suite,
        sources=__ret__.sources,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_simulation_application)
def get_simulation_application_output(arn: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSimulationApplicationResult]:
    """
    AWS::RoboMaker::SimulationApplication resource creates an AWS RoboMaker SimulationApplication. Simulation application can be used in AWS RoboMaker Simulation Jobs.
    """
    ...
