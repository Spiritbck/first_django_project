from ast import Delete
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Artist(models.Model):
    # Declearing database fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()


class Lyrics(models.Model):
    # many-to-one relation
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE ) 

    content = models.CharField(max_length=1000)
    song_id = models.AutoField(primary_key=True)


class Song(models.Model):
    # many-to-one relation
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE ) 

    
    # Declearing database fields
    title = models.CharField(max_length=30)
    artist_id = models.AutoField(primary_key=True)
    likes = models.IntegerField(default=0)
    date_released = models.DateTimeField('date released')
