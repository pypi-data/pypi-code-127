__all__ = ('UserPoint', 'SendPasswordPoint', 'LogPoint')

from phonenumber_field.serializerfields import PhoneNumberField

from expressmoney.api import *

SERVICE = 'auth'


class UserCreateContract(Contract):
    username = PhoneNumberField()
    department = serializers.IntegerField(min_value=1)
    ip = serializers.IPAddressField()
    http_referer = serializers.URLField(allow_blank=True, max_length=2048)


class LogCreateContract(Contract):
    url = serializers.URLField()
    ip = serializers.IPAddressField()
    fingerprint = serializers.CharField(max_length=64, allow_null=True)
    ga = serializers.CharField(max_length=64, allow_null=True)


class SendPasswordCreateContract(Contract):
    user = serializers.IntegerField(min_value=1)


class SendPasswordID(ID):
    _service = SERVICE
    _app = 'users'
    _view_set = 'send_password'


class UserID(ID):
    _service = SERVICE
    _app = 'users'
    _view_set = 'user'


class LogID(ID):
    _service = SERVICE
    _app = 'users'
    _view_set = 'log'


class SendPasswordPoint(CreatePointMixin, ContractPoint):
    _point_id = SendPasswordID()
    _create_contract = SendPasswordCreateContract


class UserPoint(CreatePointMixin, ContractPoint):
    _point_id = UserID()
    _create_contract = UserCreateContract


class LogPoint(CreatePointMixin, ContractPoint):
    _point_id = LogID()
    _create_contract = LogCreateContract
