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


class Sandbox(object):
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
        'created_at': 'str',
        'name': 'str',
        'preview_endpoints': 'list[SandboxPreviewEndpoint]',
        'routing_key': 'str',
        'spec': 'SandboxSpec',
        'status': 'SandboxReadiness'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'name': 'name',
        'preview_endpoints': 'previewEndpoints',
        'routing_key': 'routingKey',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, created_at=None, name=None, preview_endpoints=None, routing_key=None, spec=None, status=None, _configuration=None):  # noqa: E501
        """Sandbox - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._name = None
        self._preview_endpoints = None
        self._routing_key = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if preview_endpoints is not None:
            self.preview_endpoints = preview_endpoints
        if routing_key is not None:
            self.routing_key = routing_key
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def created_at(self):
        """Gets the created_at of this Sandbox.  # noqa: E501


        :return: The created_at of this Sandbox.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Sandbox.


        :param created_at: The created_at of this Sandbox.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this Sandbox.  # noqa: E501

        Human-readable name of this sandbox  # noqa: E501

        :return: The name of this Sandbox.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sandbox.

        Human-readable name of this sandbox  # noqa: E501

        :param name: The name of this Sandbox.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def preview_endpoints(self):
        """Gets the preview_endpoints of this Sandbox.  # noqa: E501


        :return: The preview_endpoints of this Sandbox.  # noqa: E501
        :rtype: list[SandboxPreviewEndpoint]
        """
        return self._preview_endpoints

    @preview_endpoints.setter
    def preview_endpoints(self, preview_endpoints):
        """Sets the preview_endpoints of this Sandbox.


        :param preview_endpoints: The preview_endpoints of this Sandbox.  # noqa: E501
        :type: list[SandboxPreviewEndpoint]
        """

        self._preview_endpoints = preview_endpoints

    @property
    def routing_key(self):
        """Gets the routing_key of this Sandbox.  # noqa: E501


        :return: The routing_key of this Sandbox.  # noqa: E501
        :rtype: str
        """
        return self._routing_key

    @routing_key.setter
    def routing_key(self, routing_key):
        """Sets the routing_key of this Sandbox.


        :param routing_key: The routing_key of this Sandbox.  # noqa: E501
        :type: str
        """

        self._routing_key = routing_key

    @property
    def spec(self):
        """Gets the spec of this Sandbox.  # noqa: E501


        :return: The spec of this Sandbox.  # noqa: E501
        :rtype: SandboxSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this Sandbox.


        :param spec: The spec of this Sandbox.  # noqa: E501
        :type: SandboxSpec
        """

        self._spec = spec

    @property
    def status(self):
        """Gets the status of this Sandbox.  # noqa: E501


        :return: The status of this Sandbox.  # noqa: E501
        :rtype: SandboxReadiness
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Sandbox.


        :param status: The status of this Sandbox.  # noqa: E501
        :type: SandboxReadiness
        """

        self._status = status

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
        if issubclass(Sandbox, dict):
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
        if not isinstance(other, Sandbox):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Sandbox):
            return True

        return self.to_dict() != other.to_dict()
