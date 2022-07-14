'''
# AWS::GlobalAccelerator Construct Library

## Introduction

AWS Global Accelerator (AGA) is a service that improves the availability and
performance of your applications with local or global users.

It intercepts your user's network connection at an edge location close to
them, and routes it to one of potentially multiple, redundant backends across
the more reliable and less congested AWS global network.

AGA can be used to route traffic to Application Load Balancers, Network Load
Balancers, EC2 Instances and Elastic IP Addresses.

For more information, see the [AWS Global
Accelerator Developer Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GlobalAccelerator.html).

## Example

Here's an example that sets up a Global Accelerator for two Application Load
Balancers in two different AWS Regions:

```python
# Create an Accelerator
accelerator = globalaccelerator.Accelerator(self, "Accelerator")

# Create a Listener
listener = accelerator.add_listener("Listener",
    port_ranges=[globalaccelerator.PortRange(from_port=80), globalaccelerator.PortRange(from_port=443)
    ]
)

# Import the Load Balancers
nlb1 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(self, "NLB1",
    load_balancer_arn="arn:aws:elasticloadbalancing:us-west-2:111111111111:loadbalancer/app/my-load-balancer1/e16bef66805b"
)
nlb2 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(self, "NLB2",
    load_balancer_arn="arn:aws:elasticloadbalancing:ap-south-1:111111111111:loadbalancer/app/my-load-balancer2/5513dc2ea8a1"
)

# Add one EndpointGroup for each Region we are targeting
listener.add_endpoint_group("Group1",
    endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb1)]
)
listener.add_endpoint_group("Group2",
    # Imported load balancers automatically calculate their Region from the ARN.
    # If you are load balancing to other resources, you must also pass a `region`
    # parameter here.
    endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb2)]
)
```

## Concepts

The **Accelerator** construct defines a Global Accelerator resource.

An Accelerator includes one or more **Listeners** that accepts inbound
connections on one or more ports.

Each Listener has one or more **Endpoint Groups**, representing multiple
geographically distributed copies of your application. There is one Endpoint
Group per Region, and user traffic is routed to the closest Region by default.

An Endpoint Group consists of one or more **Endpoints**, which is where the
user traffic coming in on the Listener is ultimately sent. The Endpoint port
used is the same as the traffic came in on at the Listener, unless overridden.

## Types of Endpoints

There are 4 types of Endpoints, and they can be found in the
`@aws-cdk/aws-globalaccelerator-endpoints` package:

* Application Load Balancers
* Network Load Balancers
* EC2 Instances
* Elastic IP Addresses

### Application Load Balancers

```python
# alb: elbv2.ApplicationLoadBalancer
# listener: globalaccelerator.Listener


listener.add_endpoint_group("Group",
    endpoints=[
        ga_endpoints.ApplicationLoadBalancerEndpoint(alb,
            weight=128,
            preserve_client_ip=True
        )
    ]
)
```

### Network Load Balancers

```python
# nlb: elbv2.NetworkLoadBalancer
# listener: globalaccelerator.Listener


listener.add_endpoint_group("Group",
    endpoints=[
        ga_endpoints.NetworkLoadBalancerEndpoint(nlb,
            weight=128
        )
    ]
)
```

### EC2 Instances

```python
# listener: globalaccelerator.Listener
# instance: ec2.Instance


listener.add_endpoint_group("Group",
    endpoints=[
        ga_endpoints.InstanceEndpoint(instance,
            weight=128,
            preserve_client_ip=True
        )
    ]
)
```

### Elastic IP Addresses

```python
# listener: globalaccelerator.Listener
# eip: ec2.CfnEIP


listener.add_endpoint_group("Group",
    endpoints=[
        ga_endpoints.CfnEipEndpoint(eip,
            weight=128
        )
    ]
)
```

## Client IP Address Preservation and Security Groups

When using the `preserveClientIp` feature, AGA creates
**Elastic Network Interfaces** (ENIs) in your AWS account, that are
associated with a Security Group AGA creates for you. You can use the
security group created by AGA as a source group in other security groups
(such as those for EC2 instances or Elastic Load Balancers), if you want to
restrict incoming traffic to the AGA security group rules.

AGA creates a specific security group called `GlobalAccelerator` for each VPC
it has an ENI in (this behavior can not be changed). CloudFormation doesn't
support referencing the security group created by AGA, but this construct
library comes with a custom resource that enables you to reference the AGA
security group.

Call `endpointGroup.connectionsPeer()` to obtain a reference to the Security Group
which you can use in connection rules. You must pass a reference to the VPC in whose
context the security group will be looked up. Example:

```python
# listener: globalaccelerator.Listener

# Non-open ALB
# alb: elbv2.ApplicationLoadBalancer

# Remember that there is only one AGA security group per VPC.
# vpc: ec2.Vpc


endpoint_group = listener.add_endpoint_group("Group",
    endpoints=[
        ga_endpoints.ApplicationLoadBalancerEndpoint(alb,
            preserve_client_ip=True
        )
    ]
)
aga_sg = endpoint_group.connections_peer("GlobalAcceleratorSG", vpc)

# Allow connections from the AGA to the ALB
alb.connections.allow_from(aga_sg, ec2.Port.tcp(443))
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_ec2 import IPeer as _IPeer_cf58db9a, IVpc as _IVpc_f30d5663


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.AcceleratorAttributes",
    jsii_struct_bases=[],
    name_mapping={"accelerator_arn": "acceleratorArn", "dns_name": "dnsName"},
)
class AcceleratorAttributes:
    def __init__(
        self,
        *,
        accelerator_arn: builtins.str,
        dns_name: builtins.str,
    ) -> None:
        '''Attributes required to import an existing accelerator to the stack.

        :param accelerator_arn: The ARN of the accelerator.
        :param dns_name: The DNS name of the accelerator.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_globalaccelerator as globalaccelerator
            
            accelerator_attributes = globalaccelerator.AcceleratorAttributes(
                accelerator_arn="acceleratorArn",
                dns_name="dnsName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "accelerator_arn": accelerator_arn,
            "dns_name": dns_name,
        }

    @builtins.property
    def accelerator_arn(self) -> builtins.str:
        '''The ARN of the accelerator.'''
        result = self._values.get("accelerator_arn")
        assert result is not None, "Required property 'accelerator_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_name(self) -> builtins.str:
        '''The DNS name of the accelerator.'''
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcceleratorAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.AcceleratorProps",
    jsii_struct_bases=[],
    name_mapping={"accelerator_name": "acceleratorName", "enabled": "enabled"},
)
class AcceleratorProps:
    def __init__(
        self,
        *,
        accelerator_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Construct properties of the Accelerator.

        :param accelerator_name: The name of the accelerator. Default: - resource ID
        :param enabled: Indicates whether the accelerator is enabled. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_globalaccelerator as globalaccelerator
            
            accelerator_props = globalaccelerator.AcceleratorProps(
                accelerator_name="acceleratorName",
                enabled=False
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerator_name is not None:
            self._values["accelerator_name"] = accelerator_name
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def accelerator_name(self) -> typing.Optional[builtins.str]:
        '''The name of the accelerator.

        :default: - resource ID
        '''
        result = self._values.get("accelerator_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether the accelerator is enabled.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcceleratorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAccelerator(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnAccelerator",
):
    '''A CloudFormation ``AWS::GlobalAccelerator::Accelerator``.

    The ``AWS::GlobalAccelerator::Accelerator`` resource is a Global Accelerator resource type that contains information about how you create an accelerator. An accelerator includes one or more listeners that process inbound connections and direct traffic to one or more endpoint groups, each of which includes endpoints, such as Application Load Balancers, Network Load Balancers, and Amazon EC2 instances.

    :cloudformationResource: AWS::GlobalAccelerator::Accelerator
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_globalaccelerator as globalaccelerator
        
        cfn_accelerator = globalaccelerator.CfnAccelerator(self, "MyCfnAccelerator",
            name="name",
        
            # the properties below are optional
            enabled=False,
            ip_addresses=["ipAddresses"],
            ip_address_type="ipAddressType",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::GlobalAccelerator::Accelerator``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.
        :param enabled: Indicates whether the accelerator is enabled. The value is true or false. The default value is true. If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.
        :param ip_addresses: Optionally, if you've added your own IP address pool to Global Accelerator (BYOIP), you can choose IP addresses from your own pool to use for the accelerator's static IP addresses when you create an accelerator. You can specify one or two addresses, separated by a comma. Do not include the /32 suffix. Only one IP address from each of your IP address ranges can be used for each accelerator. If you specify only one IP address from your IP address range, Global Accelerator assigns a second static IP address for the accelerator from the AWS IP address pool. Note that you can't update IP addresses for an existing accelerator. To change them, you must create a new accelerator with the new addresses. For more information, see `Bring Your Own IP Addresses (BYOIP) <https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html>`_ in the *AWS Global Accelerator Developer Guide* .
        :param ip_address_type: The value for the address type must be IPv4.
        :param tags: Create tags for an accelerator. For more information, see `Tagging <https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html>`_ in the *AWS Global Accelerator Developer Guide* .
        '''
        props = CfnAcceleratorProps(
            name=name,
            enabled=enabled,
            ip_addresses=ip_addresses,
            ip_address_type=ip_address_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAcceleratorArn")
    def attr_accelerator_arn(self) -> builtins.str:
        '''The ARN of the accelerator, such as ``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`` .

        :cloudformationAttribute: AcceleratorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAcceleratorArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDnsName")
    def attr_dns_name(self) -> builtins.str:
        '''The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IP addresses.

        :cloudformationAttribute: DnsName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDnsName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIpv4Addresses")
    def attr_ipv4_addresses(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: Ipv4Addresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrIpv4Addresses"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Create tags for an accelerator.

        For more information, see `Tagging <https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html>`_ in the *AWS Global Accelerator Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the accelerator.

        The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the accelerator is enabled. The value is true or false. The default value is true.

        If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optionally, if you've added your own IP address pool to Global Accelerator (BYOIP), you can choose IP addresses from your own pool to use for the accelerator's static IP addresses when you create an accelerator.

        You can specify one or two addresses, separated by a comma. Do not include the /32 suffix.

        Only one IP address from each of your IP address ranges can be used for each accelerator. If you specify only one IP address from your IP address range, Global Accelerator assigns a second static IP address for the accelerator from the AWS IP address pool.

        Note that you can't update IP addresses for an existing accelerator. To change them, you must create a new accelerator with the new addresses.

        For more information, see `Bring Your Own IP Addresses (BYOIP) <https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html>`_ in the *AWS Global Accelerator Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-ipaddresses
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipAddresses"))

    @ip_addresses.setter
    def ip_addresses(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "ipAddresses", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''The value for the address type must be IPv4.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-ipaddresstype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ipAddressType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnAcceleratorProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "enabled": "enabled",
        "ip_addresses": "ipAddresses",
        "ip_address_type": "ipAddressType",
        "tags": "tags",
    },
)
class CfnAcceleratorProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccelerator``.

        :param name: The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.
        :param enabled: Indicates whether the accelerator is enabled. The value is true or false. The default value is true. If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.
        :param ip_addresses: Optionally, if you've added your own IP address pool to Global Accelerator (BYOIP), you can choose IP addresses from your own pool to use for the accelerator's static IP addresses when you create an accelerator. You can specify one or two addresses, separated by a comma. Do not include the /32 suffix. Only one IP address from each of your IP address ranges can be used for each accelerator. If you specify only one IP address from your IP address range, Global Accelerator assigns a second static IP address for the accelerator from the AWS IP address pool. Note that you can't update IP addresses for an existing accelerator. To change them, you must create a new accelerator with the new addresses. For more information, see `Bring Your Own IP Addresses (BYOIP) <https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html>`_ in the *AWS Global Accelerator Developer Guide* .
        :param ip_address_type: The value for the address type must be IPv4.
        :param tags: Create tags for an accelerator. For more information, see `Tagging <https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html>`_ in the *AWS Global Accelerator Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_globalaccelerator as globalaccelerator
            
            cfn_accelerator_props = globalaccelerator.CfnAcceleratorProps(
                name="name",
            
                # the properties below are optional
                enabled=False,
                ip_addresses=["ipAddresses"],
                ip_address_type="ipAddressType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if ip_addresses is not None:
            self._values["ip_addresses"] = ip_addresses
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the accelerator.

        The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the accelerator is enabled. The value is true or false. The default value is true.

        If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optionally, if you've added your own IP address pool to Global Accelerator (BYOIP), you can choose IP addresses from your own pool to use for the accelerator's static IP addresses when you create an accelerator.

        You can specify one or two addresses, separated by a comma. Do not include the /32 suffix.

        Only one IP address from each of your IP address ranges can be used for each accelerator. If you specify only one IP address from your IP address range, Global Accelerator assigns a second static IP address for the accelerator from the AWS IP address pool.

        Note that you can't update IP addresses for an existing accelerator. To change them, you must create a new accelerator with the new addresses.

        For more information, see `Bring Your Own IP Addresses (BYOIP) <https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html>`_ in the *AWS Global Accelerator Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-ipaddresses
        '''
        result = self._values.get("ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''The value for the address type must be IPv4.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-ipaddresstype
        '''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Create tags for an accelerator.

        For more information, see `Tagging <https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html>`_ in the *AWS Global Accelerator Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAcceleratorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEndpointGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnEndpointGroup",
):
    '''A CloudFormation ``AWS::GlobalAccelerator::EndpointGroup``.

    The ``AWS::GlobalAccelerator::EndpointGroup`` resource is a Global Accelerator resource type that contains information about how you create an endpoint group for the specified listener. An endpoint group is a collection of endpoints in one AWS Region .

    :cloudformationResource: AWS::GlobalAccelerator::EndpointGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_globalaccelerator as globalaccelerator
        
        cfn_endpoint_group = globalaccelerator.CfnEndpointGroup(self, "MyCfnEndpointGroup",
            endpoint_group_region="endpointGroupRegion",
            listener_arn="listenerArn",
        
            # the properties below are optional
            endpoint_configurations=[globalaccelerator.CfnEndpointGroup.EndpointConfigurationProperty(
                endpoint_id="endpointId",
        
                # the properties below are optional
                client_ip_preservation_enabled=False,
                weight=123
            )],
            health_check_interval_seconds=123,
            health_check_path="healthCheckPath",
            health_check_port=123,
            health_check_protocol="healthCheckProtocol",
            port_overrides=[globalaccelerator.CfnEndpointGroup.PortOverrideProperty(
                endpoint_port=123,
                listener_port=123
            )],
            threshold_count=123,
            traffic_dial_percentage=123
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        endpoint_group_region: builtins.str,
        listener_arn: builtins.str,
        endpoint_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnEndpointGroup.EndpointConfigurationProperty", _IResolvable_da3f097b]]]] = None,
        health_check_interval_seconds: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional[builtins.str] = None,
        port_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnEndpointGroup.PortOverrideProperty", _IResolvable_da3f097b]]]] = None,
        threshold_count: typing.Optional[jsii.Number] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::GlobalAccelerator::EndpointGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param endpoint_group_region: The AWS Regions where the endpoint group is located.
        :param listener_arn: The Amazon Resource Name (ARN) of the listener.
        :param endpoint_configurations: The list of endpoint objects.
        :param health_check_interval_seconds: The time—10 seconds or 30 seconds—between health checks for each endpoint. The default value is 30.
        :param health_check_path: If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).
        :param health_check_port: The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.
        :param health_check_protocol: The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.
        :param port_overrides: Allows you to override the destination ports used to route traffic to an endpoint. Using a port override lets you to map a list of external destination ports (that your users send traffic to) to a list of internal destination ports that you want an application endpoint to receive traffic on.
        :param threshold_count: The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
        :param traffic_dial_percentage: The percentage of traffic to send to an AWS Regions . Additional traffic is distributed to other endpoint groups for this listener. Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. The default value is 100.
        '''
        props = CfnEndpointGroupProps(
            endpoint_group_region=endpoint_group_region,
            listener_arn=listener_arn,
            endpoint_configurations=endpoint_configurations,
            health_check_interval_seconds=health_check_interval_seconds,
            health_check_path=health_check_path,
            health_check_port=health_check_port,
            health_check_protocol=health_check_protocol,
            port_overrides=port_overrides,
            threshold_count=threshold_count,
            traffic_dial_percentage=traffic_dial_percentage,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEndpointGroupArn")
    def attr_endpoint_group_arn(self) -> builtins.str:
        '''The ARN of the endpoint group, such as ``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/098765zyxwvu`` .

        :cloudformationAttribute: EndpointGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointGroupRegion")
    def endpoint_group_region(self) -> builtins.str:
        '''The AWS Regions where the endpoint group is located.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-endpointgroupregion
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointGroupRegion"))

    @endpoint_group_region.setter
    def endpoint_group_region(self, value: builtins.str) -> None:
        jsii.set(self, "endpointGroupRegion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listenerArn")
    def listener_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the listener.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-listenerarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "listenerArn"))

    @listener_arn.setter
    def listener_arn(self, value: builtins.str) -> None:
        jsii.set(self, "listenerArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointConfigurations")
    def endpoint_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.EndpointConfigurationProperty", _IResolvable_da3f097b]]]]:
        '''The list of endpoint objects.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-endpointconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.EndpointConfigurationProperty", _IResolvable_da3f097b]]]], jsii.get(self, "endpointConfigurations"))

    @endpoint_configurations.setter
    def endpoint_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.EndpointConfigurationProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "endpointConfigurations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckIntervalSeconds")
    def health_check_interval_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time—10 seconds or 30 seconds—between health checks for each endpoint.

        The default value is 30.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckintervalseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckIntervalSeconds"))

    @health_check_interval_seconds.setter
    def health_check_interval_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        jsii.set(self, "healthCheckIntervalSeconds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckPath")
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks.

        The default is slash (/).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckpath
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckPath"))

    @health_check_path.setter
    def health_check_path(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "healthCheckPath", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckPort")
    def health_check_port(self) -> typing.Optional[jsii.Number]:
        '''The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group.

        The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckport
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckPort"))

    @health_check_port.setter
    def health_check_port(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "healthCheckPort", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckProtocol")
    def health_check_protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group.

        The default value is TCP.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckprotocol
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckProtocol"))

    @health_check_protocol.setter
    def health_check_protocol(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "healthCheckProtocol", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portOverrides")
    def port_overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.PortOverrideProperty", _IResolvable_da3f097b]]]]:
        '''Allows you to override the destination ports used to route traffic to an endpoint.

        Using a port override lets you to map a list of external destination ports (that your users send traffic to) to a list of internal destination ports that you want an application endpoint to receive traffic on.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-portoverrides
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.PortOverrideProperty", _IResolvable_da3f097b]]]], jsii.get(self, "portOverrides"))

    @port_overrides.setter
    def port_overrides(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnEndpointGroup.PortOverrideProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "portOverrides", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="thresholdCount")
    def threshold_count(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy.

        The default value is 3.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-thresholdcount
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdCount"))

    @threshold_count.setter
    def threshold_count(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "thresholdCount", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trafficDialPercentage")
    def traffic_dial_percentage(self) -> typing.Optional[jsii.Number]:
        '''The percentage of traffic to send to an AWS Regions .

        Additional traffic is distributed to other endpoint groups for this listener.

        Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.

        The default value is 100.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-trafficdialpercentage
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "trafficDialPercentage"))

    @traffic_dial_percentage.setter
    def traffic_dial_percentage(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "trafficDialPercentage", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnEndpointGroup.EndpointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_id": "endpointId",
            "client_ip_preservation_enabled": "clientIpPreservationEnabled",
            "weight": "weight",
        },
    )
    class EndpointConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint_id: builtins.str,
            client_ip_preservation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A complex type for endpoints.

            A resource must be valid and active when you add it as an endpoint.

            :param endpoint_id: An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For Amazon EC2 instances, this is the EC2 instance ID. A resource must be valid and active when you add it as an endpoint. An Application Load Balancer can be either internal or internet-facing.
            :param client_ip_preservation_enabled: Indicates whether client IP address preservation is enabled for an Application Load Balancer endpoint. The value is true or false. The default value is true for new accelerators. If the value is set to true, the client's IP address is preserved in the ``X-Forwarded-For`` request header as traffic travels to applications on the Application Load Balancer endpoint fronted by the accelerator. For more information, see `Preserve Client IP Addresses <https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.html>`_ in the *AWS Global Accelerator Developer Guide* .
            :param weight: The weight associated with the endpoint. When you add weights to endpoints, you configure Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see `Endpoint Weights <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`_ in the *AWS Global Accelerator Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_globalaccelerator as globalaccelerator
                
                endpoint_configuration_property = globalaccelerator.CfnEndpointGroup.EndpointConfigurationProperty(
                    endpoint_id="endpointId",
                
                    # the properties below are optional
                    client_ip_preservation_enabled=False,
                    weight=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_id": endpoint_id,
            }
            if client_ip_preservation_enabled is not None:
                self._values["client_ip_preservation_enabled"] = client_ip_preservation_enabled
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def endpoint_id(self) -> builtins.str:
            '''An ID for the endpoint.

            If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For Amazon EC2 instances, this is the EC2 instance ID. A resource must be valid and active when you add it as an endpoint.

            An Application Load Balancer can be either internal or internet-facing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html#cfn-globalaccelerator-endpointgroup-endpointconfiguration-endpointid
            '''
            result = self._values.get("endpoint_id")
            assert result is not None, "Required property 'endpoint_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_ip_preservation_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether client IP address preservation is enabled for an Application Load Balancer endpoint.

            The value is true or false. The default value is true for new accelerators.

            If the value is set to true, the client's IP address is preserved in the ``X-Forwarded-For`` request header as traffic travels to applications on the Application Load Balancer endpoint fronted by the accelerator.

            For more information, see `Preserve Client IP Addresses <https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.html>`_ in the *AWS Global Accelerator Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html#cfn-globalaccelerator-endpointgroup-endpointconfiguration-clientippreservationenabled
            '''
            result = self._values.get("client_ip_preservation_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''The weight associated with the endpoint.

            When you add weights to endpoints, you configure Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see `Endpoint Weights <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`_ in the *AWS Global Accelerator Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html#cfn-globalaccelerator-endpointgroup-endpointconfiguration-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnEndpointGroup.PortOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_port": "endpointPort",
            "listener_port": "listenerPort",
        },
    )
    class PortOverrideProperty:
        def __init__(
            self,
            *,
            endpoint_port: jsii.Number,
            listener_port: jsii.Number,
        ) -> None:
            '''Override specific listener ports used to route traffic to endpoints that are part of an endpoint group.

            For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.

            For more information, see `Port overrides <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html>`_ in the *AWS Global Accelerator Developer Guide* .

            :param endpoint_port: The endpoint port that you want a listener port to be mapped to. This is the port on the endpoint, such as the Application Load Balancer or Amazon EC2 instance.
            :param listener_port: The listener port that you want to map to a specific endpoint port. This is the port that user traffic arrives to the Global Accelerator on.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_globalaccelerator as globalaccelerator
                
                port_override_property = globalaccelerator.CfnEndpointGroup.PortOverrideProperty(
                    endpoint_port=123,
                    listener_port=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_port": endpoint_port,
                "listener_port": listener_port,
            }

        @builtins.property
        def endpoint_port(self) -> jsii.Number:
            '''The endpoint port that you want a listener port to be mapped to.

            This is the port on the endpoint, such as the Application Load Balancer or Amazon EC2 instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html#cfn-globalaccelerator-endpointgroup-portoverride-endpointport
            '''
            result = self._values.get("endpoint_port")
            assert result is not None, "Required property 'endpoint_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def listener_port(self) -> jsii.Number:
            '''The listener port that you want to map to a specific endpoint port.

            This is the port that user traffic arrives to the Global Accelerator on.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html#cfn-globalaccelerator-endpointgroup-portoverride-listenerport
            '''
            result = self._values.get("listener_port")
            assert result is not None, "Required property 'listener_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnEndpointGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_group_region": "endpointGroupRegion",
        "listener_arn": "listenerArn",
        "endpoint_configurations": "endpointConfigurations",
        "health_check_interval_seconds": "healthCheckIntervalSeconds",
        "health_check_path": "healthCheckPath",
        "health_check_port": "healthCheckPort",
        "health_check_protocol": "healthCheckProtocol",
        "port_overrides": "portOverrides",
        "threshold_count": "thresholdCount",
        "traffic_dial_percentage": "trafficDialPercentage",
    },
)
class CfnEndpointGroupProps:
    def __init__(
        self,
        *,
        endpoint_group_region: builtins.str,
        listener_arn: builtins.str,
        endpoint_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnEndpointGroup.EndpointConfigurationProperty, _IResolvable_da3f097b]]]] = None,
        health_check_interval_seconds: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional[builtins.str] = None,
        port_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnEndpointGroup.PortOverrideProperty, _IResolvable_da3f097b]]]] = None,
        threshold_count: typing.Optional[jsii.Number] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnEndpointGroup``.

        :param endpoint_group_region: The AWS Regions where the endpoint group is located.
        :param listener_arn: The Amazon Resource Name (ARN) of the listener.
        :param endpoint_configurations: The list of endpoint objects.
        :param health_check_interval_seconds: The time—10 seconds or 30 seconds—between health checks for each endpoint. The default value is 30.
        :param health_check_path: If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).
        :param health_check_port: The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.
        :param health_check_protocol: The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.
        :param port_overrides: Allows you to override the destination ports used to route traffic to an endpoint. Using a port override lets you to map a list of external destination ports (that your users send traffic to) to a list of internal destination ports that you want an application endpoint to receive traffic on.
        :param threshold_count: The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
        :param traffic_dial_percentage: The percentage of traffic to send to an AWS Regions . Additional traffic is distributed to other endpoint groups for this listener. Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. The default value is 100.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_globalaccelerator as globalaccelerator
            
            cfn_endpoint_group_props = globalaccelerator.CfnEndpointGroupProps(
                endpoint_group_region="endpointGroupRegion",
                listener_arn="listenerArn",
            
                # the properties below are optional
                endpoint_configurations=[globalaccelerator.CfnEndpointGroup.EndpointConfigurationProperty(
                    endpoint_id="endpointId",
            
                    # the properties below are optional
                    client_ip_preservation_enabled=False,
                    weight=123
                )],
                health_check_interval_seconds=123,
                health_check_path="healthCheckPath",
                health_check_port=123,
                health_check_protocol="healthCheckProtocol",
                port_overrides=[globalaccelerator.CfnEndpointGroup.PortOverrideProperty(
                    endpoint_port=123,
                    listener_port=123
                )],
                threshold_count=123,
                traffic_dial_percentage=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_group_region": endpoint_group_region,
            "listener_arn": listener_arn,
        }
        if endpoint_configurations is not None:
            self._values["endpoint_configurations"] = endpoint_configurations
        if health_check_interval_seconds is not None:
            self._values["health_check_interval_seconds"] = health_check_interval_seconds
        if health_check_path is not None:
            self._values["health_check_path"] = health_check_path
        if health_check_port is not None:
            self._values["health_check_port"] = health_check_port
        if health_check_protocol is not None:
            self._values["health_check_protocol"] = health_check_protocol
        if port_overrides is not None:
            self._values["port_overrides"] = port_overrides
        if threshold_count is not None:
            self._values["threshold_count"] = threshold_count
        if traffic_dial_percentage is not None:
            self._values["traffic_dial_percentage"] = traffic_dial_percentage

    @builtins.property
    def endpoint_group_region(self) -> builtins.str:
        '''The AWS Regions where the endpoint group is located.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-endpointgroupregion
        '''
        result = self._values.get("endpoint_group_region")
        assert result is not None, "Required property 'endpoint_group_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def listener_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the listener.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-listenerarn
        '''
        result = self._values.get("listener_arn")
        assert result is not None, "Required property 'listener_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnEndpointGroup.EndpointConfigurationProperty, _IResolvable_da3f097b]]]]:
        '''The list of endpoint objects.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-endpointconfigurations
        '''
        result = self._values.get("endpoint_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnEndpointGroup.EndpointConfigurationProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def health_check_interval_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time—10 seconds or 30 seconds—between health checks for each endpoint.

        The default value is 30.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckintervalseconds
        '''
        result = self._values.get("health_check_interval_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks.

        The default is slash (/).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckpath
        '''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_port(self) -> typing.Optional[jsii.Number]:
        '''The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group.

        The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckport
        '''
        result = self._values.get("health_check_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group.

        The default value is TCP.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckprotocol
        '''
        result = self._values.get("health_check_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnEndpointGroup.PortOverrideProperty, _IResolvable_da3f097b]]]]:
        '''Allows you to override the destination ports used to route traffic to an endpoint.

        Using a port override lets you to map a list of external destination ports (that your users send traffic to) to a list of internal destination ports that you want an application endpoint to receive traffic on.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-portoverrides
        '''
        result = self._values.get("port_overrides")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnEndpointGroup.PortOverrideProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def threshold_count(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy.

        The default value is 3.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-thresholdcount
        '''
        result = self._values.get("threshold_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def traffic_dial_percentage(self) -> typing.Optional[jsii.Number]:
        '''The percentage of traffic to send to an AWS Regions .

        Additional traffic is distributed to other endpoint groups for this listener.

        Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.

        The default value is 100.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-trafficdialpercentage
        '''
        result = self._values.get("traffic_dial_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnListener(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnListener",
):
    '''A CloudFormation ``AWS::GlobalAccelerator::Listener``.

    The ``AWS::GlobalAccelerator::Listener`` resource is a Global Accelerator resource type that contains information about how you create a listener to process inbound connections from clients to an accelerator. Connections arrive to assigned static IP addresses on a port, port range, or list of port ranges that you specify.

    :cloudformationResource: AWS::GlobalAccelerator::Listener
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_globalaccelerator as globalaccelerator
        
        cfn_listener = globalaccelerator.CfnListener(self, "MyCfnListener",
            accelerator_arn="acceleratorArn",
            port_ranges=[globalaccelerator.CfnListener.PortRangeProperty(
                from_port=123,
                to_port=123
            )],
            protocol="protocol",
        
            # the properties below are optional
            client_affinity="clientAffinity"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accelerator_arn: builtins.str,
        port_ranges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnListener.PortRangeProperty", _IResolvable_da3f097b]]],
        protocol: builtins.str,
        client_affinity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::GlobalAccelerator::Listener``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param accelerator_arn: The Amazon Resource Name (ARN) of your accelerator.
        :param port_ranges: The list of port ranges for the connections from clients to the accelerator.
        :param protocol: The protocol for the connections from clients to the accelerator.
        :param client_affinity: Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Client affinity gives you control over whether to always route each client to the same specific endpoint. AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes. If you want a given client to always be routed to the same endpoint, set client affinity to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value. The default value is ``NONE`` .
        '''
        props = CfnListenerProps(
            accelerator_arn=accelerator_arn,
            port_ranges=port_ranges,
            protocol=protocol,
            client_affinity=client_affinity,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrListenerArn")
    def attr_listener_arn(self) -> builtins.str:
        '''The ARN of the listener, such as ``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz`` .

        :cloudformationAttribute: ListenerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrListenerArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceleratorArn")
    def accelerator_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of your accelerator.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-acceleratorarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "acceleratorArn"))

    @accelerator_arn.setter
    def accelerator_arn(self, value: builtins.str) -> None:
        jsii.set(self, "acceleratorArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="portRanges")
    def port_ranges(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnListener.PortRangeProperty", _IResolvable_da3f097b]]]:
        '''The list of port ranges for the connections from clients to the accelerator.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-portranges
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnListener.PortRangeProperty", _IResolvable_da3f097b]]], jsii.get(self, "portRanges"))

    @port_ranges.setter
    def port_ranges(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnListener.PortRangeProperty", _IResolvable_da3f097b]]],
    ) -> None:
        jsii.set(self, "portRanges", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        '''The protocol for the connections from clients to the accelerator.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-protocol
        '''
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        jsii.set(self, "protocol", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clientAffinity")
    def client_affinity(self) -> typing.Optional[builtins.str]:
        '''Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request.

        Client affinity gives you control over whether to always route each client to the same specific endpoint.

        AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.

        If you want a given client to always be routed to the same endpoint, set client affinity to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.

        The default value is ``NONE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-clientaffinity
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientAffinity"))

    @client_affinity.setter
    def client_affinity(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "clientAffinity", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnListener.PortRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"from_port": "fromPort", "to_port": "toPort"},
    )
    class PortRangeProperty:
        def __init__(self, *, from_port: jsii.Number, to_port: jsii.Number) -> None:
            '''A complex type for a range of ports for a listener.

            :param from_port: The first port in the range of ports, inclusive.
            :param to_port: The last port in the range of ports, inclusive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_globalaccelerator as globalaccelerator
                
                port_range_property = globalaccelerator.CfnListener.PortRangeProperty(
                    from_port=123,
                    to_port=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "from_port": from_port,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''The first port in the range of ports, inclusive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html#cfn-globalaccelerator-listener-portrange-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''The last port in the range of ports, inclusive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html#cfn-globalaccelerator-listener-portrange-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.CfnListenerProps",
    jsii_struct_bases=[],
    name_mapping={
        "accelerator_arn": "acceleratorArn",
        "port_ranges": "portRanges",
        "protocol": "protocol",
        "client_affinity": "clientAffinity",
    },
)
class CfnListenerProps:
    def __init__(
        self,
        *,
        accelerator_arn: builtins.str,
        port_ranges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnListener.PortRangeProperty, _IResolvable_da3f097b]]],
        protocol: builtins.str,
        client_affinity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnListener``.

        :param accelerator_arn: The Amazon Resource Name (ARN) of your accelerator.
        :param port_ranges: The list of port ranges for the connections from clients to the accelerator.
        :param protocol: The protocol for the connections from clients to the accelerator.
        :param client_affinity: Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Client affinity gives you control over whether to always route each client to the same specific endpoint. AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes. If you want a given client to always be routed to the same endpoint, set client affinity to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value. The default value is ``NONE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_globalaccelerator as globalaccelerator
            
            cfn_listener_props = globalaccelerator.CfnListenerProps(
                accelerator_arn="acceleratorArn",
                port_ranges=[globalaccelerator.CfnListener.PortRangeProperty(
                    from_port=123,
                    to_port=123
                )],
                protocol="protocol",
            
                # the properties below are optional
                client_affinity="clientAffinity"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "accelerator_arn": accelerator_arn,
            "port_ranges": port_ranges,
            "protocol": protocol,
        }
        if client_affinity is not None:
            self._values["client_affinity"] = client_affinity

    @builtins.property
    def accelerator_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of your accelerator.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-acceleratorarn
        '''
        result = self._values.get("accelerator_arn")
        assert result is not None, "Required property 'accelerator_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port_ranges(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnListener.PortRangeProperty, _IResolvable_da3f097b]]]:
        '''The list of port ranges for the connections from clients to the accelerator.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-portranges
        '''
        result = self._values.get("port_ranges")
        assert result is not None, "Required property 'port_ranges' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnListener.PortRangeProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''The protocol for the connections from clients to the accelerator.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_affinity(self) -> typing.Optional[builtins.str]:
        '''Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request.

        Client affinity gives you control over whether to always route each client to the same specific endpoint.

        AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.

        If you want a given client to always be routed to the same endpoint, set client affinity to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.

        The default value is ``NONE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-clientaffinity
        '''
        result = self._values.get("client_affinity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnListenerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_globalaccelerator.ClientAffinity")
class ClientAffinity(enum.Enum):
    '''Client affinity gives you control over whether to always route each client to the same specific endpoint.

    :see: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.html#about-listeners-client-affinity
    '''

    NONE = "NONE"
    '''Route traffic based on the 5-tuple ``(source IP, source port, destination IP, destination port, protocol)``.'''
    SOURCE_IP = "SOURCE_IP"
    '''Route traffic based on the 2-tuple ``(source IP, destination IP)``.

    The result is that multiple connections from the same client will be routed the same.
    '''


@jsii.enum(jsii_type="aws-cdk-lib.aws_globalaccelerator.ConnectionProtocol")
class ConnectionProtocol(enum.Enum):
    '''The protocol for the connections from clients to the accelerator.'''

    TCP = "TCP"
    '''TCP.'''
    UDP = "UDP"
    '''UDP.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.EndpointGroupOptions",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_group_name": "endpointGroupName",
        "endpoints": "endpoints",
        "health_check_interval": "healthCheckInterval",
        "health_check_path": "healthCheckPath",
        "health_check_port": "healthCheckPort",
        "health_check_protocol": "healthCheckProtocol",
        "health_check_threshold": "healthCheckThreshold",
        "port_overrides": "portOverrides",
        "region": "region",
        "traffic_dial_percentage": "trafficDialPercentage",
    },
)
class EndpointGroupOptions:
    def __init__(
        self,
        *,
        endpoint_group_name: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Sequence["IEndpoint"]] = None,
        health_check_interval: typing.Optional[_Duration_4839e8c3] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional["HealthCheckProtocol"] = None,
        health_check_threshold: typing.Optional[jsii.Number] = None,
        port_overrides: typing.Optional[typing.Sequence["PortOverride"]] = None,
        region: typing.Optional[builtins.str] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Basic options for creating a new EndpointGroup.

        :param endpoint_group_name: Name of the endpoint group. Default: - logical ID of the resource
        :param endpoints: Initial list of endpoints for this group. Default: - Group is initially empty
        :param health_check_interval: The time between health checks for each endpoint. Must be either 10 or 30 seconds. Default: Duration.seconds(30)
        :param health_check_path: The ping path for health checks (if the protocol is HTTP(S)). Default: '/'
        :param health_check_port: The port used to perform health checks. Default: - The listener's port
        :param health_check_protocol: The protocol used to perform health checks. Default: HealthCheckProtocol.TCP
        :param health_check_threshold: The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. Default: 3
        :param port_overrides: Override the destination ports used to route traffic to an endpoint. Unless overridden, the port used to hit the endpoint will be the same as the port that traffic arrives on at the listener. Default: - No overrides
        :param region: The AWS Region where the endpoint group is located. Default: - region of the first endpoint in this group, or the stack region if that region can't be determined
        :param traffic_dial_percentage: The percentage of traffic to send to this AWS Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. Additional traffic is distributed to other endpoint groups for this listener. Default: 100

        :exampleMetadata: infused

        Example::

            # alb: elbv2.ApplicationLoadBalancer
            # listener: globalaccelerator.Listener
            
            
            listener.add_endpoint_group("Group",
                endpoints=[
                    ga_endpoints.ApplicationLoadBalancerEndpoint(alb,
                        weight=128,
                        preserve_client_ip=True
                    )
                ]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if endpoint_group_name is not None:
            self._values["endpoint_group_name"] = endpoint_group_name
        if endpoints is not None:
            self._values["endpoints"] = endpoints
        if health_check_interval is not None:
            self._values["health_check_interval"] = health_check_interval
        if health_check_path is not None:
            self._values["health_check_path"] = health_check_path
        if health_check_port is not None:
            self._values["health_check_port"] = health_check_port
        if health_check_protocol is not None:
            self._values["health_check_protocol"] = health_check_protocol
        if health_check_threshold is not None:
            self._values["health_check_threshold"] = health_check_threshold
        if port_overrides is not None:
            self._values["port_overrides"] = port_overrides
        if region is not None:
            self._values["region"] = region
        if traffic_dial_percentage is not None:
            self._values["traffic_dial_percentage"] = traffic_dial_percentage

    @builtins.property
    def endpoint_group_name(self) -> typing.Optional[builtins.str]:
        '''Name of the endpoint group.

        :default: - logical ID of the resource
        '''
        result = self._values.get("endpoint_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoints(self) -> typing.Optional[typing.List["IEndpoint"]]:
        '''Initial list of endpoints for this group.

        :default: - Group is initially empty
        '''
        result = self._values.get("endpoints")
        return typing.cast(typing.Optional[typing.List["IEndpoint"]], result)

    @builtins.property
    def health_check_interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The time between health checks for each endpoint.

        Must be either 10 or 30 seconds.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("health_check_interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''The ping path for health checks (if the protocol is HTTP(S)).

        :default: '/'
        '''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_port(self) -> typing.Optional[jsii.Number]:
        '''The port used to perform health checks.

        :default: - The listener's port
        '''
        result = self._values.get("health_check_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_protocol(self) -> typing.Optional["HealthCheckProtocol"]:
        '''The protocol used to perform health checks.

        :default: HealthCheckProtocol.TCP
        '''
        result = self._values.get("health_check_protocol")
        return typing.cast(typing.Optional["HealthCheckProtocol"], result)

    @builtins.property
    def health_check_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy.

        :default: 3
        '''
        result = self._values.get("health_check_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_overrides(self) -> typing.Optional[typing.List["PortOverride"]]:
        '''Override the destination ports used to route traffic to an endpoint.

        Unless overridden, the port used to hit the endpoint will be the same as the port
        that traffic arrives on at the listener.

        :default: - No overrides
        '''
        result = self._values.get("port_overrides")
        return typing.cast(typing.Optional[typing.List["PortOverride"]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region where the endpoint group is located.

        :default: - region of the first endpoint in this group, or the stack region if that region can't be determined
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def traffic_dial_percentage(self) -> typing.Optional[jsii.Number]:
        '''The percentage of traffic to send to this AWS Region.

        The percentage is applied to the traffic that would otherwise have been
        routed to the Region based on optimal routing. Additional traffic is
        distributed to other endpoint groups for this listener.

        :default: 100
        '''
        result = self._values.get("traffic_dial_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointGroupOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.EndpointGroupProps",
    jsii_struct_bases=[EndpointGroupOptions],
    name_mapping={
        "endpoint_group_name": "endpointGroupName",
        "endpoints": "endpoints",
        "health_check_interval": "healthCheckInterval",
        "health_check_path": "healthCheckPath",
        "health_check_port": "healthCheckPort",
        "health_check_protocol": "healthCheckProtocol",
        "health_check_threshold": "healthCheckThreshold",
        "port_overrides": "portOverrides",
        "region": "region",
        "traffic_dial_percentage": "trafficDialPercentage",
        "listener": "listener",
    },
)
class EndpointGroupProps(EndpointGroupOptions):
    def __init__(
        self,
        *,
        endpoint_group_name: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Sequence["IEndpoint"]] = None,
        health_check_interval: typing.Optional[_Duration_4839e8c3] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional["HealthCheckProtocol"] = None,
        health_check_threshold: typing.Optional[jsii.Number] = None,
        port_overrides: typing.Optional[typing.Sequence["PortOverride"]] = None,
        region: typing.Optional[builtins.str] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
        listener: "IListener",
    ) -> None:
        '''Property of the EndpointGroup.

        :param endpoint_group_name: Name of the endpoint group. Default: - logical ID of the resource
        :param endpoints: Initial list of endpoints for this group. Default: - Group is initially empty
        :param health_check_interval: The time between health checks for each endpoint. Must be either 10 or 30 seconds. Default: Duration.seconds(30)
        :param health_check_path: The ping path for health checks (if the protocol is HTTP(S)). Default: '/'
        :param health_check_port: The port used to perform health checks. Default: - The listener's port
        :param health_check_protocol: The protocol used to perform health checks. Default: HealthCheckProtocol.TCP
        :param health_check_threshold: The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. Default: 3
        :param port_overrides: Override the destination ports used to route traffic to an endpoint. Unless overridden, the port used to hit the endpoint will be the same as the port that traffic arrives on at the listener. Default: - No overrides
        :param region: The AWS Region where the endpoint group is located. Default: - region of the first endpoint in this group, or the stack region if that region can't be determined
        :param traffic_dial_percentage: The percentage of traffic to send to this AWS Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. Additional traffic is distributed to other endpoint groups for this listener. Default: 100
        :param listener: The Amazon Resource Name (ARN) of the listener.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_globalaccelerator as globalaccelerator
            
            # endpoint: globalaccelerator.IEndpoint
            # listener: globalaccelerator.Listener
            
            endpoint_group_props = globalaccelerator.EndpointGroupProps(
                listener=listener,
            
                # the properties below are optional
                endpoint_group_name="endpointGroupName",
                endpoints=[endpoint],
                health_check_interval=cdk.Duration.minutes(30),
                health_check_path="healthCheckPath",
                health_check_port=123,
                health_check_protocol=globalaccelerator.HealthCheckProtocol.TCP,
                health_check_threshold=123,
                port_overrides=[globalaccelerator.PortOverride(
                    endpoint_port=123,
                    listener_port=123
                )],
                region="region",
                traffic_dial_percentage=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "listener": listener,
        }
        if endpoint_group_name is not None:
            self._values["endpoint_group_name"] = endpoint_group_name
        if endpoints is not None:
            self._values["endpoints"] = endpoints
        if health_check_interval is not None:
            self._values["health_check_interval"] = health_check_interval
        if health_check_path is not None:
            self._values["health_check_path"] = health_check_path
        if health_check_port is not None:
            self._values["health_check_port"] = health_check_port
        if health_check_protocol is not None:
            self._values["health_check_protocol"] = health_check_protocol
        if health_check_threshold is not None:
            self._values["health_check_threshold"] = health_check_threshold
        if port_overrides is not None:
            self._values["port_overrides"] = port_overrides
        if region is not None:
            self._values["region"] = region
        if traffic_dial_percentage is not None:
            self._values["traffic_dial_percentage"] = traffic_dial_percentage

    @builtins.property
    def endpoint_group_name(self) -> typing.Optional[builtins.str]:
        '''Name of the endpoint group.

        :default: - logical ID of the resource
        '''
        result = self._values.get("endpoint_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoints(self) -> typing.Optional[typing.List["IEndpoint"]]:
        '''Initial list of endpoints for this group.

        :default: - Group is initially empty
        '''
        result = self._values.get("endpoints")
        return typing.cast(typing.Optional[typing.List["IEndpoint"]], result)

    @builtins.property
    def health_check_interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The time between health checks for each endpoint.

        Must be either 10 or 30 seconds.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("health_check_interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''The ping path for health checks (if the protocol is HTTP(S)).

        :default: '/'
        '''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_port(self) -> typing.Optional[jsii.Number]:
        '''The port used to perform health checks.

        :default: - The listener's port
        '''
        result = self._values.get("health_check_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_protocol(self) -> typing.Optional["HealthCheckProtocol"]:
        '''The protocol used to perform health checks.

        :default: HealthCheckProtocol.TCP
        '''
        result = self._values.get("health_check_protocol")
        return typing.cast(typing.Optional["HealthCheckProtocol"], result)

    @builtins.property
    def health_check_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy.

        :default: 3
        '''
        result = self._values.get("health_check_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_overrides(self) -> typing.Optional[typing.List["PortOverride"]]:
        '''Override the destination ports used to route traffic to an endpoint.

        Unless overridden, the port used to hit the endpoint will be the same as the port
        that traffic arrives on at the listener.

        :default: - No overrides
        '''
        result = self._values.get("port_overrides")
        return typing.cast(typing.Optional[typing.List["PortOverride"]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region where the endpoint group is located.

        :default: - region of the first endpoint in this group, or the stack region if that region can't be determined
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def traffic_dial_percentage(self) -> typing.Optional[jsii.Number]:
        '''The percentage of traffic to send to this AWS Region.

        The percentage is applied to the traffic that would otherwise have been
        routed to the Region based on optimal routing. Additional traffic is
        distributed to other endpoint groups for this listener.

        :default: 100
        '''
        result = self._values.get("traffic_dial_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def listener(self) -> "IListener":
        '''The Amazon Resource Name (ARN) of the listener.'''
        result = self._values.get("listener")
        assert result is not None, "Required property 'listener' is missing"
        return typing.cast("IListener", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_globalaccelerator.HealthCheckProtocol")
class HealthCheckProtocol(enum.Enum):
    '''The protocol for the connections from clients to the accelerator.'''

    TCP = "TCP"
    '''TCP.'''
    HTTP = "HTTP"
    '''HTTP.'''
    HTTPS = "HTTPS"
    '''HTTPS.'''


@jsii.interface(jsii_type="aws-cdk-lib.aws_globalaccelerator.IAccelerator")
class IAccelerator(_IResource_c80c4260, typing_extensions.Protocol):
    '''The interface of the Accelerator.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceleratorArn")
    def accelerator_arn(self) -> builtins.str:
        '''The ARN of the accelerator.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        '''The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IP addresses.

        :attribute: true
        '''
        ...


class _IAcceleratorProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''The interface of the Accelerator.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_globalaccelerator.IAccelerator"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceleratorArn")
    def accelerator_arn(self) -> builtins.str:
        '''The ARN of the accelerator.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "acceleratorArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        '''The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IP addresses.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccelerator).__jsii_proxy_class__ = lambda : _IAcceleratorProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_globalaccelerator.IEndpoint")
class IEndpoint(typing_extensions.Protocol):
    '''An endpoint for the endpoint group.

    Implementations of ``IEndpoint`` can be found in the ``aws-globalaccelerator-endpoints`` package.
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the endpoint is located.

        If the region cannot be determined, ``undefined`` is returned
        '''
        ...

    @jsii.member(jsii_name="renderEndpointConfiguration")
    def render_endpoint_configuration(self) -> typing.Any:
        '''Render the endpoint to an endpoint configuration.'''
        ...


class _IEndpointProxy:
    '''An endpoint for the endpoint group.

    Implementations of ``IEndpoint`` can be found in the ``aws-globalaccelerator-endpoints`` package.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_globalaccelerator.IEndpoint"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the endpoint is located.

        If the region cannot be determined, ``undefined`` is returned
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @jsii.member(jsii_name="renderEndpointConfiguration")
    def render_endpoint_configuration(self) -> typing.Any:
        '''Render the endpoint to an endpoint configuration.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderEndpointConfiguration", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpoint).__jsii_proxy_class__ = lambda : _IEndpointProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_globalaccelerator.IEndpointGroup")
class IEndpointGroup(_IResource_c80c4260, typing_extensions.Protocol):
    '''The interface of the EndpointGroup.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointGroupArn")
    def endpoint_group_arn(self) -> builtins.str:
        '''EndpointGroup ARN.

        :attribute: true
        '''
        ...


class _IEndpointGroupProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''The interface of the EndpointGroup.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_globalaccelerator.IEndpointGroup"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointGroupArn")
    def endpoint_group_arn(self) -> builtins.str:
        '''EndpointGroup ARN.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointGroupArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointGroup).__jsii_proxy_class__ = lambda : _IEndpointGroupProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_globalaccelerator.IListener")
class IListener(_IResource_c80c4260, typing_extensions.Protocol):
    '''Interface of the Listener.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listenerArn")
    def listener_arn(self) -> builtins.str:
        '''The ARN of the listener.

        :attribute: true
        '''
        ...


class _IListenerProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''Interface of the Listener.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_globalaccelerator.IListener"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listenerArn")
    def listener_arn(self) -> builtins.str:
        '''The ARN of the listener.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "listenerArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IListener).__jsii_proxy_class__ = lambda : _IListenerProxy


@jsii.implements(IListener)
class Listener(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.Listener",
):
    '''The construct for the Listener.

    :exampleMetadata: infused

    Example::

        # Create an Accelerator
        accelerator = globalaccelerator.Accelerator(self, "Accelerator")
        
        # Create a Listener
        listener = accelerator.add_listener("Listener",
            port_ranges=[globalaccelerator.PortRange(from_port=80), globalaccelerator.PortRange(from_port=443)
            ]
        )
        
        # Import the Load Balancers
        nlb1 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(self, "NLB1",
            load_balancer_arn="arn:aws:elasticloadbalancing:us-west-2:111111111111:loadbalancer/app/my-load-balancer1/e16bef66805b"
        )
        nlb2 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(self, "NLB2",
            load_balancer_arn="arn:aws:elasticloadbalancing:ap-south-1:111111111111:loadbalancer/app/my-load-balancer2/5513dc2ea8a1"
        )
        
        # Add one EndpointGroup for each Region we are targeting
        listener.add_endpoint_group("Group1",
            endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb1)]
        )
        listener.add_endpoint_group("Group2",
            # Imported load balancers automatically calculate their Region from the ARN.
            # If you are load balancing to other resources, you must also pass a `region`
            # parameter here.
            endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb2)]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accelerator: IAccelerator,
        port_ranges: typing.Sequence["PortRange"],
        client_affinity: typing.Optional[ClientAffinity] = None,
        listener_name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[ConnectionProtocol] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param accelerator: The accelerator for this listener.
        :param port_ranges: The list of port ranges for the connections from clients to the accelerator.
        :param client_affinity: Client affinity to direct all requests from a user to the same endpoint. If you have stateful applications, client affinity lets you direct all requests from a user to the same endpoint. By default, each connection from each client is routed to seperate endpoints. Set client affinity to SOURCE_IP to route all connections from a single client to the same endpoint. Default: ClientAffinity.NONE
        :param listener_name: Name of the listener. Default: - logical ID of the resource
        :param protocol: The protocol for the connections from clients to the accelerator. Default: ConnectionProtocol.TCP
        '''
        props = ListenerProps(
            accelerator=accelerator,
            port_ranges=port_ranges,
            client_affinity=client_affinity,
            listener_name=listener_name,
            protocol=protocol,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromListenerArn") # type: ignore[misc]
    @builtins.classmethod
    def from_listener_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        listener_arn: builtins.str,
    ) -> IListener:
        '''import from ARN.

        :param scope: -
        :param id: -
        :param listener_arn: -
        '''
        return typing.cast(IListener, jsii.sinvoke(cls, "fromListenerArn", [scope, id, listener_arn]))

    @jsii.member(jsii_name="addEndpointGroup")
    def add_endpoint_group(
        self,
        id: builtins.str,
        *,
        endpoint_group_name: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Sequence[IEndpoint]] = None,
        health_check_interval: typing.Optional[_Duration_4839e8c3] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional[HealthCheckProtocol] = None,
        health_check_threshold: typing.Optional[jsii.Number] = None,
        port_overrides: typing.Optional[typing.Sequence["PortOverride"]] = None,
        region: typing.Optional[builtins.str] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
    ) -> "EndpointGroup":
        '''Add a new endpoint group to this listener.

        :param id: -
        :param endpoint_group_name: Name of the endpoint group. Default: - logical ID of the resource
        :param endpoints: Initial list of endpoints for this group. Default: - Group is initially empty
        :param health_check_interval: The time between health checks for each endpoint. Must be either 10 or 30 seconds. Default: Duration.seconds(30)
        :param health_check_path: The ping path for health checks (if the protocol is HTTP(S)). Default: '/'
        :param health_check_port: The port used to perform health checks. Default: - The listener's port
        :param health_check_protocol: The protocol used to perform health checks. Default: HealthCheckProtocol.TCP
        :param health_check_threshold: The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. Default: 3
        :param port_overrides: Override the destination ports used to route traffic to an endpoint. Unless overridden, the port used to hit the endpoint will be the same as the port that traffic arrives on at the listener. Default: - No overrides
        :param region: The AWS Region where the endpoint group is located. Default: - region of the first endpoint in this group, or the stack region if that region can't be determined
        :param traffic_dial_percentage: The percentage of traffic to send to this AWS Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. Additional traffic is distributed to other endpoint groups for this listener. Default: 100
        '''
        options = EndpointGroupOptions(
            endpoint_group_name=endpoint_group_name,
            endpoints=endpoints,
            health_check_interval=health_check_interval,
            health_check_path=health_check_path,
            health_check_port=health_check_port,
            health_check_protocol=health_check_protocol,
            health_check_threshold=health_check_threshold,
            port_overrides=port_overrides,
            region=region,
            traffic_dial_percentage=traffic_dial_percentage,
        )

        return typing.cast("EndpointGroup", jsii.invoke(self, "addEndpointGroup", [id, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listenerArn")
    def listener_arn(self) -> builtins.str:
        '''The ARN of the listener.'''
        return typing.cast(builtins.str, jsii.get(self, "listenerArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="listenerName")
    def listener_name(self) -> builtins.str:
        '''The name of the listener.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "listenerName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.ListenerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "port_ranges": "portRanges",
        "client_affinity": "clientAffinity",
        "listener_name": "listenerName",
        "protocol": "protocol",
    },
)
class ListenerOptions:
    def __init__(
        self,
        *,
        port_ranges: typing.Sequence["PortRange"],
        client_affinity: typing.Optional[ClientAffinity] = None,
        listener_name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[ConnectionProtocol] = None,
    ) -> None:
        '''Construct options for Listener.

        :param port_ranges: The list of port ranges for the connections from clients to the accelerator.
        :param client_affinity: Client affinity to direct all requests from a user to the same endpoint. If you have stateful applications, client affinity lets you direct all requests from a user to the same endpoint. By default, each connection from each client is routed to seperate endpoints. Set client affinity to SOURCE_IP to route all connections from a single client to the same endpoint. Default: ClientAffinity.NONE
        :param listener_name: Name of the listener. Default: - logical ID of the resource
        :param protocol: The protocol for the connections from clients to the accelerator. Default: ConnectionProtocol.TCP

        :exampleMetadata: infused

        Example::

            # Create an Accelerator
            accelerator = globalaccelerator.Accelerator(self, "Accelerator")
            
            # Create a Listener
            listener = accelerator.add_listener("Listener",
                port_ranges=[globalaccelerator.PortRange(from_port=80), globalaccelerator.PortRange(from_port=443)
                ]
            )
            
            # Import the Load Balancers
            nlb1 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(self, "NLB1",
                load_balancer_arn="arn:aws:elasticloadbalancing:us-west-2:111111111111:loadbalancer/app/my-load-balancer1/e16bef66805b"
            )
            nlb2 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(self, "NLB2",
                load_balancer_arn="arn:aws:elasticloadbalancing:ap-south-1:111111111111:loadbalancer/app/my-load-balancer2/5513dc2ea8a1"
            )
            
            # Add one EndpointGroup for each Region we are targeting
            listener.add_endpoint_group("Group1",
                endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb1)]
            )
            listener.add_endpoint_group("Group2",
                # Imported load balancers automatically calculate their Region from the ARN.
                # If you are load balancing to other resources, you must also pass a `region`
                # parameter here.
                endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb2)]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "port_ranges": port_ranges,
        }
        if client_affinity is not None:
            self._values["client_affinity"] = client_affinity
        if listener_name is not None:
            self._values["listener_name"] = listener_name
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def port_ranges(self) -> typing.List["PortRange"]:
        '''The list of port ranges for the connections from clients to the accelerator.'''
        result = self._values.get("port_ranges")
        assert result is not None, "Required property 'port_ranges' is missing"
        return typing.cast(typing.List["PortRange"], result)

    @builtins.property
    def client_affinity(self) -> typing.Optional[ClientAffinity]:
        '''Client affinity to direct all requests from a user to the same endpoint.

        If you have stateful applications, client affinity lets you direct all
        requests from a user to the same endpoint.

        By default, each connection from each client is routed to seperate
        endpoints. Set client affinity to SOURCE_IP to route all connections from
        a single client to the same endpoint.

        :default: ClientAffinity.NONE
        '''
        result = self._values.get("client_affinity")
        return typing.cast(typing.Optional[ClientAffinity], result)

    @builtins.property
    def listener_name(self) -> typing.Optional[builtins.str]:
        '''Name of the listener.

        :default: - logical ID of the resource
        '''
        result = self._values.get("listener_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[ConnectionProtocol]:
        '''The protocol for the connections from clients to the accelerator.

        :default: ConnectionProtocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[ConnectionProtocol], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListenerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.ListenerProps",
    jsii_struct_bases=[ListenerOptions],
    name_mapping={
        "port_ranges": "portRanges",
        "client_affinity": "clientAffinity",
        "listener_name": "listenerName",
        "protocol": "protocol",
        "accelerator": "accelerator",
    },
)
class ListenerProps(ListenerOptions):
    def __init__(
        self,
        *,
        port_ranges: typing.Sequence["PortRange"],
        client_affinity: typing.Optional[ClientAffinity] = None,
        listener_name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[ConnectionProtocol] = None,
        accelerator: IAccelerator,
    ) -> None:
        '''Construct properties for Listener.

        :param port_ranges: The list of port ranges for the connections from clients to the accelerator.
        :param client_affinity: Client affinity to direct all requests from a user to the same endpoint. If you have stateful applications, client affinity lets you direct all requests from a user to the same endpoint. By default, each connection from each client is routed to seperate endpoints. Set client affinity to SOURCE_IP to route all connections from a single client to the same endpoint. Default: ClientAffinity.NONE
        :param listener_name: Name of the listener. Default: - logical ID of the resource
        :param protocol: The protocol for the connections from clients to the accelerator. Default: ConnectionProtocol.TCP
        :param accelerator: The accelerator for this listener.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_globalaccelerator as globalaccelerator
            
            # accelerator: globalaccelerator.Accelerator
            
            listener_props = globalaccelerator.ListenerProps(
                accelerator=accelerator,
                port_ranges=[globalaccelerator.PortRange(
                    from_port=123,
            
                    # the properties below are optional
                    to_port=123
                )],
            
                # the properties below are optional
                client_affinity=globalaccelerator.ClientAffinity.NONE,
                listener_name="listenerName",
                protocol=globalaccelerator.ConnectionProtocol.TCP
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "port_ranges": port_ranges,
            "accelerator": accelerator,
        }
        if client_affinity is not None:
            self._values["client_affinity"] = client_affinity
        if listener_name is not None:
            self._values["listener_name"] = listener_name
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def port_ranges(self) -> typing.List["PortRange"]:
        '''The list of port ranges for the connections from clients to the accelerator.'''
        result = self._values.get("port_ranges")
        assert result is not None, "Required property 'port_ranges' is missing"
        return typing.cast(typing.List["PortRange"], result)

    @builtins.property
    def client_affinity(self) -> typing.Optional[ClientAffinity]:
        '''Client affinity to direct all requests from a user to the same endpoint.

        If you have stateful applications, client affinity lets you direct all
        requests from a user to the same endpoint.

        By default, each connection from each client is routed to seperate
        endpoints. Set client affinity to SOURCE_IP to route all connections from
        a single client to the same endpoint.

        :default: ClientAffinity.NONE
        '''
        result = self._values.get("client_affinity")
        return typing.cast(typing.Optional[ClientAffinity], result)

    @builtins.property
    def listener_name(self) -> typing.Optional[builtins.str]:
        '''Name of the listener.

        :default: - logical ID of the resource
        '''
        result = self._values.get("listener_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[ConnectionProtocol]:
        '''The protocol for the connections from clients to the accelerator.

        :default: ConnectionProtocol.TCP
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[ConnectionProtocol], result)

    @builtins.property
    def accelerator(self) -> IAccelerator:
        '''The accelerator for this listener.'''
        result = self._values.get("accelerator")
        assert result is not None, "Required property 'accelerator' is missing"
        return typing.cast(IAccelerator, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListenerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.PortOverride",
    jsii_struct_bases=[],
    name_mapping={"endpoint_port": "endpointPort", "listener_port": "listenerPort"},
)
class PortOverride:
    def __init__(
        self,
        *,
        endpoint_port: jsii.Number,
        listener_port: jsii.Number,
    ) -> None:
        '''Override specific listener ports used to route traffic to endpoints that are part of an endpoint group.

        :param endpoint_port: The endpoint port that you want a listener port to be mapped to. This is the port on the endpoint, such as the Application Load Balancer or Amazon EC2 instance.
        :param listener_port: The listener port that you want to map to a specific endpoint port. This is the port that user traffic arrives to the Global Accelerator on.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_globalaccelerator as globalaccelerator
            
            port_override = globalaccelerator.PortOverride(
                endpoint_port=123,
                listener_port=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_port": endpoint_port,
            "listener_port": listener_port,
        }

    @builtins.property
    def endpoint_port(self) -> jsii.Number:
        '''The endpoint port that you want a listener port to be mapped to.

        This is the port on the endpoint, such as the Application Load Balancer or Amazon EC2 instance.
        '''
        result = self._values.get("endpoint_port")
        assert result is not None, "Required property 'endpoint_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def listener_port(self) -> jsii.Number:
        '''The listener port that you want to map to a specific endpoint port.

        This is the port that user traffic arrives to the Global Accelerator on.
        '''
        result = self._values.get("listener_port")
        assert result is not None, "Required property 'listener_port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.PortRange",
    jsii_struct_bases=[],
    name_mapping={"from_port": "fromPort", "to_port": "toPort"},
)
class PortRange:
    def __init__(
        self,
        *,
        from_port: jsii.Number,
        to_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''The list of port ranges for the connections from clients to the accelerator.

        :param from_port: The first port in the range of ports, inclusive.
        :param to_port: The last port in the range of ports, inclusive. Default: - same as ``fromPort``

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_globalaccelerator as globalaccelerator
            
            port_range = globalaccelerator.PortRange(
                from_port=123,
            
                # the properties below are optional
                to_port=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "from_port": from_port,
        }
        if to_port is not None:
            self._values["to_port"] = to_port

    @builtins.property
    def from_port(self) -> jsii.Number:
        '''The first port in the range of ports, inclusive.'''
        result = self._values.get("from_port")
        assert result is not None, "Required property 'from_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def to_port(self) -> typing.Optional[jsii.Number]:
        '''The last port in the range of ports, inclusive.

        :default: - same as ``fromPort``
        '''
        result = self._values.get("to_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IEndpoint)
class RawEndpoint(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.RawEndpoint",
):
    '''Untyped endpoint implementation.

    Prefer using the classes in the ``aws-globalaccelerator-endpoints`` package instead,
    as they accept typed constructs. You can use this class if you want to use an
    endpoint type that does not have an appropriate class in that package yet.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_globalaccelerator as globalaccelerator
        
        raw_endpoint = globalaccelerator.RawEndpoint(
            endpoint_id="endpointId",
        
            # the properties below are optional
            preserve_client_ip=False,
            region="region",
            weight=123
        )
    '''

    def __init__(
        self,
        *,
        endpoint_id: builtins.str,
        preserve_client_ip: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param endpoint_id: Identifier of the endpoint. Load balancer ARN, instance ID or EIP allocation ID.
        :param preserve_client_ip: Forward the client IP address. GlobalAccelerator will create Network Interfaces in your VPC in order to preserve the client IP address. Only applies to Application Load Balancers and EC2 instances. Client IP address preservation is supported only in specific AWS Regions. See the GlobalAccelerator Developer Guide for a list. Default: true if possible and available
        :param region: The region where this endpoint is located. Default: - Unknown what region this endpoint is located
        :param weight: Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128
        '''
        props = RawEndpointProps(
            endpoint_id=endpoint_id,
            preserve_client_ip=preserve_client_ip,
            region=region,
            weight=weight,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="renderEndpointConfiguration")
    def render_endpoint_configuration(self) -> typing.Any:
        '''Render the endpoint to an endpoint configuration.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderEndpointConfiguration", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the endpoint is located.

        If the region cannot be determined, ``undefined`` is returned
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator.RawEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_id": "endpointId",
        "preserve_client_ip": "preserveClientIp",
        "region": "region",
        "weight": "weight",
    },
)
class RawEndpointProps:
    def __init__(
        self,
        *,
        endpoint_id: builtins.str,
        preserve_client_ip: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for RawEndpoint.

        :param endpoint_id: Identifier of the endpoint. Load balancer ARN, instance ID or EIP allocation ID.
        :param preserve_client_ip: Forward the client IP address. GlobalAccelerator will create Network Interfaces in your VPC in order to preserve the client IP address. Only applies to Application Load Balancers and EC2 instances. Client IP address preservation is supported only in specific AWS Regions. See the GlobalAccelerator Developer Guide for a list. Default: true if possible and available
        :param region: The region where this endpoint is located. Default: - Unknown what region this endpoint is located
        :param weight: Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_globalaccelerator as globalaccelerator
            
            raw_endpoint_props = globalaccelerator.RawEndpointProps(
                endpoint_id="endpointId",
            
                # the properties below are optional
                preserve_client_ip=False,
                region="region",
                weight=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_id": endpoint_id,
        }
        if preserve_client_ip is not None:
            self._values["preserve_client_ip"] = preserve_client_ip
        if region is not None:
            self._values["region"] = region
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def endpoint_id(self) -> builtins.str:
        '''Identifier of the endpoint.

        Load balancer ARN, instance ID or EIP allocation ID.
        '''
        result = self._values.get("endpoint_id")
        assert result is not None, "Required property 'endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preserve_client_ip(self) -> typing.Optional[builtins.bool]:
        '''Forward the client IP address.

        GlobalAccelerator will create Network Interfaces in your VPC in order
        to preserve the client IP address.

        Only applies to Application Load Balancers and EC2 instances.

        Client IP address preservation is supported only in specific AWS Regions.
        See the GlobalAccelerator Developer Guide for a list.

        :default: true if possible and available
        '''
        result = self._values.get("preserve_client_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where this endpoint is located.

        :default: - Unknown what region this endpoint is located
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Endpoint weight across all endpoints in the group.

        Must be a value between 0 and 255.

        :default: 128
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RawEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IAccelerator)
class Accelerator(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.Accelerator",
):
    '''The Accelerator construct.

    :exampleMetadata: infused

    Example::

        # Create an Accelerator
        accelerator = globalaccelerator.Accelerator(self, "Accelerator")
        
        # Create a Listener
        listener = accelerator.add_listener("Listener",
            port_ranges=[globalaccelerator.PortRange(from_port=80), globalaccelerator.PortRange(from_port=443)
            ]
        )
        
        # Import the Load Balancers
        nlb1 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(self, "NLB1",
            load_balancer_arn="arn:aws:elasticloadbalancing:us-west-2:111111111111:loadbalancer/app/my-load-balancer1/e16bef66805b"
        )
        nlb2 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(self, "NLB2",
            load_balancer_arn="arn:aws:elasticloadbalancing:ap-south-1:111111111111:loadbalancer/app/my-load-balancer2/5513dc2ea8a1"
        )
        
        # Add one EndpointGroup for each Region we are targeting
        listener.add_endpoint_group("Group1",
            endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb1)]
        )
        listener.add_endpoint_group("Group2",
            # Imported load balancers automatically calculate their Region from the ARN.
            # If you are load balancing to other resources, you must also pass a `region`
            # parameter here.
            endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb2)]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accelerator_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param accelerator_name: The name of the accelerator. Default: - resource ID
        :param enabled: Indicates whether the accelerator is enabled. Default: true
        '''
        props = AcceleratorProps(accelerator_name=accelerator_name, enabled=enabled)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAcceleratorAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_accelerator_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        accelerator_arn: builtins.str,
        dns_name: builtins.str,
    ) -> IAccelerator:
        '''import from attributes.

        :param scope: -
        :param id: -
        :param accelerator_arn: The ARN of the accelerator.
        :param dns_name: The DNS name of the accelerator.
        '''
        attrs = AcceleratorAttributes(
            accelerator_arn=accelerator_arn, dns_name=dns_name
        )

        return typing.cast(IAccelerator, jsii.sinvoke(cls, "fromAcceleratorAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addListener")
    def add_listener(
        self,
        id: builtins.str,
        *,
        port_ranges: typing.Sequence[PortRange],
        client_affinity: typing.Optional[ClientAffinity] = None,
        listener_name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[ConnectionProtocol] = None,
    ) -> Listener:
        '''Add a listener to the accelerator.

        :param id: -
        :param port_ranges: The list of port ranges for the connections from clients to the accelerator.
        :param client_affinity: Client affinity to direct all requests from a user to the same endpoint. If you have stateful applications, client affinity lets you direct all requests from a user to the same endpoint. By default, each connection from each client is routed to seperate endpoints. Set client affinity to SOURCE_IP to route all connections from a single client to the same endpoint. Default: ClientAffinity.NONE
        :param listener_name: Name of the listener. Default: - logical ID of the resource
        :param protocol: The protocol for the connections from clients to the accelerator. Default: ConnectionProtocol.TCP
        '''
        options = ListenerOptions(
            port_ranges=port_ranges,
            client_affinity=client_affinity,
            listener_name=listener_name,
            protocol=protocol,
        )

        return typing.cast(Listener, jsii.invoke(self, "addListener", [id, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceleratorArn")
    def accelerator_arn(self) -> builtins.str:
        '''The ARN of the accelerator.'''
        return typing.cast(builtins.str, jsii.get(self, "acceleratorArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        '''The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IP addresses.'''
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))


@jsii.implements(IEndpointGroup)
class EndpointGroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator.EndpointGroup",
):
    '''EndpointGroup construct.

    :exampleMetadata: infused

    Example::

        # listener: globalaccelerator.Listener
        
        # Non-open ALB
        # alb: elbv2.ApplicationLoadBalancer
        
        # Remember that there is only one AGA security group per VPC.
        # vpc: ec2.Vpc
        
        
        endpoint_group = listener.add_endpoint_group("Group",
            endpoints=[
                ga_endpoints.ApplicationLoadBalancerEndpoint(alb,
                    preserve_client_ip=True
                )
            ]
        )
        aga_sg = endpoint_group.connections_peer("GlobalAcceleratorSG", vpc)
        
        # Allow connections from the AGA to the ALB
        alb.connections.allow_from(aga_sg, ec2.Port.tcp(443))
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        listener: IListener,
        endpoint_group_name: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Sequence[IEndpoint]] = None,
        health_check_interval: typing.Optional[_Duration_4839e8c3] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        health_check_port: typing.Optional[jsii.Number] = None,
        health_check_protocol: typing.Optional[HealthCheckProtocol] = None,
        health_check_threshold: typing.Optional[jsii.Number] = None,
        port_overrides: typing.Optional[typing.Sequence[PortOverride]] = None,
        region: typing.Optional[builtins.str] = None,
        traffic_dial_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param listener: The Amazon Resource Name (ARN) of the listener.
        :param endpoint_group_name: Name of the endpoint group. Default: - logical ID of the resource
        :param endpoints: Initial list of endpoints for this group. Default: - Group is initially empty
        :param health_check_interval: The time between health checks for each endpoint. Must be either 10 or 30 seconds. Default: Duration.seconds(30)
        :param health_check_path: The ping path for health checks (if the protocol is HTTP(S)). Default: '/'
        :param health_check_port: The port used to perform health checks. Default: - The listener's port
        :param health_check_protocol: The protocol used to perform health checks. Default: HealthCheckProtocol.TCP
        :param health_check_threshold: The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. Default: 3
        :param port_overrides: Override the destination ports used to route traffic to an endpoint. Unless overridden, the port used to hit the endpoint will be the same as the port that traffic arrives on at the listener. Default: - No overrides
        :param region: The AWS Region where the endpoint group is located. Default: - region of the first endpoint in this group, or the stack region if that region can't be determined
        :param traffic_dial_percentage: The percentage of traffic to send to this AWS Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing. Additional traffic is distributed to other endpoint groups for this listener. Default: 100
        '''
        props = EndpointGroupProps(
            listener=listener,
            endpoint_group_name=endpoint_group_name,
            endpoints=endpoints,
            health_check_interval=health_check_interval,
            health_check_path=health_check_path,
            health_check_port=health_check_port,
            health_check_protocol=health_check_protocol,
            health_check_threshold=health_check_threshold,
            port_overrides=port_overrides,
            region=region,
            traffic_dial_percentage=traffic_dial_percentage,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEndpointGroupArn") # type: ignore[misc]
    @builtins.classmethod
    def from_endpoint_group_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        endpoint_group_arn: builtins.str,
    ) -> IEndpointGroup:
        '''import from ARN.

        :param scope: -
        :param id: -
        :param endpoint_group_arn: -
        '''
        return typing.cast(IEndpointGroup, jsii.sinvoke(cls, "fromEndpointGroupArn", [scope, id, endpoint_group_arn]))

    @jsii.member(jsii_name="addEndpoint")
    def add_endpoint(self, endpoint: IEndpoint) -> None:
        '''Add an endpoint.

        :param endpoint: -
        '''
        return typing.cast(None, jsii.invoke(self, "addEndpoint", [endpoint]))

    @jsii.member(jsii_name="connectionsPeer")
    def connections_peer(
        self,
        id: builtins.str,
        vpc: _IVpc_f30d5663,
    ) -> _IPeer_cf58db9a:
        '''Return an object that represents the Accelerator's Security Group.

        Uses a Custom Resource to look up the Security Group that Accelerator
        creates at deploy time. Requires your VPC ID to perform the lookup.

        The Security Group will only be created if you enable **Client IP
        Preservation** on any of the endpoints.

        You cannot manipulate the rules inside this security group, but you can
        use this security group as a Peer in Connections rules on other
        constructs.

        :param id: -
        :param vpc: -
        '''
        return typing.cast(_IPeer_cf58db9a, jsii.invoke(self, "connectionsPeer", [id, vpc]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointGroupArn")
    def endpoint_group_arn(self) -> builtins.str:
        '''EndpointGroup ARN.'''
        return typing.cast(builtins.str, jsii.get(self, "endpointGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointGroupName")
    def endpoint_group_name(self) -> builtins.str:
        '''The name of the endpoint group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointGroupName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpoints")
    def _endpoints(self) -> typing.List[IEndpoint]:
        '''The array of the endpoints in this endpoint group.'''
        return typing.cast(typing.List[IEndpoint], jsii.get(self, "endpoints"))


__all__ = [
    "Accelerator",
    "AcceleratorAttributes",
    "AcceleratorProps",
    "CfnAccelerator",
    "CfnAcceleratorProps",
    "CfnEndpointGroup",
    "CfnEndpointGroupProps",
    "CfnListener",
    "CfnListenerProps",
    "ClientAffinity",
    "ConnectionProtocol",
    "EndpointGroup",
    "EndpointGroupOptions",
    "EndpointGroupProps",
    "HealthCheckProtocol",
    "IAccelerator",
    "IEndpoint",
    "IEndpointGroup",
    "IListener",
    "Listener",
    "ListenerOptions",
    "ListenerProps",
    "PortOverride",
    "PortRange",
    "RawEndpoint",
    "RawEndpointProps",
]

publication.publish()
