# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0007_auto_20150928_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='quiz',
            field=models.ForeignKey(to='core360.Quiz', help_text='Questionário que será aplicado.', verbose_name='Questionário'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='registration_date',
            field=models.DateField(verbose_name='Data Cadastro'),
        ),
        migrations.AlterField(
            model_name='question',
            name='options',
            field=models.ManyToManyField(verbose_name='Opções', to='core360.Options'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(verbose_name='Texto', max_length=500),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.ManyToManyField(verbose_name='Questões', to='core360.Question', related_name='questionario_questao'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='registration_date',
            field=models.DateField(verbose_name='Data Criação'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(verbose_name='Titulo', max_length=40),
        ),
    ]
