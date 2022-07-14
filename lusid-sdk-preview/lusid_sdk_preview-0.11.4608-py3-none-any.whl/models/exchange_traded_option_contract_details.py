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


class ExchangeTradedOptionContractDetails(object):
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
        'dom_ccy': 'str',
        'strike': 'float',
        'contract_size': 'float',
        'country': 'str',
        'delivery_type': 'str',
        'description': 'str',
        'exchange_code': 'str',
        'exercise_date': 'datetime',
        'exercise_type': 'str',
        'option_code': 'str',
        'option_type': 'str',
        'underlying': 'LusidInstrument',
        'underlying_code': 'str'
    }

    attribute_map = {
        'dom_ccy': 'domCcy',
        'strike': 'strike',
        'contract_size': 'contractSize',
        'country': 'country',
        'delivery_type': 'deliveryType',
        'description': 'description',
        'exchange_code': 'exchangeCode',
        'exercise_date': 'exerciseDate',
        'exercise_type': 'exerciseType',
        'option_code': 'optionCode',
        'option_type': 'optionType',
        'underlying': 'underlying',
        'underlying_code': 'underlyingCode'
    }

    required_map = {
        'dom_ccy': 'required',
        'strike': 'required',
        'contract_size': 'required',
        'country': 'required',
        'delivery_type': 'required',
        'description': 'required',
        'exchange_code': 'required',
        'exercise_date': 'required',
        'exercise_type': 'required',
        'option_code': 'required',
        'option_type': 'required',
        'underlying': 'required',
        'underlying_code': 'required'
    }

    def __init__(self, dom_ccy=None, strike=None, contract_size=None, country=None, delivery_type=None, description=None, exchange_code=None, exercise_date=None, exercise_type=None, option_code=None, option_type=None, underlying=None, underlying_code=None, local_vars_configuration=None):  # noqa: E501
        """ExchangeTradedOptionContractDetails - a model defined in OpenAPI"
        
        :param dom_ccy:  Currency in which the contract is paid. (required)
        :type dom_ccy: str
        :param strike:  The option strike, this can be negative for some options. (required)
        :type strike: float
        :param contract_size:  Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such. (required)
        :type contract_size: float
        :param country:  Country (code) for the exchange. (required)
        :type country: str
        :param delivery_type:  The delivery type, cash or physical. An option on a future is physically settled if upon exercising the  holder receives a future.    Supported string (enumeration) values are: [Cash, Physical]. (required)
        :type delivery_type: str
        :param description:  Description of contract (required)
        :type description: str
        :param exchange_code:  Exchange code for contract    Supported string (enumeration) values are: [ASX, CBOT, CBF, CME, CMX, EOP, HKG, KFE, MFM, OSE, SGX, NYBOT, KCBT, MGE, MATIF, SFE, NYFE, NYM, LIFFE, EUREX, ICE, MSE, NASDAQ, EEX, LME, MIL, MEXDER]. (required)
        :type exchange_code: str
        :param exercise_date:  Exercise Date. (required)
        :type exercise_date: datetime
        :param exercise_type:  The exercise type, European, American or Bermudan.    Supported string (enumeration) values are: [European, Bermudan, American]. (required)
        :type exercise_type: str
        :param option_code:  Option Contract Code, typically one or two letters, e.g. OG => Option on Gold. (required)
        :type option_code: str
        :param option_type:  The option type, Call or Put.    Supported string (enumeration) values are: [Call, Put]. (required)
        :type option_type: str
        :param underlying:  (required)
        :type underlying: lusid.LusidInstrument
        :param underlying_code:  Code of the underlying, for an option on futures this should be the futures code. (required)
        :type underlying_code: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dom_ccy = None
        self._strike = None
        self._contract_size = None
        self._country = None
        self._delivery_type = None
        self._description = None
        self._exchange_code = None
        self._exercise_date = None
        self._exercise_type = None
        self._option_code = None
        self._option_type = None
        self._underlying = None
        self._underlying_code = None
        self.discriminator = None

        self.dom_ccy = dom_ccy
        self.strike = strike
        self.contract_size = contract_size
        self.country = country
        self.delivery_type = delivery_type
        self.description = description
        self.exchange_code = exchange_code
        self.exercise_date = exercise_date
        self.exercise_type = exercise_type
        self.option_code = option_code
        self.option_type = option_type
        self.underlying = underlying
        self.underlying_code = underlying_code

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this ExchangeTradedOptionContractDetails.  # noqa: E501

        Currency in which the contract is paid.  # noqa: E501

        :return: The dom_ccy of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this ExchangeTradedOptionContractDetails.

        Currency in which the contract is paid.  # noqa: E501

        :param dom_ccy: The dom_ccy of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def strike(self):
        """Gets the strike of this ExchangeTradedOptionContractDetails.  # noqa: E501

        The option strike, this can be negative for some options.  # noqa: E501

        :return: The strike of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: float
        """
        return self._strike

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this ExchangeTradedOptionContractDetails.

        The option strike, this can be negative for some options.  # noqa: E501

        :param strike: The strike of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type strike: float
        """
        if self.local_vars_configuration.client_side_validation and strike is None:  # noqa: E501
            raise ValueError("Invalid value for `strike`, must not be `None`")  # noqa: E501

        self._strike = strike

    @property
    def contract_size(self):
        """Gets the contract_size of this ExchangeTradedOptionContractDetails.  # noqa: E501

        Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such.  # noqa: E501

        :return: The contract_size of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: float
        """
        return self._contract_size

    @contract_size.setter
    def contract_size(self, contract_size):
        """Sets the contract_size of this ExchangeTradedOptionContractDetails.

        Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such.  # noqa: E501

        :param contract_size: The contract_size of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type contract_size: float
        """
        if self.local_vars_configuration.client_side_validation and contract_size is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_size`, must not be `None`")  # noqa: E501

        self._contract_size = contract_size

    @property
    def country(self):
        """Gets the country of this ExchangeTradedOptionContractDetails.  # noqa: E501

        Country (code) for the exchange.  # noqa: E501

        :return: The country of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ExchangeTradedOptionContractDetails.

        Country (code) for the exchange.  # noqa: E501

        :param country: The country of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type country: str
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def delivery_type(self):
        """Gets the delivery_type of this ExchangeTradedOptionContractDetails.  # noqa: E501

        The delivery type, cash or physical. An option on a future is physically settled if upon exercising the  holder receives a future.    Supported string (enumeration) values are: [Cash, Physical].  # noqa: E501

        :return: The delivery_type of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, delivery_type):
        """Sets the delivery_type of this ExchangeTradedOptionContractDetails.

        The delivery type, cash or physical. An option on a future is physically settled if upon exercising the  holder receives a future.    Supported string (enumeration) values are: [Cash, Physical].  # noqa: E501

        :param delivery_type: The delivery_type of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type delivery_type: str
        """
        if self.local_vars_configuration.client_side_validation and delivery_type is None:  # noqa: E501
            raise ValueError("Invalid value for `delivery_type`, must not be `None`")  # noqa: E501

        self._delivery_type = delivery_type

    @property
    def description(self):
        """Gets the description of this ExchangeTradedOptionContractDetails.  # noqa: E501

        Description of contract  # noqa: E501

        :return: The description of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExchangeTradedOptionContractDetails.

        Description of contract  # noqa: E501

        :param description: The description of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def exchange_code(self):
        """Gets the exchange_code of this ExchangeTradedOptionContractDetails.  # noqa: E501

        Exchange code for contract    Supported string (enumeration) values are: [ASX, CBOT, CBF, CME, CMX, EOP, HKG, KFE, MFM, OSE, SGX, NYBOT, KCBT, MGE, MATIF, SFE, NYFE, NYM, LIFFE, EUREX, ICE, MSE, NASDAQ, EEX, LME, MIL, MEXDER].  # noqa: E501

        :return: The exchange_code of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._exchange_code

    @exchange_code.setter
    def exchange_code(self, exchange_code):
        """Sets the exchange_code of this ExchangeTradedOptionContractDetails.

        Exchange code for contract    Supported string (enumeration) values are: [ASX, CBOT, CBF, CME, CMX, EOP, HKG, KFE, MFM, OSE, SGX, NYBOT, KCBT, MGE, MATIF, SFE, NYFE, NYM, LIFFE, EUREX, ICE, MSE, NASDAQ, EEX, LME, MIL, MEXDER].  # noqa: E501

        :param exchange_code: The exchange_code of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type exchange_code: str
        """
        if self.local_vars_configuration.client_side_validation and exchange_code is None:  # noqa: E501
            raise ValueError("Invalid value for `exchange_code`, must not be `None`")  # noqa: E501

        self._exchange_code = exchange_code

    @property
    def exercise_date(self):
        """Gets the exercise_date of this ExchangeTradedOptionContractDetails.  # noqa: E501

        Exercise Date.  # noqa: E501

        :return: The exercise_date of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._exercise_date

    @exercise_date.setter
    def exercise_date(self, exercise_date):
        """Sets the exercise_date of this ExchangeTradedOptionContractDetails.

        Exercise Date.  # noqa: E501

        :param exercise_date: The exercise_date of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type exercise_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and exercise_date is None:  # noqa: E501
            raise ValueError("Invalid value for `exercise_date`, must not be `None`")  # noqa: E501

        self._exercise_date = exercise_date

    @property
    def exercise_type(self):
        """Gets the exercise_type of this ExchangeTradedOptionContractDetails.  # noqa: E501

        The exercise type, European, American or Bermudan.    Supported string (enumeration) values are: [European, Bermudan, American].  # noqa: E501

        :return: The exercise_type of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._exercise_type

    @exercise_type.setter
    def exercise_type(self, exercise_type):
        """Sets the exercise_type of this ExchangeTradedOptionContractDetails.

        The exercise type, European, American or Bermudan.    Supported string (enumeration) values are: [European, Bermudan, American].  # noqa: E501

        :param exercise_type: The exercise_type of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type exercise_type: str
        """
        if self.local_vars_configuration.client_side_validation and exercise_type is None:  # noqa: E501
            raise ValueError("Invalid value for `exercise_type`, must not be `None`")  # noqa: E501

        self._exercise_type = exercise_type

    @property
    def option_code(self):
        """Gets the option_code of this ExchangeTradedOptionContractDetails.  # noqa: E501

        Option Contract Code, typically one or two letters, e.g. OG => Option on Gold.  # noqa: E501

        :return: The option_code of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._option_code

    @option_code.setter
    def option_code(self, option_code):
        """Sets the option_code of this ExchangeTradedOptionContractDetails.

        Option Contract Code, typically one or two letters, e.g. OG => Option on Gold.  # noqa: E501

        :param option_code: The option_code of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type option_code: str
        """
        if self.local_vars_configuration.client_side_validation and option_code is None:  # noqa: E501
            raise ValueError("Invalid value for `option_code`, must not be `None`")  # noqa: E501

        self._option_code = option_code

    @property
    def option_type(self):
        """Gets the option_type of this ExchangeTradedOptionContractDetails.  # noqa: E501

        The option type, Call or Put.    Supported string (enumeration) values are: [Call, Put].  # noqa: E501

        :return: The option_type of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        """Sets the option_type of this ExchangeTradedOptionContractDetails.

        The option type, Call or Put.    Supported string (enumeration) values are: [Call, Put].  # noqa: E501

        :param option_type: The option_type of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type option_type: str
        """
        if self.local_vars_configuration.client_side_validation and option_type is None:  # noqa: E501
            raise ValueError("Invalid value for `option_type`, must not be `None`")  # noqa: E501

        self._option_type = option_type

    @property
    def underlying(self):
        """Gets the underlying of this ExchangeTradedOptionContractDetails.  # noqa: E501


        :return: The underlying of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: lusid.LusidInstrument
        """
        return self._underlying

    @underlying.setter
    def underlying(self, underlying):
        """Sets the underlying of this ExchangeTradedOptionContractDetails.


        :param underlying: The underlying of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type underlying: lusid.LusidInstrument
        """
        if self.local_vars_configuration.client_side_validation and underlying is None:  # noqa: E501
            raise ValueError("Invalid value for `underlying`, must not be `None`")  # noqa: E501

        self._underlying = underlying

    @property
    def underlying_code(self):
        """Gets the underlying_code of this ExchangeTradedOptionContractDetails.  # noqa: E501

        Code of the underlying, for an option on futures this should be the futures code.  # noqa: E501

        :return: The underlying_code of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._underlying_code

    @underlying_code.setter
    def underlying_code(self, underlying_code):
        """Sets the underlying_code of this ExchangeTradedOptionContractDetails.

        Code of the underlying, for an option on futures this should be the futures code.  # noqa: E501

        :param underlying_code: The underlying_code of this ExchangeTradedOptionContractDetails.  # noqa: E501
        :type underlying_code: str
        """
        if self.local_vars_configuration.client_side_validation and underlying_code is None:  # noqa: E501
            raise ValueError("Invalid value for `underlying_code`, must not be `None`")  # noqa: E501

        self._underlying_code = underlying_code

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
        if not isinstance(other, ExchangeTradedOptionContractDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExchangeTradedOptionContractDetails):
            return True

        return self.to_dict() != other.to_dict()
