# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0002_auto_20150908_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='employee',
        ),
    ]
