# Generated by Django 3.0.9 on 2020-08-29 21:23

import coderedcms.blocks.base_blocks
import coderedcms.blocks.html_blocks
import coderedcms.fields
from django.db import migrations, models
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('coderedcms', '0018_auto_20200805_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coderedpage',
            name='struct_org_address_country',
            field=models.CharField(blank=True, help_text='For example, USA. Two-letter ISO 3166-1 alpha-2 country code is also acceptable https://en.wikipedia.org/wiki/ISO_3166-1', max_length=255, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='contentwall',
            name='content',
            field=coderedcms.fields.CoderedStreamField([], blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='content',
            field=coderedcms.fields.CoderedStreamField([], blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='reusablecontent',
            name='content',
            field=coderedcms.fields.CoderedStreamField([], blank=True, verbose_name='content'),
        ),
    ]
