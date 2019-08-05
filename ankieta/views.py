# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Pytanie

from django.template import loader

# Create your views here.


def index(request):
    pytania_od_najnowszego = Pytanie.objects.order_by('data_publikacji')[:5]
    # return HttpResponse(', '.join([p.text_pytania for p in pytania_od_najnowszego]))
    template = loader.get_template('ankieta/index.html')
    context = {
        'lista_pytan': pytania_od_najnowszego
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse('Szukasz pytania z id %s' % question_id)


def results(request, question_id):
    response = 'Szukasz rezultatu pytania z id %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('Głosujesz na pytanie z id %s' % question_id)
