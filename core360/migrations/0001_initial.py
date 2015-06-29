# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('boss', models.ForeignKey(related_name='employee_boss', blank=True, to='core360.Employee', help_text=b'Respons\xc3\xa1vel', null=True)),
                ('department', models.ForeignKey(to='core360.Department')),
            ],
            options={
                'verbose_name': 'Funcion\xe1rio',
                'verbose_name_plural': 'Funcion\xe1rios',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_date', models.DateField()),
                ('employee_assessed', models.ForeignKey(to='core360.Employee')),
                ('person_will_answer_form', models.ForeignKey(related_name='avaliador', to='core360.Employee')),
            ],
            options={
                'verbose_name': 'Avalia\xe7\xe3o',
                'verbose_name_plural': 'Avalia\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Op\xe7ao',
                'verbose_name_plural': 'Op\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500)),
                ('options', models.ManyToManyField(to='core360.Options')),
            ],
            options={
                'verbose_name': 'Quest\xe3o',
                'verbose_name_plural': 'Quest\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('registration_date', models.DateField()),
                ('description_of_work', models.TextField(max_length=500, null=True, blank=True)),
                ('employee', models.ManyToManyField(related_name='Avaliado', to='core360.Employee')),
            ],
            options={
                'verbose_name': 'Question\xe1rio',
                'verbose_name_plural': 'Question\xe1rios',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(to='core360.Quiz'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='quiz',
            field=models.ForeignKey(to='core360.Quiz'),
        ),
        migrations.AddField(
            model_name='employee',
            name='office',
            field=models.ForeignKey(to='core360.Office'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
