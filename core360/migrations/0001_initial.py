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
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('boss', models.ForeignKey(help_text='Responsável', blank=True, related_name='employee_boss', to='core360.Employee', null=True)),
                ('department', models.ForeignKey(to='core360.Department')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('registration_date', models.DateField()),
                ('employee_assessed', models.ForeignKey(help_text='Funcionários que será avaliado.', to='core360.Employee')),
                ('person_will_answer_form', models.ForeignKey(help_text='Avaliador.', related_name='avaliador', to='core360.Employee')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Opçao',
                'verbose_name_plural': 'Opções',
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
                'verbose_name': 'Questão',
                'verbose_name_plural': 'Questões',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('registration_date', models.DateField()),
                ('employee', models.ManyToManyField(help_text='Funcionário que vai participar deste questionário.', to='core360.Employee', related_name='Avaliado')),
            ],
            options={
                'verbose_name': 'Questionário',
                'verbose_name_plural': 'Questionários',
            },
        ),
        migrations.AddField(
            model_name='evaluation',
            name='questions',
            field=models.ManyToManyField(to='core360.Question'),
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
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, to='core360.Options'),
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
