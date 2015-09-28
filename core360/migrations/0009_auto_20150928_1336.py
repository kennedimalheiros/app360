# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0008_auto_20150928_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Descrição Opção'),
        ),
    ]
