from django.db import models

# Create your models here.
class Song(models.Model):
    song_title = models.CharField(max_length=100)
    album = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    audio = models.FileField(default='')

    def __str__(self):
        return self.song_title


