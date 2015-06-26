# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0004_auto_20150622_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='boss',
        ),
        migrations.AddField(
            model_name='employee',
            name='boss',
            field=models.ManyToManyField(related_name='boss_rel_+', to='core360.Employee'),
        ),
    ]
