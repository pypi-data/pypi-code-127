# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulpcore.configuration import Configuration


class RBACContentGuardPermission(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'usernames': 'list[object]',
        'groupnames': 'list[object]'
    }

    attribute_map = {
        'usernames': 'usernames',
        'groupnames': 'groupnames'
    }

    def __init__(self, usernames=[], groupnames=[], local_vars_configuration=None):  # noqa: E501
        """RBACContentGuardPermission - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._usernames = None
        self._groupnames = None
        self.discriminator = None

        if usernames is not None:
            self.usernames = usernames
        if groupnames is not None:
            self.groupnames = groupnames

    @property
    def usernames(self):
        """Gets the usernames of this RBACContentGuardPermission.  # noqa: E501


        :return: The usernames of this RBACContentGuardPermission.  # noqa: E501
        :rtype: list[object]
        """
        return self._usernames

    @usernames.setter
    def usernames(self, usernames):
        """Sets the usernames of this RBACContentGuardPermission.


        :param usernames: The usernames of this RBACContentGuardPermission.  # noqa: E501
        :type: list[object]
        """

        self._usernames = usernames

    @property
    def groupnames(self):
        """Gets the groupnames of this RBACContentGuardPermission.  # noqa: E501


        :return: The groupnames of this RBACContentGuardPermission.  # noqa: E501
        :rtype: list[object]
        """
        return self._groupnames

    @groupnames.setter
    def groupnames(self, groupnames):
        """Sets the groupnames of this RBACContentGuardPermission.


        :param groupnames: The groupnames of this RBACContentGuardPermission.  # noqa: E501
        :type: list[object]
        """

        self._groupnames = groupnames

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RBACContentGuardPermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RBACContentGuardPermission):
            return True

        return self.to_dict() != other.to_dict()
