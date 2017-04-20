from films.models import *
from rest_framework import serializers

class FilmsSerializer(serializers.HyperlinkedModelSerializer):
    gen_name = serializers.ReadOnlyField()
    class Meta:
        model = Film
        fields = ('id_film', 'name', 'photo', 'annotation', 'gen_name')

class GenSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = ('id_genre', 'name')