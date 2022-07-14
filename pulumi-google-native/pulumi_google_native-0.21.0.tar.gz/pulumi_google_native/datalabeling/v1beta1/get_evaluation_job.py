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
    'GetEvaluationJobResult',
    'AwaitableGetEvaluationJobResult',
    'get_evaluation_job',
    'get_evaluation_job_output',
]

@pulumi.output_type
class GetEvaluationJobResult:
    def __init__(__self__, annotation_spec_set=None, attempts=None, create_time=None, description=None, evaluation_job_config=None, label_missing_ground_truth=None, model_version=None, name=None, schedule=None, state=None):
        if annotation_spec_set and not isinstance(annotation_spec_set, str):
            raise TypeError("Expected argument 'annotation_spec_set' to be a str")
        pulumi.set(__self__, "annotation_spec_set", annotation_spec_set)
        if attempts and not isinstance(attempts, list):
            raise TypeError("Expected argument 'attempts' to be a list")
        pulumi.set(__self__, "attempts", attempts)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if evaluation_job_config and not isinstance(evaluation_job_config, dict):
            raise TypeError("Expected argument 'evaluation_job_config' to be a dict")
        pulumi.set(__self__, "evaluation_job_config", evaluation_job_config)
        if label_missing_ground_truth and not isinstance(label_missing_ground_truth, bool):
            raise TypeError("Expected argument 'label_missing_ground_truth' to be a bool")
        pulumi.set(__self__, "label_missing_ground_truth", label_missing_ground_truth)
        if model_version and not isinstance(model_version, str):
            raise TypeError("Expected argument 'model_version' to be a str")
        pulumi.set(__self__, "model_version", model_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schedule and not isinstance(schedule, str):
            raise TypeError("Expected argument 'schedule' to be a str")
        pulumi.set(__self__, "schedule", schedule)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="annotationSpecSet")
    def annotation_spec_set(self) -> str:
        """
        Name of the AnnotationSpecSet describing all the labels that your machine learning model outputs. You must create this resource before you create an evaluation job and provide its name in the following format: "projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}"
        """
        return pulumi.get(self, "annotation_spec_set")

    @property
    @pulumi.getter
    def attempts(self) -> Sequence['outputs.GoogleCloudDatalabelingV1beta1AttemptResponse']:
        """
        Every time the evaluation job runs and an error occurs, the failed attempt is appended to this array.
        """
        return pulumi.get(self, "attempts")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Timestamp of when this evaluation job was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the job. The description can be up to 25,000 characters long.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="evaluationJobConfig")
    def evaluation_job_config(self) -> 'outputs.GoogleCloudDatalabelingV1beta1EvaluationJobConfigResponse':
        """
        Configuration details for the evaluation job.
        """
        return pulumi.get(self, "evaluation_job_config")

    @property
    @pulumi.getter(name="labelMissingGroundTruth")
    def label_missing_ground_truth(self) -> bool:
        """
        Whether you want Data Labeling Service to provide ground truth labels for prediction input. If you want the service to assign human labelers to annotate your data, set this to `true`. If you want to provide your own ground truth labels in the evaluation job's BigQuery table, set this to `false`.
        """
        return pulumi.get(self, "label_missing_ground_truth")

    @property
    @pulumi.getter(name="modelVersion")
    def model_version(self) -> str:
        """
        The [AI Platform Prediction model version](/ml-engine/docs/prediction-overview) to be evaluated. Prediction input and output is sampled from this model version. When creating an evaluation job, specify the model version in the following format: "projects/{project_id}/models/{model_name}/versions/{version_name}" There can only be one evaluation job per model version.
        """
        return pulumi.get(self, "model_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        After you create a job, Data Labeling Service assigns a name to the job with the following format: "projects/{project_id}/evaluationJobs/ {evaluation_job_id}"
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedule(self) -> str:
        """
        Describes the interval at which the job runs. This interval must be at least 1 day, and it is rounded to the nearest day. For example, if you specify a 50-hour interval, the job runs every 2 days. You can provide the schedule in [crontab format](/scheduler/docs/configuring/cron-job-schedules) or in an [English-like format](/appengine/docs/standard/python/config/cronref#schedule_format). Regardless of what you specify, the job will run at 10:00 AM UTC. Only the interval from this schedule is used, not the specific time of day.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Describes the current state of the job.
        """
        return pulumi.get(self, "state")


class AwaitableGetEvaluationJobResult(GetEvaluationJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEvaluationJobResult(
            annotation_spec_set=self.annotation_spec_set,
            attempts=self.attempts,
            create_time=self.create_time,
            description=self.description,
            evaluation_job_config=self.evaluation_job_config,
            label_missing_ground_truth=self.label_missing_ground_truth,
            model_version=self.model_version,
            name=self.name,
            schedule=self.schedule,
            state=self.state)


def get_evaluation_job(evaluation_job_id: Optional[str] = None,
                       project: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEvaluationJobResult:
    """
    Gets an evaluation job by resource name.
    """
    __args__ = dict()
    __args__['evaluationJobId'] = evaluation_job_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:datalabeling/v1beta1:getEvaluationJob', __args__, opts=opts, typ=GetEvaluationJobResult).value

    return AwaitableGetEvaluationJobResult(
        annotation_spec_set=__ret__.annotation_spec_set,
        attempts=__ret__.attempts,
        create_time=__ret__.create_time,
        description=__ret__.description,
        evaluation_job_config=__ret__.evaluation_job_config,
        label_missing_ground_truth=__ret__.label_missing_ground_truth,
        model_version=__ret__.model_version,
        name=__ret__.name,
        schedule=__ret__.schedule,
        state=__ret__.state)


@_utilities.lift_output_func(get_evaluation_job)
def get_evaluation_job_output(evaluation_job_id: Optional[pulumi.Input[str]] = None,
                              project: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEvaluationJobResult]:
    """
    Gets an evaluation job by resource name.
    """
    ...
