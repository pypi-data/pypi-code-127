# Generated by Django 2.2.16 on 2021-03-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_flow', '0049_projectfavourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='disciplines',
            field=models.ManyToManyField(blank=True, to='course_flow.Discipline'),
        ),
    ]
