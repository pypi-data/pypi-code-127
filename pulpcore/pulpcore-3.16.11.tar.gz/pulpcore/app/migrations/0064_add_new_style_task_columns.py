# Generated by Django 2.2.20 on 2021-04-27 07:51

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models

TASK_BATCH_SIZE = 1000


def copy_reserved_resources_record(apps, schema_editor):
    Task = apps.get_model('core', 'Task')

    # Update _reserved_resource_record for all tasks, 1000 tasks at a time.
    # When we hit 1K tasks, go to the db for the batch.
    # Make sure to update the final batch!
    tasks = []
    for task in Task.objects.iterator(chunk_size=TASK_BATCH_SIZE):
        task._reserved_resources_record = list(task.reserved_resources_record.values_list('resource', flat=True))
        tasks.append(task)
        if len(tasks) == TASK_BATCH_SIZE:
            Task.objects.bulk_update(tasks, ["_reserved_resources_record"])
            tasks.clear()

    # Update last set of tasks
    if len(tasks) > 0:
        Task.objects.bulk_update(tasks, ["_reserved_resources_record"])


def purge_reservedresources(apps, schema_editor):
    TaskReservedResource = apps.get_model('core', 'TaskReservedResource')
    TaskReservedResource.objects.all().delete()

    ReservedResource = apps.get_model('core', 'ReservedResource')
    ReservedResource.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_repository_retained_versions'),
    ]

    operations = [
        # Purge any ReservedResource entries - if there are any, they're orphans
        migrations.RunPython(
            code=purge_reservedresources,
            reverse_code=migrations.RunPython.noop,
        ),
        # Update entities for the new task-system
        migrations.AddField(
            model_name='task',
            name='args',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='kwargs',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='_reserved_resources_record',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='task',
            name='_resource_job_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='progressreport',
            name='state',
            field=models.TextField(choices=[('waiting', 'Waiting'), ('skipped', 'Skipped'), ('running', 'Running'), ('completed', 'Completed'), ('failed', 'Failed'), ('canceled', 'Canceled'), ('canceling', 'Canceling')], default='waiting'),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.TextField(choices=[('waiting', 'Waiting'), ('skipped', 'Skipped'), ('running', 'Running'), ('completed', 'Completed'), ('failed', 'Failed'), ('canceled', 'Canceled'), ('canceling', 'Canceling')]),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['pulp_created'], name='core_task_pulp_cr_10223f_idx'),
        ),
        migrations.RunPython(
            code=copy_reserved_resources_record,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RemoveField(
            model_name='taskreservedresourcerecord',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='taskreservedresourcerecord',
            name='task',
        ),
        migrations.DeleteModel(
            name='ReservedResourceRecord',
        ),
        migrations.DeleteModel(
            name='TaskReservedResourceRecord',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='_reserved_resources_record',
            new_name='reserved_resources_record',
        ),

    ]
