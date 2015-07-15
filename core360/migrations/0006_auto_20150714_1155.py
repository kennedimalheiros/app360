# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0005_auto_20150707_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('answer', models.ForeignKey(blank=True, to='core360.Options', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='description_of_work',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='finalize',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='answer',
            name='evaluation',
            field=models.ForeignKey(to='core360.Evaluation'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='core360.Question'),
        ),
    ]
