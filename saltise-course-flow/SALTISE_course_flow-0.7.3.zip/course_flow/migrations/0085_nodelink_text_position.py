# Generated by Django 2.2.25 on 2022-05-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course_flow", "0084_week_is_dropped"),
    ]

    operations = [
        migrations.AddField(
            model_name="nodelink",
            name="text_position",
            field=models.PositiveSmallIntegerField(default=20),
        ),
    ]
