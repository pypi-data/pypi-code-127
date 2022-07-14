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
    'GetPublicRepositoryResult',
    'AwaitableGetPublicRepositoryResult',
    'get_public_repository',
    'get_public_repository_output',
]

@pulumi.output_type
class GetPublicRepositoryResult:
    def __init__(__self__, arn=None, repository_catalog_data=None, repository_policy_text=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if repository_catalog_data and not isinstance(repository_catalog_data, dict):
            raise TypeError("Expected argument 'repository_catalog_data' to be a dict")
        pulumi.set(__self__, "repository_catalog_data", repository_catalog_data)
        if repository_policy_text and not isinstance(repository_policy_text, dict):
            raise TypeError("Expected argument 'repository_policy_text' to be a dict")
        pulumi.set(__self__, "repository_policy_text", repository_policy_text)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="repositoryCatalogData")
    def repository_catalog_data(self) -> Optional['outputs.RepositoryCatalogDataProperties']:
        """
        The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see <link>
        """
        return pulumi.get(self, "repository_catalog_data")

    @property
    @pulumi.getter(name="repositoryPolicyText")
    def repository_policy_text(self) -> Optional[Any]:
        """
        The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide. 
        """
        return pulumi.get(self, "repository_policy_text")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.PublicRepositoryTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetPublicRepositoryResult(GetPublicRepositoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPublicRepositoryResult(
            arn=self.arn,
            repository_catalog_data=self.repository_catalog_data,
            repository_policy_text=self.repository_policy_text,
            tags=self.tags)


def get_public_repository(repository_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPublicRepositoryResult:
    """
    The AWS::ECR::PublicRepository resource specifies an Amazon Elastic Container Public Registry (Amazon Public ECR) repository, where users can push and pull Docker images. For more information, see https://docs.aws.amazon.com/AmazonECR


    :param str repository_name: The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
    """
    __args__ = dict()
    __args__['repositoryName'] = repository_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ecr:getPublicRepository', __args__, opts=opts, typ=GetPublicRepositoryResult).value

    return AwaitableGetPublicRepositoryResult(
        arn=__ret__.arn,
        repository_catalog_data=__ret__.repository_catalog_data,
        repository_policy_text=__ret__.repository_policy_text,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_public_repository)
def get_public_repository_output(repository_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPublicRepositoryResult]:
    """
    The AWS::ECR::PublicRepository resource specifies an Amazon Elastic Container Public Registry (Amazon Public ECR) repository, where users can push and pull Docker images. For more information, see https://docs.aws.amazon.com/AmazonECR


    :param str repository_name: The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
    """
    ...
