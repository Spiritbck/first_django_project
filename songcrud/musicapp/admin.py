from django.contrib import admin
from .models import Artist, Lyrics, Song

# Register your models here.

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Lyrics)