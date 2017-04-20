from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from films.models import *
from films.serializers import FilmsSerializer, GenSerializer


class FilmsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.all().order_by('name')
    serializer_class = FilmsSerializer


class GenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenSerializer

# Create your views here.
def index(request):
    films = Film.objects.order_by('name')
    return render(request, 'index.html', {'films': films})

# def rubs(request):
#     menus = Menu.objects.order_by('id_menu')
#     return render(request, 'rubs.html', {'menus': menus})
#
# def author(request):
#     menus = Menu.objects.order_by('id_menu')
#     return render(request, 'author.html', {'menus':menus})
#
def film(request, pk):
    film = Film.objects.get(pk=pk)
    return render(request, 'film.html', {'film': film})