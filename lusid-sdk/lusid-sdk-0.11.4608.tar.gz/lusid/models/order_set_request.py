# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4608
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class OrderSetRequest(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'order_requests': 'list[OrderRequest]'
    }

    attribute_map = {
        'order_requests': 'orderRequests'
    }

    required_map = {
        'order_requests': 'optional'
    }

    def __init__(self, order_requests=None, local_vars_configuration=None):  # noqa: E501
        """OrderSetRequest - a model defined in OpenAPI"
        
        :param order_requests:  A collection of OrderRequests.
        :type order_requests: list[lusid.OrderRequest]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._order_requests = None
        self.discriminator = None

        self.order_requests = order_requests

    @property
    def order_requests(self):
        """Gets the order_requests of this OrderSetRequest.  # noqa: E501

        A collection of OrderRequests.  # noqa: E501

        :return: The order_requests of this OrderSetRequest.  # noqa: E501
        :rtype: list[lusid.OrderRequest]
        """
        return self._order_requests

    @order_requests.setter
    def order_requests(self, order_requests):
        """Sets the order_requests of this OrderSetRequest.

        A collection of OrderRequests.  # noqa: E501

        :param order_requests: The order_requests of this OrderSetRequest.  # noqa: E501
        :type order_requests: list[lusid.OrderRequest]
        """

        self._order_requests = order_requests

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderSetRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderSetRequest):
            return True

        return self.to_dict() != other.to_dict()
