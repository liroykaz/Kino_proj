# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_film_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='annotation',
            field=models.TextField(verbose_name='Аннотация', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.CharField(verbose_name='Год', max_length=20, db_index=True),
        ),
    ]
