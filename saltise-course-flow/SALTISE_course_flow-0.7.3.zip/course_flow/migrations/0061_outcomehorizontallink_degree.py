# Generated by Django 2.2.20 on 2021-07-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_flow', '0060_auto_20210621_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='outcomehorizontallink',
            name='degree',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
