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


class SandboxSpec(object):
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
        'cluster': 'str',
        'description': 'str',
        'endpoints': 'list[SandboxEndpoint]',
        'forks': 'list[SandboxForkSpec]',
        'resources': 'list[SandboxResource]',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'cluster': 'cluster',
        'description': 'description',
        'endpoints': 'endpoints',
        'forks': 'forks',
        'resources': 'resources',
        'tags': 'tags'
    }

    def __init__(self, cluster=None, description=None, endpoints=None, forks=None, resources=None, tags=None, _configuration=None):  # noqa: E501
        """SandboxSpec - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cluster = None
        self._description = None
        self._endpoints = None
        self._forks = None
        self._resources = None
        self._tags = None
        self.discriminator = None

        self.cluster = cluster
        if description is not None:
            self.description = description
        if endpoints is not None:
            self.endpoints = endpoints
        self.forks = forks
        if resources is not None:
            self.resources = resources
        if tags is not None:
            self.tags = tags

    @property
    def cluster(self):
        """Gets the cluster of this SandboxSpec.  # noqa: E501

        Cluster within which this sandbox should be created  # noqa: E501

        :return: The cluster of this SandboxSpec.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this SandboxSpec.

        Cluster within which this sandbox should be created  # noqa: E501

        :param cluster: The cluster of this SandboxSpec.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cluster is None:
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def description(self):
        """Gets the description of this SandboxSpec.  # noqa: E501

        Description of the purpose of this sandbox  # noqa: E501

        :return: The description of this SandboxSpec.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SandboxSpec.

        Description of the purpose of this sandbox  # noqa: E501

        :param description: The description of this SandboxSpec.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def endpoints(self):
        """Gets the endpoints of this SandboxSpec.  # noqa: E501

        Endpoints that can be used to point to external DNS names or ingress gateways  # noqa: E501

        :return: The endpoints of this SandboxSpec.  # noqa: E501
        :rtype: list[SandboxEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this SandboxSpec.

        Endpoints that can be used to point to external DNS names or ingress gateways  # noqa: E501

        :param endpoints: The endpoints of this SandboxSpec.  # noqa: E501
        :type: list[SandboxEndpoint]
        """

        self._endpoints = endpoints

    @property
    def forks(self):
        """Gets the forks of this SandboxSpec.  # noqa: E501

        Forks is the specification of each forked entity  # noqa: E501

        :return: The forks of this SandboxSpec.  # noqa: E501
        :rtype: list[SandboxForkSpec]
        """
        return self._forks

    @forks.setter
    def forks(self, forks):
        """Sets the forks of this SandboxSpec.

        Forks is the specification of each forked entity  # noqa: E501

        :param forks: The forks of this SandboxSpec.  # noqa: E501
        :type: list[SandboxForkSpec]
        """
        if self._configuration.client_side_validation and forks is None:
            raise ValueError("Invalid value for `forks`, must not be `None`")  # noqa: E501

        self._forks = forks

    @property
    def resources(self):
        """Gets the resources of this SandboxSpec.  # noqa: E501

        Resources specifies each required resource to spin up the sandbox  # noqa: E501

        :return: The resources of this SandboxSpec.  # noqa: E501
        :rtype: list[SandboxResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this SandboxSpec.

        Resources specifies each required resource to spin up the sandbox  # noqa: E501

        :param resources: The resources of this SandboxSpec.  # noqa: E501
        :type: list[SandboxResource]
        """

        self._resources = resources

    @property
    def tags(self):
        """Gets the tags of this SandboxSpec.  # noqa: E501


        :return: The tags of this SandboxSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SandboxSpec.


        :param tags: The tags of this SandboxSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

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
        if issubclass(SandboxSpec, dict):
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
        if not isinstance(other, SandboxSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxSpec):
            return True

        return self.to_dict() != other.to_dict()
