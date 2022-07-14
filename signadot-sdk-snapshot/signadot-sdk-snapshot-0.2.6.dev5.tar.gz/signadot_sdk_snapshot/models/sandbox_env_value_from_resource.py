# coding: utf-8

"""
    Signadot API

    API for Signadot Sandboxes  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from signadot_sdk_snapshot.configuration import Configuration


class SandboxEnvValueFromResource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'output_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'output_key': 'outputKey'
    }

    def __init__(self, name=None, output_key=None, _configuration=None):  # noqa: E501
        """SandboxEnvValueFromResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._output_key = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if output_key is not None:
            self.output_key = output_key

    @property
    def name(self):
        """Gets the name of this SandboxEnvValueFromResource.  # noqa: E501


        :return: The name of this SandboxEnvValueFromResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SandboxEnvValueFromResource.


        :param name: The name of this SandboxEnvValueFromResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def output_key(self):
        """Gets the output_key of this SandboxEnvValueFromResource.  # noqa: E501


        :return: The output_key of this SandboxEnvValueFromResource.  # noqa: E501
        :rtype: str
        """
        return self._output_key

    @output_key.setter
    def output_key(self, output_key):
        """Sets the output_key of this SandboxEnvValueFromResource.


        :param output_key: The output_key of this SandboxEnvValueFromResource.  # noqa: E501
        :type: str
        """

        self._output_key = output_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SandboxEnvValueFromResource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SandboxEnvValueFromResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxEnvValueFromResource):
            return True

        return self.to_dict() != other.to_dict()
