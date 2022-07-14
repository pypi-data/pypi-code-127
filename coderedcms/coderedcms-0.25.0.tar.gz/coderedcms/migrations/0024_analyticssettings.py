# Generated by Django 3.2.7 on 2021-09-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderedcms', '0023_auto_20210908_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyticssettings',
            name='ga_g_tracking_id',
            field=models.CharField(blank=True, help_text='Your Google Analytics 4 tracking ID (begins with "G-")', max_length=255, verbose_name='G Tracking ID'),
        ),
        migrations.AddField(
            model_name='analyticssettings',
            name='gtm_id',
            field=models.CharField(blank=True, help_text='Begins with "GTM-"', max_length=255, verbose_name='Google Tag Manager ID'),
        ),
        migrations.AlterField(
            model_name='analyticssettings',
            name='ga_tracking_id',
            field=models.CharField(blank=True, help_text='Your Google "Universal Analytics" tracking ID (begins with "UA-")', max_length=255, verbose_name='UA Tracking ID'),
        ),
    ]
