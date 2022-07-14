# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['EntitlementArgs', 'Entitlement']

@pulumi.input_type
class EntitlementArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 customer_id: pulumi.Input[str],
                 offer: pulumi.Input[str],
                 association_info: Optional[pulumi.Input['GoogleCloudChannelV1AssociationInfoArgs']] = None,
                 commitment_settings: Optional[pulumi.Input['GoogleCloudChannelV1CommitmentSettingsArgs']] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudChannelV1ParameterArgs']]]] = None,
                 purchase_order_id: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Entitlement resource.
        :param pulumi.Input[str] offer: The offer resource name for which the entitlement is to be created. Takes the form: accounts/{account_id}/offers/{offer_id}.
        :param pulumi.Input['GoogleCloudChannelV1AssociationInfoArgs'] association_info: Association information to other entitlements.
        :param pulumi.Input['GoogleCloudChannelV1CommitmentSettingsArgs'] commitment_settings: Commitment settings for a commitment-based Offer. Required for commitment based offers.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudChannelV1ParameterArgs']]] parameters: Extended entitlement parameters. When creating an entitlement, valid parameter names and values are defined in the Offer.parameter_definitions. The response may include the following output-only Parameters: - assigned_units: The number of licenses assigned to users. - max_units: The maximum assignable units for a flexible offer. - num_units: The total commitment for commitment-based offers.
        :param pulumi.Input[str] purchase_order_id: Optional. This purchase order (PO) information is for resellers to use for their company tracking usage. If a purchaseOrderId value is given, it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. This is only supported for Google Workspace entitlements.
        :param pulumi.Input[str] request_id: Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete. For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request. The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`).
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "customer_id", customer_id)
        pulumi.set(__self__, "offer", offer)
        if association_info is not None:
            pulumi.set(__self__, "association_info", association_info)
        if commitment_settings is not None:
            pulumi.set(__self__, "commitment_settings", commitment_settings)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if purchase_order_id is not None:
            pulumi.set(__self__, "purchase_order_id", purchase_order_id)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "customer_id")

    @customer_id.setter
    def customer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "customer_id", value)

    @property
    @pulumi.getter
    def offer(self) -> pulumi.Input[str]:
        """
        The offer resource name for which the entitlement is to be created. Takes the form: accounts/{account_id}/offers/{offer_id}.
        """
        return pulumi.get(self, "offer")

    @offer.setter
    def offer(self, value: pulumi.Input[str]):
        pulumi.set(self, "offer", value)

    @property
    @pulumi.getter(name="associationInfo")
    def association_info(self) -> Optional[pulumi.Input['GoogleCloudChannelV1AssociationInfoArgs']]:
        """
        Association information to other entitlements.
        """
        return pulumi.get(self, "association_info")

    @association_info.setter
    def association_info(self, value: Optional[pulumi.Input['GoogleCloudChannelV1AssociationInfoArgs']]):
        pulumi.set(self, "association_info", value)

    @property
    @pulumi.getter(name="commitmentSettings")
    def commitment_settings(self) -> Optional[pulumi.Input['GoogleCloudChannelV1CommitmentSettingsArgs']]:
        """
        Commitment settings for a commitment-based Offer. Required for commitment based offers.
        """
        return pulumi.get(self, "commitment_settings")

    @commitment_settings.setter
    def commitment_settings(self, value: Optional[pulumi.Input['GoogleCloudChannelV1CommitmentSettingsArgs']]):
        pulumi.set(self, "commitment_settings", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudChannelV1ParameterArgs']]]]:
        """
        Extended entitlement parameters. When creating an entitlement, valid parameter names and values are defined in the Offer.parameter_definitions. The response may include the following output-only Parameters: - assigned_units: The number of licenses assigned to users. - max_units: The maximum assignable units for a flexible offer. - num_units: The total commitment for commitment-based offers.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudChannelV1ParameterArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="purchaseOrderId")
    def purchase_order_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. This purchase order (PO) information is for resellers to use for their company tracking usage. If a purchaseOrderId value is given, it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. This is only supported for Google Workspace entitlements.
        """
        return pulumi.get(self, "purchase_order_id")

    @purchase_order_id.setter
    def purchase_order_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "purchase_order_id", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete. For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request. The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`).
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)


class Entitlement(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 association_info: Optional[pulumi.Input[pulumi.InputType['GoogleCloudChannelV1AssociationInfoArgs']]] = None,
                 commitment_settings: Optional[pulumi.Input[pulumi.InputType['GoogleCloudChannelV1CommitmentSettingsArgs']]] = None,
                 customer_id: Optional[pulumi.Input[str]] = None,
                 offer: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudChannelV1ParameterArgs']]]]] = None,
                 purchase_order_id: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an entitlement for a customer. Possible error codes: * PERMISSION_DENIED: The customer doesn't belong to the reseller. * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * There is already a customer entitlement for a SKU from the same product family. * INVALID_VALUE: Make sure the OfferId is valid. If it is, contact Google Channel support for further troubleshooting. * NOT_FOUND: The customer or offer resource was not found. * ALREADY_EXISTS: * The SKU was already purchased for the customer. * The customer's primary email already exists. Retry after changing the customer's primary contact email. * CONDITION_NOT_MET or FAILED_PRECONDITION: * The domain required for purchasing a SKU has not been verified. * A pre-requisite SKU required to purchase an Add-On SKU is missing. For example, Google Workspace Business Starter is required to purchase Vault or Drive. * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.
        Auto-naming is currently not supported for this resource.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudChannelV1AssociationInfoArgs']] association_info: Association information to other entitlements.
        :param pulumi.Input[pulumi.InputType['GoogleCloudChannelV1CommitmentSettingsArgs']] commitment_settings: Commitment settings for a commitment-based Offer. Required for commitment based offers.
        :param pulumi.Input[str] offer: The offer resource name for which the entitlement is to be created. Takes the form: accounts/{account_id}/offers/{offer_id}.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudChannelV1ParameterArgs']]]] parameters: Extended entitlement parameters. When creating an entitlement, valid parameter names and values are defined in the Offer.parameter_definitions. The response may include the following output-only Parameters: - assigned_units: The number of licenses assigned to users. - max_units: The maximum assignable units for a flexible offer. - num_units: The total commitment for commitment-based offers.
        :param pulumi.Input[str] purchase_order_id: Optional. This purchase order (PO) information is for resellers to use for their company tracking usage. If a purchaseOrderId value is given, it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. This is only supported for Google Workspace entitlements.
        :param pulumi.Input[str] request_id: Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete. For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request. The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EntitlementArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an entitlement for a customer. Possible error codes: * PERMISSION_DENIED: The customer doesn't belong to the reseller. * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * There is already a customer entitlement for a SKU from the same product family. * INVALID_VALUE: Make sure the OfferId is valid. If it is, contact Google Channel support for further troubleshooting. * NOT_FOUND: The customer or offer resource was not found. * ALREADY_EXISTS: * The SKU was already purchased for the customer. * The customer's primary email already exists. Retry after changing the customer's primary contact email. * CONDITION_NOT_MET or FAILED_PRECONDITION: * The domain required for purchasing a SKU has not been verified. * A pre-requisite SKU required to purchase an Add-On SKU is missing. For example, Google Workspace Business Starter is required to purchase Vault or Drive. * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.
        Auto-naming is currently not supported for this resource.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param EntitlementArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EntitlementArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 association_info: Optional[pulumi.Input[pulumi.InputType['GoogleCloudChannelV1AssociationInfoArgs']]] = None,
                 commitment_settings: Optional[pulumi.Input[pulumi.InputType['GoogleCloudChannelV1CommitmentSettingsArgs']]] = None,
                 customer_id: Optional[pulumi.Input[str]] = None,
                 offer: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudChannelV1ParameterArgs']]]]] = None,
                 purchase_order_id: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        else:
            opts = copy.copy(opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EntitlementArgs.__new__(EntitlementArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["association_info"] = association_info
            __props__.__dict__["commitment_settings"] = commitment_settings
            if customer_id is None and not opts.urn:
                raise TypeError("Missing required property 'customer_id'")
            __props__.__dict__["customer_id"] = customer_id
            if offer is None and not opts.urn:
                raise TypeError("Missing required property 'offer'")
            __props__.__dict__["offer"] = offer
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["purchase_order_id"] = purchase_order_id
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioned_service"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["suspension_reasons"] = None
            __props__.__dict__["trial_settings"] = None
            __props__.__dict__["update_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["account_id", "customer_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Entitlement, __self__).__init__(
            'google-native:cloudchannel/v1:Entitlement',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Entitlement':
        """
        Get an existing Entitlement resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EntitlementArgs.__new__(EntitlementArgs)

        __props__.__dict__["account_id"] = None
        __props__.__dict__["association_info"] = None
        __props__.__dict__["commitment_settings"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["customer_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["offer"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["provisioned_service"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["purchase_order_id"] = None
        __props__.__dict__["suspension_reasons"] = None
        __props__.__dict__["trial_settings"] = None
        __props__.__dict__["update_time"] = None
        return Entitlement(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="associationInfo")
    def association_info(self) -> pulumi.Output['outputs.GoogleCloudChannelV1AssociationInfoResponse']:
        """
        Association information to other entitlements.
        """
        return pulumi.get(self, "association_info")

    @property
    @pulumi.getter(name="commitmentSettings")
    def commitment_settings(self) -> pulumi.Output['outputs.GoogleCloudChannelV1CommitmentSettingsResponse']:
        """
        Commitment settings for a commitment-based Offer. Required for commitment based offers.
        """
        return pulumi.get(self, "commitment_settings")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time at which the entitlement is created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "customer_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of an entitlement in the form: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def offer(self) -> pulumi.Output[str]:
        """
        The offer resource name for which the entitlement is to be created. Takes the form: accounts/{account_id}/offers/{offer_id}.
        """
        return pulumi.get(self, "offer")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Sequence['outputs.GoogleCloudChannelV1ParameterResponse']]:
        """
        Extended entitlement parameters. When creating an entitlement, valid parameter names and values are defined in the Offer.parameter_definitions. The response may include the following output-only Parameters: - assigned_units: The number of licenses assigned to users. - max_units: The maximum assignable units for a flexible offer. - num_units: The total commitment for commitment-based offers.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisionedService")
    def provisioned_service(self) -> pulumi.Output['outputs.GoogleCloudChannelV1ProvisionedServiceResponse']:
        """
        Service provisioning details for the entitlement.
        """
        return pulumi.get(self, "provisioned_service")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Current provisioning state of the entitlement.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="purchaseOrderId")
    def purchase_order_id(self) -> pulumi.Output[str]:
        """
        Optional. This purchase order (PO) information is for resellers to use for their company tracking usage. If a purchaseOrderId value is given, it appears in the API responses and shows up in the invoice. The property accepts up to 80 plain text characters. This is only supported for Google Workspace entitlements.
        """
        return pulumi.get(self, "purchase_order_id")

    @property
    @pulumi.getter(name="suspensionReasons")
    def suspension_reasons(self) -> pulumi.Output[Sequence[str]]:
        """
        Enumerable of all current suspension reasons for an entitlement.
        """
        return pulumi.get(self, "suspension_reasons")

    @property
    @pulumi.getter(name="trialSettings")
    def trial_settings(self) -> pulumi.Output['outputs.GoogleCloudChannelV1TrialSettingsResponse']:
        """
        Settings for trial offers.
        """
        return pulumi.get(self, "trial_settings")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time at which the entitlement is updated.
        """
        return pulumi.get(self, "update_time")

