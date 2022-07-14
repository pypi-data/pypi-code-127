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
    'GetAppResult',
    'AwaitableGetAppResult',
    'get_app',
    'get_app_output',
]

@pulumi.output_type
class GetAppResult:
    def __init__(__self__, app_arn=None, resource_spec=None):
        if app_arn and not isinstance(app_arn, str):
            raise TypeError("Expected argument 'app_arn' to be a str")
        pulumi.set(__self__, "app_arn", app_arn)
        if resource_spec and not isinstance(resource_spec, dict):
            raise TypeError("Expected argument 'resource_spec' to be a dict")
        pulumi.set(__self__, "resource_spec", resource_spec)

    @property
    @pulumi.getter(name="appArn")
    def app_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the app.
        """
        return pulumi.get(self, "app_arn")

    @property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> Optional['outputs.AppResourceSpec']:
        """
        The instance type and the Amazon Resource Name (ARN) of the SageMaker image created on the instance.
        """
        return pulumi.get(self, "resource_spec")


class AwaitableGetAppResult(GetAppResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppResult(
            app_arn=self.app_arn,
            resource_spec=self.resource_spec)


def get_app(app_name: Optional[str] = None,
            app_type: Optional['AppType'] = None,
            domain_id: Optional[str] = None,
            user_profile_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppResult:
    """
    Resource Type definition for AWS::SageMaker::App


    :param str app_name: The name of the app.
    :param 'AppType' app_type: The type of app.
    :param str domain_id: The domain ID.
    :param str user_profile_name: The user profile name.
    """
    __args__ = dict()
    __args__['appName'] = app_name
    __args__['appType'] = app_type
    __args__['domainId'] = domain_id
    __args__['userProfileName'] = user_profile_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getApp', __args__, opts=opts, typ=GetAppResult).value

    return AwaitableGetAppResult(
        app_arn=__ret__.app_arn,
        resource_spec=__ret__.resource_spec)


@_utilities.lift_output_func(get_app)
def get_app_output(app_name: Optional[pulumi.Input[str]] = None,
                   app_type: Optional[pulumi.Input['AppType']] = None,
                   domain_id: Optional[pulumi.Input[str]] = None,
                   user_profile_name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppResult]:
    """
    Resource Type definition for AWS::SageMaker::App


    :param str app_name: The name of the app.
    :param 'AppType' app_type: The type of app.
    :param str domain_id: The domain ID.
    :param str user_profile_name: The user profile name.
    """
    ...
