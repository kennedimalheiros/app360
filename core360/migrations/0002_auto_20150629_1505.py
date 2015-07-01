# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name': 'Cargo', 'verbose_name_plural': 'Cargos'},
        ),
    ]
