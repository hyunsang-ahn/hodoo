from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=30)
    poster_path = models.CharField(max_length=140)
    overview = models.TextField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Score(models.Model):
    content =  models.CharField(max_length=140)
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)