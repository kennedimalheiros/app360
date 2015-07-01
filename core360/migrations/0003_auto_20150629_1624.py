# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0002_auto_20150629_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='employee_assessed',
            field=models.ForeignKey(help_text=b'Funcion\xc3\xa1rios que ser\xc3\xa1 avaliado.', to='core360.Employee'),
        ),
    ]
