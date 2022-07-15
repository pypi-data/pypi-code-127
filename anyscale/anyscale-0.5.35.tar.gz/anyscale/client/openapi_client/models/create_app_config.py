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


class CreateAppConfig(object):
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
        'name': 'str',
        'project_id': 'str',
        'config_json': 'CreateAppConfigConfigurationSchema'
    }

    attribute_map = {
        'name': 'name',
        'project_id': 'project_id',
        'config_json': 'config_json'
    }

    def __init__(self, name=None, project_id=None, config_json=None, local_vars_configuration=None):  # noqa: E501
        """CreateAppConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._project_id = None
        self._config_json = None
        self.discriminator = None

        self.name = name
        if project_id is not None:
            self.project_id = project_id
        self.config_json = config_json

    @property
    def name(self):
        """Gets the name of this CreateAppConfig.  # noqa: E501

        Name of the App Template.  # noqa: E501

        :return: The name of this CreateAppConfig.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAppConfig.

        Name of the App Template.  # noqa: E501

        :param name: The name of this CreateAppConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this CreateAppConfig.  # noqa: E501

        ID of the Project this App Config is for.  # noqa: E501

        :return: The project_id of this CreateAppConfig.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateAppConfig.

        ID of the Project this App Config is for.  # noqa: E501

        :param project_id: The project_id of this CreateAppConfig.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def config_json(self):
        """Gets the config_json of this CreateAppConfig.  # noqa: E501

        Config JSON to use to create a new App Config.  # noqa: E501

        :return: The config_json of this CreateAppConfig.  # noqa: E501
        :rtype: CreateAppConfigConfigurationSchema
        """
        return self._config_json

    @config_json.setter
    def config_json(self, config_json):
        """Sets the config_json of this CreateAppConfig.

        Config JSON to use to create a new App Config.  # noqa: E501

        :param config_json: The config_json of this CreateAppConfig.  # noqa: E501
        :type: CreateAppConfigConfigurationSchema
        """
        if self.local_vars_configuration.client_side_validation and config_json is None:  # noqa: E501
            raise ValueError("Invalid value for `config_json`, must not be `None`")  # noqa: E501

        self._config_json = config_json

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
        if not isinstance(other, CreateAppConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAppConfig):
            return True

        return self.to_dict() != other.to_dict()
