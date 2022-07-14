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
    'GetAnalyzerResult',
    'AwaitableGetAnalyzerResult',
    'get_analyzer',
    'get_analyzer_output',
]

@pulumi.output_type
class GetAnalyzerResult:
    def __init__(__self__, archive_rules=None, arn=None, tags=None):
        if archive_rules and not isinstance(archive_rules, list):
            raise TypeError("Expected argument 'archive_rules' to be a list")
        pulumi.set(__self__, "archive_rules", archive_rules)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="archiveRules")
    def archive_rules(self) -> Optional[Sequence['outputs.AnalyzerArchiveRule']]:
        return pulumi.get(self, "archive_rules")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the analyzer
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.AnalyzerTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetAnalyzerResult(GetAnalyzerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAnalyzerResult(
            archive_rules=self.archive_rules,
            arn=self.arn,
            tags=self.tags)


def get_analyzer(arn: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAnalyzerResult:
    """
    The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account


    :param str arn: Amazon Resource Name (ARN) of the analyzer
    """
    __args__ = dict()
    __args__['arn'] = arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:accessanalyzer:getAnalyzer', __args__, opts=opts, typ=GetAnalyzerResult).value

    return AwaitableGetAnalyzerResult(
        archive_rules=__ret__.archive_rules,
        arn=__ret__.arn,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_analyzer)
def get_analyzer_output(arn: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAnalyzerResult]:
    """
    The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account


    :param str arn: Amazon Resource Name (ARN) of the analyzer
    """
    ...
