# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'NotificationRuleDetailType',
    'NotificationRuleStatus',
]


class NotificationRuleDetailType(str, Enum):
    BASIC = "BASIC"
    FULL = "FULL"


class NotificationRuleStatus(str, Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
