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


class AnyscaledDataplaneConfig(object):
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
        'config': 'str',
        'head_node': 'bool'
    }

    attribute_map = {
        'config': 'config',
        'head_node': 'head_node'
    }

    def __init__(self, config=None, head_node=None, local_vars_configuration=None):  # noqa: E501
        """AnyscaledDataplaneConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config = None
        self._head_node = None
        self.discriminator = None

        self.config = config
        self.head_node = head_node

    @property
    def config(self):
        """Gets the config of this AnyscaledDataplaneConfig.  # noqa: E501


        :return: The config of this AnyscaledDataplaneConfig.  # noqa: E501
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this AnyscaledDataplaneConfig.


        :param config: The config of this AnyscaledDataplaneConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and config is None:  # noqa: E501
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def head_node(self):
        """Gets the head_node of this AnyscaledDataplaneConfig.  # noqa: E501


        :return: The head_node of this AnyscaledDataplaneConfig.  # noqa: E501
        :rtype: bool
        """
        return self._head_node

    @head_node.setter
    def head_node(self, head_node):
        """Sets the head_node of this AnyscaledDataplaneConfig.


        :param head_node: The head_node of this AnyscaledDataplaneConfig.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and head_node is None:  # noqa: E501
            raise ValueError("Invalid value for `head_node`, must not be `None`")  # noqa: E501

        self._head_node = head_node

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
        if not isinstance(other, AnyscaledDataplaneConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnyscaledDataplaneConfig):
            return True

        return self.to_dict() != other.to_dict()
