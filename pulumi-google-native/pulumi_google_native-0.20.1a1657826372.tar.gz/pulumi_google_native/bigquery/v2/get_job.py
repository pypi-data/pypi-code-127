# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetJobResult',
    'AwaitableGetJobResult',
    'get_job',
    'get_job_output',
]

@pulumi.output_type
class GetJobResult:
    def __init__(__self__, configuration=None, etag=None, job_reference=None, kind=None, self_link=None, statistics=None, status=None, user_email=None):
        if configuration and not isinstance(configuration, dict):
            raise TypeError("Expected argument 'configuration' to be a dict")
        pulumi.set(__self__, "configuration", configuration)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if job_reference and not isinstance(job_reference, dict):
            raise TypeError("Expected argument 'job_reference' to be a dict")
        pulumi.set(__self__, "job_reference", job_reference)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if statistics and not isinstance(statistics, dict):
            raise TypeError("Expected argument 'statistics' to be a dict")
        pulumi.set(__self__, "statistics", statistics)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if user_email and not isinstance(user_email, str):
            raise TypeError("Expected argument 'user_email' to be a str")
        pulumi.set(__self__, "user_email", user_email)

    @property
    @pulumi.getter
    def configuration(self) -> 'outputs.JobConfigurationResponse':
        """
        [Required] Describes the job configuration.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A hash of this resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="jobReference")
    def job_reference(self) -> 'outputs.JobReferenceResponse':
        """
        [Optional] Reference describing the unique-per-user name of the job.
        """
        return pulumi.get(self, "job_reference")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        A URL that can be used to access this resource again.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def statistics(self) -> 'outputs.JobStatisticsResponse':
        """
        Information about the job, including starting time and ending time of the job.
        """
        return pulumi.get(self, "statistics")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.JobStatusResponse':
        """
        The status of this job. Examine this value when polling an asynchronous job to see if the job is complete.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> str:
        """
        Email address of the user who ran the job.
        """
        return pulumi.get(self, "user_email")


class AwaitableGetJobResult(GetJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJobResult(
            configuration=self.configuration,
            etag=self.etag,
            job_reference=self.job_reference,
            kind=self.kind,
            self_link=self.self_link,
            statistics=self.statistics,
            status=self.status,
            user_email=self.user_email)


def get_job(job_id: Optional[str] = None,
            location: Optional[str] = None,
            project: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJobResult:
    """
    Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role.
    """
    __args__ = dict()
    __args__['jobId'] = job_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:bigquery/v2:getJob', __args__, opts=opts, typ=GetJobResult).value

    return AwaitableGetJobResult(
        configuration=__ret__.configuration,
        etag=__ret__.etag,
        job_reference=__ret__.job_reference,
        kind=__ret__.kind,
        self_link=__ret__.self_link,
        statistics=__ret__.statistics,
        status=__ret__.status,
        user_email=__ret__.user_email)


@_utilities.lift_output_func(get_job)
def get_job_output(job_id: Optional[pulumi.Input[str]] = None,
                   location: Optional[pulumi.Input[Optional[str]]] = None,
                   project: Optional[pulumi.Input[Optional[str]]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJobResult]:
    """
    Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role.
    """
    ...
