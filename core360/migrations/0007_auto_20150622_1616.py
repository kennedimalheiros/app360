# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0006_auto_20150622_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='boss',
            field=models.ManyToManyField(related_name='boss_rel_+', to='core360.Employee'),
        ),
    ]
