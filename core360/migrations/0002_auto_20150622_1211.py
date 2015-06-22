# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core360', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='nome',
            new_name='name',
        ),
        migrations.AddField(
            model_name='cargo',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
