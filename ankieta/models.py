# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
# Create your models here.


class Pytanie(models.Model):
    text_pytania = models.CharField(max_length=200)
    data_publikacji = models.DateTimeField(default=now, editable=False)

    def siemanko(self):
        return 'Siemanko z pytania nr : {}'.format(self.id)

    def __str__(self):
        return self.text_pytania

    class Meta:
        ordering = (['-data_publikacji'])

    def __unicode__(self):
        return unicode(self.text_pytania)


class Odpowiedz(models.Model):
    pytanie = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    odpowiedz = models.CharField(max_length=200)
    glosy = models.IntegerField(default=0)

    def __str__(self):
        return self.odpowiedz
