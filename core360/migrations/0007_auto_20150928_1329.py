# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0006_auto_20150908_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='boss',
            field=models.ForeignKey(help_text='Responsável (opcional)', verbose_name='Responsável', to='core360.Employee', related_name='employee_boss', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(to='core360.Department', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='office',
            field=models.ForeignKey(to='core360.Office', verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
