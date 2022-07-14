# Generated by Django 2.2.17 on 2020-11-18 09:41

from django.db import migrations


def namespace_access_policies_up(apps, schema_editor):
    AccessPolicy = apps.get_model('core', 'AccessPolicy')
    task_policy = AccessPolicy.objects.get(viewset_name="TaskViewSet")
    task_policy.viewset_name = "tasks"
    task_policy.save()


def namespace_access_policies_down(apps, schema_editor):
    AccessPolicy = apps.get_model('core', 'AccessPolicy')
    task_policy = AccessPolicy.objects.get(viewset_name="tasks").delete()
    task_policy.viewset_name = "TaskViewSet"
    task_policy.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_add_file_field_to_uploadchunk'),
    ]

    operations = [
        migrations.RunPython(namespace_access_policies_up, reverse_code=namespace_access_policies_down),
    ]
