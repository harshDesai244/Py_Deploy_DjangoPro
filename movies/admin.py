from csv import list_dialects
from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_createrd',)
    list_display = ('title', 'reales_date',
                    'number_in_stock', 'daily_rate', 'genre')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
