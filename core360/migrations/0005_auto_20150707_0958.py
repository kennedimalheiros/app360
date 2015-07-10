# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0004_auto_20150630_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='person_will_answer_form',
            field=models.ForeignKey(to='core360.Employee', help_text='Avaliador.', related_name='avaliador'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='quiz',
            field=models.ForeignKey(to='core360.Quiz', help_text='Questionário que será aplicado.'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description_of_work',
            field=models.TextField(max_length=500, blank=True, null=True, help_text='Descrição do Questionário.'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='employee',
            field=models.ManyToManyField(to='core360.Employee', related_name='Avaliado', help_text='Funcionário que vai participar deste questionário.'),
        ),
    ]
