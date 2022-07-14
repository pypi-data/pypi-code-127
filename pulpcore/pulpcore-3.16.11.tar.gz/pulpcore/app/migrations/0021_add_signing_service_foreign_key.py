# Generated by Django 2.2.9 on 2020-01-30 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_change_publishedartifact_constraints'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsciiArmoredDetachedSigningService',
            fields=[
                ('signingservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.SigningService')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.signingservice',),
        ),
    ]
