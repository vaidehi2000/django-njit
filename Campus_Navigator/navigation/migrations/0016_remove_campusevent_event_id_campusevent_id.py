# Generated by Django 4.2.5 on 2023-12-06 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0015_remove_campusevent_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campusevent',
            name='event_id',
        ),
        migrations.AddField(
            model_name='campusevent',
            name='id',
            field=models.BigAutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
