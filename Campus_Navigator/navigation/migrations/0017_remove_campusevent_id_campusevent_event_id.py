# Generated by Django 4.2.5 on 2023-12-06 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0016_remove_campusevent_event_id_campusevent_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campusevent',
            name='id',
        ),
        migrations.AddField(
            model_name='campusevent',
            name='event_id',
            field=models.AutoField(default='0', primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
