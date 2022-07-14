# Generated by Django 2.2.20 on 2021-04-24 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("user_feedback", "0003_feedback_archived")]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="archived",
            field=models.BooleanField(
                default=False,
                help_text="Check to mark this comment as resolved.",
                verbose_name="archive status",
            ),
        )
    ]
