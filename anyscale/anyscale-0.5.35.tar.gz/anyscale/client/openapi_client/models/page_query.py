# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class PageQuery(object):
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
        'count': 'int',
        'paging_token': 'str'
    }

    attribute_map = {
        'count': 'count',
        'paging_token': 'paging_token'
    }

    def __init__(self, count=10, paging_token=None, local_vars_configuration=None):  # noqa: E501
        """PageQuery - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._paging_token = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if paging_token is not None:
            self.paging_token = paging_token

    @property
    def count(self):
        """Gets the count of this PageQuery.  # noqa: E501

        Number of elements to fetch. Defaults to 10.  # noqa: E501

        :return: The count of this PageQuery.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PageQuery.

        Number of elements to fetch. Defaults to 10.  # noqa: E501

        :param count: The count of this PageQuery.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                count is not None and count < 0):  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def paging_token(self):
        """Gets the paging_token of this PageQuery.  # noqa: E501

        Token used for pagination. If absent, server will return elements from the first page.  # noqa: E501

        :return: The paging_token of this PageQuery.  # noqa: E501
        :rtype: str
        """
        return self._paging_token

    @paging_token.setter
    def paging_token(self, paging_token):
        """Sets the paging_token of this PageQuery.

        Token used for pagination. If absent, server will return elements from the first page.  # noqa: E501

        :param paging_token: The paging_token of this PageQuery.  # noqa: E501
        :type: str
        """

        self._paging_token = paging_token

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
        if not isinstance(other, PageQuery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageQuery):
            return True

        return self.to_dict() != other.to_dict()
