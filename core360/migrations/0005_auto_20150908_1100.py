# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0004_auto_20150908_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='employee_assessed',
            field=models.ForeignKey(to='core360.Employee', help_text='Funcionários que será avaliado.', verbose_name='Avaliado'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='person_will_answer_form',
            field=models.ForeignKey(to='core360.Employee', help_text='Avaliador.', related_name='avaliador', verbose_name='Avaliador'),
        ),
    ]
