# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AssociationComplianceSeverity',
    'AssociationSyncCompliance',
    'DocumentAttachmentsSourceKey',
    'DocumentFormat',
    'DocumentType',
    'DocumentUpdateMethod',
]


class AssociationComplianceSeverity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    UNSPECIFIED = "UNSPECIFIED"


class AssociationSyncCompliance(str, Enum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"


class DocumentAttachmentsSourceKey(str, Enum):
    """
    The key of a key-value pair that identifies the location of an attachment to a document.
    """
    SOURCE_URL = "SourceUrl"
    S3_FILE_URL = "S3FileUrl"
    ATTACHMENT_REFERENCE = "AttachmentReference"


class DocumentFormat(str, Enum):
    """
    Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
    """
    YAML = "YAML"
    JSON = "JSON"
    TEXT = "TEXT"


class DocumentType(str, Enum):
    """
    The type of document to create.
    """
    APPLICATION_CONFIGURATION = "ApplicationConfiguration"
    APPLICATION_CONFIGURATION_SCHEMA = "ApplicationConfigurationSchema"
    AUTOMATION = "Automation"
    AUTOMATION_CHANGE_TEMPLATE = "Automation.ChangeTemplate"
    CHANGE_CALENDAR = "ChangeCalendar"
    CLOUD_FORMATION = "CloudFormation"
    COMMAND = "Command"
    DEPLOYMENT_STRATEGY = "DeploymentStrategy"
    PACKAGE = "Package"
    POLICY = "Policy"
    PROBLEM_ANALYSIS = "ProblemAnalysis"
    PROBLEM_ANALYSIS_TEMPLATE = "ProblemAnalysisTemplate"
    SESSION = "Session"


class DocumentUpdateMethod(str, Enum):
    """
    Update method - when set to 'Replace', the update will replace the existing document; when set to 'NewVersion', the update will create a new version.
    """
    REPLACE = "Replace"
    NEW_VERSION = "NewVersion"
