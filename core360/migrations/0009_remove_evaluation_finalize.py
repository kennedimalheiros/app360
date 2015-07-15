# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0008_auto_20150714_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='finalize',
        ),
    ]
