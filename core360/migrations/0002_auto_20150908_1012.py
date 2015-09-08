# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='questions',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='quiz',
            field=models.ForeignKey(to='core360.Quiz', default=2, help_text='Questionário que será aplicado.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='question',
            field=models.ManyToManyField(to='core360.Question', related_name='questionario_questao'),
        ),
    ]
