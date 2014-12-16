# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('ciudad', models.CharField(default=b'', max_length=100)),
                ('fundacion', models.IntegerField()),
                ('entrenador', models.CharField(default=b'', unique=True, max_length=100)),
                ('historia', models.TextField(default=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(default=b'1970-01-01')),
                ('lugar_nacimiento', models.CharField(default=b'', max_length=100)),
                ('edad', models.IntegerField()),
                ('posicion', models.CharField(default=b'', max_length=100)),
                ('historial', models.TextField(default=b'', blank=True)),
                ('equipo', models.ForeignKey(blank=True, to='gestion_equipos.Equipo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
