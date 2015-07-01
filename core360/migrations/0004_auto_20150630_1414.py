# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0003_auto_20150629_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='boss',
            field=models.ForeignKey(help_text='Responsável', to='core360.Employee', blank=True, related_name='employee_boss', null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='employee_assessed',
            field=models.ForeignKey(help_text='Funcionários que será avaliado.', to='core360.Employee'),
        ),
    ]
