# coding: utf-8

"""
    Signadot API

    API for Signadot Sandboxes  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from signadot_sdk.configuration import Configuration


class ForkEndpoint(object):
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
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'name': 'name',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, name=None, port=None, protocol=None, _configuration=None):  # noqa: E501
        """ForkEndpoint - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def name(self):
        """Gets the name of this ForkEndpoint.  # noqa: E501

        Name of the endpoint  # noqa: E501

        :return: The name of this ForkEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ForkEndpoint.

        Name of the endpoint  # noqa: E501

        :param name: The name of this ForkEndpoint.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port(self):
        """Gets the port of this ForkEndpoint.  # noqa: E501

        Port it will map to on the forked workload  # noqa: E501

        :return: The port of this ForkEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ForkEndpoint.

        Port it will map to on the forked workload  # noqa: E501

        :param port: The port of this ForkEndpoint.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this ForkEndpoint.  # noqa: E501

        Protocol that this endpoint uses  # noqa: E501

        :return: The protocol of this ForkEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ForkEndpoint.

        Protocol that this endpoint uses  # noqa: E501

        :param protocol: The protocol of this ForkEndpoint.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

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
        if issubclass(ForkEndpoint, dict):
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
        if not isinstance(other, ForkEndpoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForkEndpoint):
            return True

        return self.to_dict() != other.to_dict()
