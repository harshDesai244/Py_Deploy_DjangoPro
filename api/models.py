from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resorce_name = 'movies'
        exclude = ['date_created']
