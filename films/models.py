# from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.db import models
# from redactor.fields import RedactorField
import datetime
import PIL
from PIL import Image


class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    name = models.CharField(max_length=30, unique=True, verbose_name='Название', db_index=True)

    def save(self, *args, **kwargs):
        super(Genre, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Genre, self).delete(*args, **kwargs)

    class Meta:
        ordering = ['name']
        unique_together = ('id_genre', 'name')
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

class Film(models.Model):
    id_film = models.AutoField(primary_key=True, unique=True, verbose_name='id')

    name = models.CharField(max_length=60, verbose_name='Название', db_index=True)
    photo = models.ImageField(upload_to="uploads/", verbose_name='Плашка', blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    annotation = models.TextField(verbose_name='Аннотация', null=True, blank=True)

    orig_name = models.CharField(max_length=60, verbose_name='Оригинальное название')
    year = models.CharField(max_length=20, verbose_name='Год', db_index=True)
    country = models.TextField(verbose_name='Страна')
    tagline = models.CharField(max_length=100, verbose_name='Слоган')
    producer = models.CharField(max_length=100, verbose_name='Режиссер')

    genre = models.ForeignKey(Genre, verbose_name='Жанр', on_delete=models.SET_NULL, null=True, blank=True)

    time = models.CharField(max_length=8, verbose_name='Время')
    cycle = models.CharField(max_length=100, verbose_name='Цикл')
    language = models.TextField(verbose_name='Языки', null=True, blank=True)
    artists = models.TextField(verbose_name='Актеры', null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Film, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Film, self).delete(*args, **kwargs)

    class Meta:
        ordering = ['name']
        unique_together = ('id_film', 'name')
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name + " " + self.year

    # @property
    # def gen_name(self):
    #     return self.genre.name

