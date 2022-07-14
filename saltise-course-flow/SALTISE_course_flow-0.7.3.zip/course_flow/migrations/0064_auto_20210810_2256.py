# Generated by Django 2.2.20 on 2021-08-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course_flow", "0063_auto_20210728_2238"),
    ]

    operations = [
        migrations.AddField(
            model_name="outcome",
            name="code",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="outcome",
            name="description",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="outcome",
            name="title",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
