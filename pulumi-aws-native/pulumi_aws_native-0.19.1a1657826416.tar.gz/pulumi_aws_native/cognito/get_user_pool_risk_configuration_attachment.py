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
    'GetUserPoolRiskConfigurationAttachmentResult',
    'AwaitableGetUserPoolRiskConfigurationAttachmentResult',
    'get_user_pool_risk_configuration_attachment',
    'get_user_pool_risk_configuration_attachment_output',
]

@pulumi.output_type
class GetUserPoolRiskConfigurationAttachmentResult:
    def __init__(__self__, account_takeover_risk_configuration=None, compromised_credentials_risk_configuration=None, id=None, risk_exception_configuration=None):
        if account_takeover_risk_configuration and not isinstance(account_takeover_risk_configuration, dict):
            raise TypeError("Expected argument 'account_takeover_risk_configuration' to be a dict")
        pulumi.set(__self__, "account_takeover_risk_configuration", account_takeover_risk_configuration)
        if compromised_credentials_risk_configuration and not isinstance(compromised_credentials_risk_configuration, dict):
            raise TypeError("Expected argument 'compromised_credentials_risk_configuration' to be a dict")
        pulumi.set(__self__, "compromised_credentials_risk_configuration", compromised_credentials_risk_configuration)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if risk_exception_configuration and not isinstance(risk_exception_configuration, dict):
            raise TypeError("Expected argument 'risk_exception_configuration' to be a dict")
        pulumi.set(__self__, "risk_exception_configuration", risk_exception_configuration)

    @property
    @pulumi.getter(name="accountTakeoverRiskConfiguration")
    def account_takeover_risk_configuration(self) -> Optional['outputs.UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationType']:
        return pulumi.get(self, "account_takeover_risk_configuration")

    @property
    @pulumi.getter(name="compromisedCredentialsRiskConfiguration")
    def compromised_credentials_risk_configuration(self) -> Optional['outputs.UserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationType']:
        return pulumi.get(self, "compromised_credentials_risk_configuration")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="riskExceptionConfiguration")
    def risk_exception_configuration(self) -> Optional['outputs.UserPoolRiskConfigurationAttachmentRiskExceptionConfigurationType']:
        return pulumi.get(self, "risk_exception_configuration")


class AwaitableGetUserPoolRiskConfigurationAttachmentResult(GetUserPoolRiskConfigurationAttachmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserPoolRiskConfigurationAttachmentResult(
            account_takeover_risk_configuration=self.account_takeover_risk_configuration,
            compromised_credentials_risk_configuration=self.compromised_credentials_risk_configuration,
            id=self.id,
            risk_exception_configuration=self.risk_exception_configuration)


def get_user_pool_risk_configuration_attachment(id: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserPoolRiskConfigurationAttachmentResult:
    """
    Resource Type definition for AWS::Cognito::UserPoolRiskConfigurationAttachment
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:cognito:getUserPoolRiskConfigurationAttachment', __args__, opts=opts, typ=GetUserPoolRiskConfigurationAttachmentResult).value

    return AwaitableGetUserPoolRiskConfigurationAttachmentResult(
        account_takeover_risk_configuration=__ret__.account_takeover_risk_configuration,
        compromised_credentials_risk_configuration=__ret__.compromised_credentials_risk_configuration,
        id=__ret__.id,
        risk_exception_configuration=__ret__.risk_exception_configuration)


@_utilities.lift_output_func(get_user_pool_risk_configuration_attachment)
def get_user_pool_risk_configuration_attachment_output(id: Optional[pulumi.Input[str]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserPoolRiskConfigurationAttachmentResult]:
    """
    Resource Type definition for AWS::Cognito::UserPoolRiskConfigurationAttachment
    """
    ...
