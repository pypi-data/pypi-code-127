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

__all__ = [
    'GetSkillResult',
    'AwaitableGetSkillResult',
    'get_skill',
    'get_skill_output',
]

@pulumi.output_type
class GetSkillResult:
    def __init__(__self__, authentication_configuration=None, id=None, skill_package=None):
        if authentication_configuration and not isinstance(authentication_configuration, dict):
            raise TypeError("Expected argument 'authentication_configuration' to be a dict")
        pulumi.set(__self__, "authentication_configuration", authentication_configuration)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if skill_package and not isinstance(skill_package, dict):
            raise TypeError("Expected argument 'skill_package' to be a dict")
        pulumi.set(__self__, "skill_package", skill_package)

    @property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> Optional['outputs.SkillAuthenticationConfiguration']:
        return pulumi.get(self, "authentication_configuration")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="skillPackage")
    def skill_package(self) -> Optional['outputs.SkillPackage']:
        return pulumi.get(self, "skill_package")


class AwaitableGetSkillResult(GetSkillResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSkillResult(
            authentication_configuration=self.authentication_configuration,
            id=self.id,
            skill_package=self.skill_package)


def get_skill(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSkillResult:
    """
    Resource Type definition for Alexa::ASK::Skill
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ask:getSkill', __args__, opts=opts, typ=GetSkillResult).value

    return AwaitableGetSkillResult(
        authentication_configuration=__ret__.authentication_configuration,
        id=__ret__.id,
        skill_package=__ret__.skill_package)


@_utilities.lift_output_func(get_skill)
def get_skill_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSkillResult]:
    """
    Resource Type definition for Alexa::ASK::Skill
    """
    ...
