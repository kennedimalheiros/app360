# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0005_auto_20150908_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='description',
            field=models.CharField(verbose_name='Descrição', max_length=100),
        ),
    ]
