# Generated by Django 2.0.2 on 2018-03-13 17:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 13, 17, 40, 26, 875923, tzinfo=utc)),
        ),
    ]
