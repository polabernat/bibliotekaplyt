from django.db import models
import datetime

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)

    GENRES = [
        (-1, "not defined"),
        (0, "rock"),
        (1, "metal"),
        (2, "pop"),
        (3, "hip-hop"),
        (4, "electronic"),
        (5, "reggae"),
        (6, "other")
    ]

    genre = models.IntegerField(choices=GENRES, default=-1)

    import random

    def __repr__(self):
        return f'<Band: {self.name} ({self.id})>'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class Album(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField()
    RATINGS = [
        (0, 'unrated'),
        (1, "*"),
        (2, "**"),
        (3, "***"),
        (4, "****"),
        (5, "*****")
    ]
    rating = models.IntegerField(choices=RATINGS)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)

class Song(models.Model):
    title = models.CharField(max_length=128)
    duration = models.TimeField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    def __repr__(self):
        return f'<Article: {self.title})>'
    def __str__(self):
        return self.title
    band = models.ManyToManyField(Band)



class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    number_of_records = models.IntegerField

    year_of_birth = models.IntegerField(null=True)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class History(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField('date published')


