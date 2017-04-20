# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id_film', models.AutoField(verbose_name='id', primary_key=True, unique=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', max_length=60, db_index=True)),
                ('annotation', models.TextField(verbose_name='Аннотация', blank=True, null=True)),
                ('orig_name', models.CharField(verbose_name='Оригинальное название', max_length=60)),
                ('year', models.CharField(verbose_name='Дата', max_length=20, db_index=True)),
                ('country', models.TextField(verbose_name='Страна')),
                ('tagline', models.CharField(verbose_name='Слоган', max_length=100)),
                ('producer', models.CharField(verbose_name='Режиссер', max_length=100)),
                ('time', models.CharField(verbose_name='Время', max_length=8)),
                ('cycle', models.CharField(verbose_name='Цикл', max_length=100)),
                ('language', models.TextField(verbose_name='Языки', blank=True, null=True)),
                ('artists', models.TextField(verbose_name='Актеры', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id_genre', models.AutoField(verbose_name='id', primary_key=True, unique=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название', max_length=30, unique=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='genre',
            unique_together=set([('id_genre', 'name')]),
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(verbose_name='Жанр', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='films.Genre'),
        ),
        migrations.AlterUniqueTogether(
            name='film',
            unique_together=set([('id_film', 'name')]),
        ),
    ]
