# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0007_evaluation_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='questions',
            field=models.ManyToManyField(to='core360.Question'),
        ),
    ]
