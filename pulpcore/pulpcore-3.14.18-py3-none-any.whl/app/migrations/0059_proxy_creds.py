# Generated by Django 2.2.18 on 2021-03-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_accesspolicy_customized'),
    ]

    operations = [
        migrations.AddField(
            model_name='remote',
            name='proxy_password',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='remote',
            name='proxy_username',
            field=models.TextField(null=True),
        ),
    ]
