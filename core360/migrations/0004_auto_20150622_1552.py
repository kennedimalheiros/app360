# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0003_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('boss', models.IntegerField()),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('department', models.ForeignKey(to='core360.Department')),
            ],
        ),
        migrations.RenameModel(
            old_name='Cargo',
            new_name='Office',
        ),
        migrations.AddField(
            model_name='employee',
            name='office',
            field=models.ForeignKey(to='core360.Office'),
        ),
    ]
