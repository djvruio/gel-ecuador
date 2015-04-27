# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_sponsor'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(unique=True, max_length=50)),
                ('facilitador', models.CharField(max_length=50)),
                ('institucion', models.CharField(max_length=50)),
                ('objetivo', models.TextField(max_length=300)),
                ('req_tecnico', models.CharField(max_length=200)),
                ('req_logistico', models.CharField(max_length=200)),
                ('knowledgearea', models.ForeignKey(to='events.KnowledgeArea')),
                ('propuesto_por', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
