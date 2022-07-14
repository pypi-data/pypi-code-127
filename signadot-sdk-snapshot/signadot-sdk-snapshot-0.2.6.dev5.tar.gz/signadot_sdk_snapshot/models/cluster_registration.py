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


class ClusterRegistration(object):
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
        'status': 'ClusterStatus'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, created_at=None, name=None, status=None, _configuration=None):  # noqa: E501
        """ClusterRegistration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._name = None
        self._status = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def created_at(self):
        """Gets the created_at of this ClusterRegistration.  # noqa: E501

        The time when this cluster was registered with Signadot.  # noqa: E501

        :return: The created_at of this ClusterRegistration.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ClusterRegistration.

        The time when this cluster was registered with Signadot.  # noqa: E501

        :param created_at: The created_at of this ClusterRegistration.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this ClusterRegistration.  # noqa: E501

        The name of the cluster.  # noqa: E501

        :return: The name of this ClusterRegistration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterRegistration.

        The name of the cluster.  # noqa: E501

        :param name: The name of this ClusterRegistration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this ClusterRegistration.  # noqa: E501


        :return: The status of this ClusterRegistration.  # noqa: E501
        :rtype: ClusterStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterRegistration.


        :param status: The status of this ClusterRegistration.  # noqa: E501
        :type: ClusterStatus
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
        if issubclass(ClusterRegistration, dict):
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
        if not isinstance(other, ClusterRegistration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterRegistration):
            return True

        return self.to_dict() != other.to_dict()
