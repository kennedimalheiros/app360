# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0012_auto_20150622_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='department',
            name='phone',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
