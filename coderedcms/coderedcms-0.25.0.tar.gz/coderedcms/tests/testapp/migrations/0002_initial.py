
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import VERSION as DJANGO_VERSION
from django.db import migrations

from wagtail.core.models import Locale


def initial_data(apps, schema_editor):
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    WebPage = apps.get_model('testapp.WebPage')

    # Create page content type
    webpage_content_type, created = ContentType.objects.get_or_create(
        model='webpage',
        app_label='testapp',
    )

    # Delete the default home page generated by wagtail,
    # and replace it with a more useful page type.
    curr_homepage = Page.objects.filter(slug='home').delete()

    homepage = WebPage.objects.create(
        title = "Home",
        slug='home',
        custom_template='coderedcms/pages/home_page.html',
        content_type=webpage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/home/',
        locale_id=Locale.get_default().id,
    )

    # Create a new default site
    Site.objects.create(
        hostname='',
        site_name='Test Site',
        root_page_id=homepage.id,
        is_default_site=True
    )


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
        ('wagtailcore', '0002_initial_data'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
