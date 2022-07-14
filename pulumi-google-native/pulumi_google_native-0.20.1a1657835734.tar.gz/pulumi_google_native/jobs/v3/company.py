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

__all__ = ['CompanyArgs', 'Company']

@pulumi.input_type
class CompanyArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 external_id: pulumi.Input[str],
                 career_site_uri: Optional[pulumi.Input[str]] = None,
                 eeo_text: Optional[pulumi.Input[str]] = None,
                 headquarters_address: Optional[pulumi.Input[str]] = None,
                 hiring_agency: Optional[pulumi.Input[bool]] = None,
                 image_uri: Optional[pulumi.Input[str]] = None,
                 keyword_searchable_job_custom_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input['CompanySize']] = None,
                 website_uri: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Company resource.
        :param pulumi.Input[str] display_name: The display name of the company, for example, "Google LLC".
        :param pulumi.Input[str] external_id: Client side company identifier, used to uniquely identify the company. The maximum number of allowed characters is 255.
        :param pulumi.Input[str] career_site_uri: Optional. The URI to employer's career site or careers page on the employer's web site, for example, "https://careers.google.com".
        :param pulumi.Input[str] eeo_text: Optional. Equal Employment Opportunity legal disclaimer text to be associated with all jobs, and typically to be displayed in all roles. The maximum number of allowed characters is 500.
        :param pulumi.Input[str] headquarters_address: Optional. The street address of the company's main headquarters, which may be different from the job location. The service attempts to geolocate the provided address, and populates a more specific location wherever possible in DerivedInfo.headquarters_location.
        :param pulumi.Input[bool] hiring_agency: Optional. Set to true if it is the hiring agency that post jobs for other employers. Defaults to false if not provided.
        :param pulumi.Input[str] image_uri: Optional. A URI that hosts the employer's company logo.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] keyword_searchable_job_custom_attributes: Optional. A list of keys of filterable Job.custom_attributes, whose corresponding `string_values` are used in keyword search. Jobs with `string_values` under these specified field keys are returned if any of the values matches the search keyword. Custom field values with parenthesis, brackets and special symbols won't be properly searchable, and those keyword queries need to be surrounded by quotes.
        :param pulumi.Input[str] name: Required during company update. The resource name for a company. This is generated by the service when a company is created. The format is "projects/{project_id}/companies/{company_id}", for example, "projects/api-test-project/companies/foo".
        :param pulumi.Input['CompanySize'] size: Optional. The employer's company size.
        :param pulumi.Input[str] website_uri: Optional. The URI representing the company's primary web site or home page, for example, "https://www.google.com". The maximum number of allowed characters is 255.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "external_id", external_id)
        if career_site_uri is not None:
            pulumi.set(__self__, "career_site_uri", career_site_uri)
        if eeo_text is not None:
            pulumi.set(__self__, "eeo_text", eeo_text)
        if headquarters_address is not None:
            pulumi.set(__self__, "headquarters_address", headquarters_address)
        if hiring_agency is not None:
            pulumi.set(__self__, "hiring_agency", hiring_agency)
        if image_uri is not None:
            pulumi.set(__self__, "image_uri", image_uri)
        if keyword_searchable_job_custom_attributes is not None:
            pulumi.set(__self__, "keyword_searchable_job_custom_attributes", keyword_searchable_job_custom_attributes)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if website_uri is not None:
            pulumi.set(__self__, "website_uri", website_uri)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the company, for example, "Google LLC".
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Input[str]:
        """
        Client side company identifier, used to uniquely identify the company. The maximum number of allowed characters is 255.
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="careerSiteUri")
    def career_site_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The URI to employer's career site or careers page on the employer's web site, for example, "https://careers.google.com".
        """
        return pulumi.get(self, "career_site_uri")

    @career_site_uri.setter
    def career_site_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "career_site_uri", value)

    @property
    @pulumi.getter(name="eeoText")
    def eeo_text(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Equal Employment Opportunity legal disclaimer text to be associated with all jobs, and typically to be displayed in all roles. The maximum number of allowed characters is 500.
        """
        return pulumi.get(self, "eeo_text")

    @eeo_text.setter
    def eeo_text(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eeo_text", value)

    @property
    @pulumi.getter(name="headquartersAddress")
    def headquarters_address(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The street address of the company's main headquarters, which may be different from the job location. The service attempts to geolocate the provided address, and populates a more specific location wherever possible in DerivedInfo.headquarters_location.
        """
        return pulumi.get(self, "headquarters_address")

    @headquarters_address.setter
    def headquarters_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "headquarters_address", value)

    @property
    @pulumi.getter(name="hiringAgency")
    def hiring_agency(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional. Set to true if it is the hiring agency that post jobs for other employers. Defaults to false if not provided.
        """
        return pulumi.get(self, "hiring_agency")

    @hiring_agency.setter
    def hiring_agency(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hiring_agency", value)

    @property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A URI that hosts the employer's company logo.
        """
        return pulumi.get(self, "image_uri")

    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_uri", value)

    @property
    @pulumi.getter(name="keywordSearchableJobCustomAttributes")
    def keyword_searchable_job_custom_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Optional. A list of keys of filterable Job.custom_attributes, whose corresponding `string_values` are used in keyword search. Jobs with `string_values` under these specified field keys are returned if any of the values matches the search keyword. Custom field values with parenthesis, brackets and special symbols won't be properly searchable, and those keyword queries need to be surrounded by quotes.
        """
        return pulumi.get(self, "keyword_searchable_job_custom_attributes")

    @keyword_searchable_job_custom_attributes.setter
    def keyword_searchable_job_custom_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "keyword_searchable_job_custom_attributes", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Required during company update. The resource name for a company. This is generated by the service when a company is created. The format is "projects/{project_id}/companies/{company_id}", for example, "projects/api-test-project/companies/foo".
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input['CompanySize']]:
        """
        Optional. The employer's company size.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input['CompanySize']]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="websiteUri")
    def website_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The URI representing the company's primary web site or home page, for example, "https://www.google.com". The maximum number of allowed characters is 255.
        """
        return pulumi.get(self, "website_uri")

    @website_uri.setter
    def website_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "website_uri", value)


class Company(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 career_site_uri: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 eeo_text: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 headquarters_address: Optional[pulumi.Input[str]] = None,
                 hiring_agency: Optional[pulumi.Input[bool]] = None,
                 image_uri: Optional[pulumi.Input[str]] = None,
                 keyword_searchable_job_custom_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input['CompanySize']] = None,
                 website_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new company entity.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] career_site_uri: Optional. The URI to employer's career site or careers page on the employer's web site, for example, "https://careers.google.com".
        :param pulumi.Input[str] display_name: The display name of the company, for example, "Google LLC".
        :param pulumi.Input[str] eeo_text: Optional. Equal Employment Opportunity legal disclaimer text to be associated with all jobs, and typically to be displayed in all roles. The maximum number of allowed characters is 500.
        :param pulumi.Input[str] external_id: Client side company identifier, used to uniquely identify the company. The maximum number of allowed characters is 255.
        :param pulumi.Input[str] headquarters_address: Optional. The street address of the company's main headquarters, which may be different from the job location. The service attempts to geolocate the provided address, and populates a more specific location wherever possible in DerivedInfo.headquarters_location.
        :param pulumi.Input[bool] hiring_agency: Optional. Set to true if it is the hiring agency that post jobs for other employers. Defaults to false if not provided.
        :param pulumi.Input[str] image_uri: Optional. A URI that hosts the employer's company logo.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] keyword_searchable_job_custom_attributes: Optional. A list of keys of filterable Job.custom_attributes, whose corresponding `string_values` are used in keyword search. Jobs with `string_values` under these specified field keys are returned if any of the values matches the search keyword. Custom field values with parenthesis, brackets and special symbols won't be properly searchable, and those keyword queries need to be surrounded by quotes.
        :param pulumi.Input[str] name: Required during company update. The resource name for a company. This is generated by the service when a company is created. The format is "projects/{project_id}/companies/{company_id}", for example, "projects/api-test-project/companies/foo".
        :param pulumi.Input['CompanySize'] size: Optional. The employer's company size.
        :param pulumi.Input[str] website_uri: Optional. The URI representing the company's primary web site or home page, for example, "https://www.google.com". The maximum number of allowed characters is 255.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CompanyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new company entity.

        :param str resource_name: The name of the resource.
        :param CompanyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CompanyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 career_site_uri: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 eeo_text: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 headquarters_address: Optional[pulumi.Input[str]] = None,
                 hiring_agency: Optional[pulumi.Input[bool]] = None,
                 image_uri: Optional[pulumi.Input[str]] = None,
                 keyword_searchable_job_custom_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input['CompanySize']] = None,
                 website_uri: Optional[pulumi.Input[str]] = None,
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
            __props__ = CompanyArgs.__new__(CompanyArgs)

            __props__.__dict__["career_site_uri"] = career_site_uri
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["eeo_text"] = eeo_text
            if external_id is None and not opts.urn:
                raise TypeError("Missing required property 'external_id'")
            __props__.__dict__["external_id"] = external_id
            __props__.__dict__["headquarters_address"] = headquarters_address
            __props__.__dict__["hiring_agency"] = hiring_agency
            __props__.__dict__["image_uri"] = image_uri
            __props__.__dict__["keyword_searchable_job_custom_attributes"] = keyword_searchable_job_custom_attributes
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["size"] = size
            __props__.__dict__["website_uri"] = website_uri
            __props__.__dict__["derived_info"] = None
            __props__.__dict__["suspended"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Company, __self__).__init__(
            'google-native:jobs/v3:Company',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Company':
        """
        Get an existing Company resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CompanyArgs.__new__(CompanyArgs)

        __props__.__dict__["career_site_uri"] = None
        __props__.__dict__["derived_info"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["eeo_text"] = None
        __props__.__dict__["external_id"] = None
        __props__.__dict__["headquarters_address"] = None
        __props__.__dict__["hiring_agency"] = None
        __props__.__dict__["image_uri"] = None
        __props__.__dict__["keyword_searchable_job_custom_attributes"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["size"] = None
        __props__.__dict__["suspended"] = None
        __props__.__dict__["website_uri"] = None
        return Company(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="careerSiteUri")
    def career_site_uri(self) -> pulumi.Output[str]:
        """
        Optional. The URI to employer's career site or careers page on the employer's web site, for example, "https://careers.google.com".
        """
        return pulumi.get(self, "career_site_uri")

    @property
    @pulumi.getter(name="derivedInfo")
    def derived_info(self) -> pulumi.Output['outputs.CompanyDerivedInfoResponse']:
        """
        Derived details about the company.
        """
        return pulumi.get(self, "derived_info")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the company, for example, "Google LLC".
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="eeoText")
    def eeo_text(self) -> pulumi.Output[str]:
        """
        Optional. Equal Employment Opportunity legal disclaimer text to be associated with all jobs, and typically to be displayed in all roles. The maximum number of allowed characters is 500.
        """
        return pulumi.get(self, "eeo_text")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[str]:
        """
        Client side company identifier, used to uniquely identify the company. The maximum number of allowed characters is 255.
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="headquartersAddress")
    def headquarters_address(self) -> pulumi.Output[str]:
        """
        Optional. The street address of the company's main headquarters, which may be different from the job location. The service attempts to geolocate the provided address, and populates a more specific location wherever possible in DerivedInfo.headquarters_location.
        """
        return pulumi.get(self, "headquarters_address")

    @property
    @pulumi.getter(name="hiringAgency")
    def hiring_agency(self) -> pulumi.Output[bool]:
        """
        Optional. Set to true if it is the hiring agency that post jobs for other employers. Defaults to false if not provided.
        """
        return pulumi.get(self, "hiring_agency")

    @property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> pulumi.Output[str]:
        """
        Optional. A URI that hosts the employer's company logo.
        """
        return pulumi.get(self, "image_uri")

    @property
    @pulumi.getter(name="keywordSearchableJobCustomAttributes")
    def keyword_searchable_job_custom_attributes(self) -> pulumi.Output[Sequence[str]]:
        """
        Optional. A list of keys of filterable Job.custom_attributes, whose corresponding `string_values` are used in keyword search. Jobs with `string_values` under these specified field keys are returned if any of the values matches the search keyword. Custom field values with parenthesis, brackets and special symbols won't be properly searchable, and those keyword queries need to be surrounded by quotes.
        """
        return pulumi.get(self, "keyword_searchable_job_custom_attributes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Required during company update. The resource name for a company. This is generated by the service when a company is created. The format is "projects/{project_id}/companies/{company_id}", for example, "projects/api-test-project/companies/foo".
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[str]:
        """
        Optional. The employer's company size.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def suspended(self) -> pulumi.Output[bool]:
        """
        Indicates whether a company is flagged to be suspended from public availability by the service when job content appears suspicious, abusive, or spammy.
        """
        return pulumi.get(self, "suspended")

    @property
    @pulumi.getter(name="websiteUri")
    def website_uri(self) -> pulumi.Output[str]:
        """
        Optional. The URI representing the company's primary web site or home page, for example, "https://www.google.com". The maximum number of allowed characters is 255.
        """
        return pulumi.get(self, "website_uri")

