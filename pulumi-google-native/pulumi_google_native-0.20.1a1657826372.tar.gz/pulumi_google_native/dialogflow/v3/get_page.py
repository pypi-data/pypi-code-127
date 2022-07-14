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

__all__ = [
    'GetPageResult',
    'AwaitableGetPageResult',
    'get_page',
    'get_page_output',
]

@pulumi.output_type
class GetPageResult:
    def __init__(__self__, display_name=None, entry_fulfillment=None, event_handlers=None, form=None, name=None, transition_route_groups=None, transition_routes=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if entry_fulfillment and not isinstance(entry_fulfillment, dict):
            raise TypeError("Expected argument 'entry_fulfillment' to be a dict")
        pulumi.set(__self__, "entry_fulfillment", entry_fulfillment)
        if event_handlers and not isinstance(event_handlers, list):
            raise TypeError("Expected argument 'event_handlers' to be a list")
        pulumi.set(__self__, "event_handlers", event_handlers)
        if form and not isinstance(form, dict):
            raise TypeError("Expected argument 'form' to be a dict")
        pulumi.set(__self__, "form", form)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if transition_route_groups and not isinstance(transition_route_groups, list):
            raise TypeError("Expected argument 'transition_route_groups' to be a list")
        pulumi.set(__self__, "transition_route_groups", transition_route_groups)
        if transition_routes and not isinstance(transition_routes, list):
            raise TypeError("Expected argument 'transition_routes' to be a list")
        pulumi.set(__self__, "transition_routes", transition_routes)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The human-readable name of the page, unique within the flow.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="entryFulfillment")
    def entry_fulfillment(self) -> 'outputs.GoogleCloudDialogflowCxV3FulfillmentResponse':
        """
        The fulfillment to call when the session is entering the page.
        """
        return pulumi.get(self, "entry_fulfillment")

    @property
    @pulumi.getter(name="eventHandlers")
    def event_handlers(self) -> Sequence['outputs.GoogleCloudDialogflowCxV3EventHandlerResponse']:
        """
        Handlers associated with the page to handle events such as webhook errors, no match or no input.
        """
        return pulumi.get(self, "event_handlers")

    @property
    @pulumi.getter
    def form(self) -> 'outputs.GoogleCloudDialogflowCxV3FormResponse':
        """
        The form associated with the page, used for collecting parameters relevant to the page.
        """
        return pulumi.get(self, "form")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The unique identifier of the page. Required for the Pages.UpdatePage method. Pages.CreatePage populates the name automatically. Format: `projects//locations//agents//flows//pages/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="transitionRouteGroups")
    def transition_route_groups(self) -> Sequence[str]:
        """
        Ordered list of `TransitionRouteGroups` associated with the page. Transition route groups must be unique within a page. * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes. * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:`projects//locations//agents//flows//transitionRouteGroups/`.
        """
        return pulumi.get(self, "transition_route_groups")

    @property
    @pulumi.getter(name="transitionRoutes")
    def transition_routes(self) -> Sequence['outputs.GoogleCloudDialogflowCxV3TransitionRouteResponse']:
        """
        A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow. When we are in a certain page, the TransitionRoutes are evalauted in the following order: * TransitionRoutes defined in the page with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in flow with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in the page with only condition specified. * TransitionRoutes defined in the transition route groups with only condition specified.
        """
        return pulumi.get(self, "transition_routes")


class AwaitableGetPageResult(GetPageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPageResult(
            display_name=self.display_name,
            entry_fulfillment=self.entry_fulfillment,
            event_handlers=self.event_handlers,
            form=self.form,
            name=self.name,
            transition_route_groups=self.transition_route_groups,
            transition_routes=self.transition_routes)


def get_page(agent_id: Optional[str] = None,
             flow_id: Optional[str] = None,
             language_code: Optional[str] = None,
             location: Optional[str] = None,
             page_id: Optional[str] = None,
             project: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPageResult:
    """
    Retrieves the specified page.
    """
    __args__ = dict()
    __args__['agentId'] = agent_id
    __args__['flowId'] = flow_id
    __args__['languageCode'] = language_code
    __args__['location'] = location
    __args__['pageId'] = page_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dialogflow/v3:getPage', __args__, opts=opts, typ=GetPageResult).value

    return AwaitableGetPageResult(
        display_name=__ret__.display_name,
        entry_fulfillment=__ret__.entry_fulfillment,
        event_handlers=__ret__.event_handlers,
        form=__ret__.form,
        name=__ret__.name,
        transition_route_groups=__ret__.transition_route_groups,
        transition_routes=__ret__.transition_routes)


@_utilities.lift_output_func(get_page)
def get_page_output(agent_id: Optional[pulumi.Input[str]] = None,
                    flow_id: Optional[pulumi.Input[str]] = None,
                    language_code: Optional[pulumi.Input[Optional[str]]] = None,
                    location: Optional[pulumi.Input[str]] = None,
                    page_id: Optional[pulumi.Input[str]] = None,
                    project: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPageResult]:
    """
    Retrieves the specified page.
    """
    ...
