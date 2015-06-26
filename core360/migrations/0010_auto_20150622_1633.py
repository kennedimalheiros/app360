# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0009_auto_20150622_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='boss',
        ),
        migrations.AddField(
            model_name='employee',
            name='boss',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
