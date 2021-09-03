from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=60,unique=True)
    director = models.CharField(max_length=60)
    studio = models.CharField(max_length=30)
    platform = models.CharField(max_length=30)
    year = models.PositiveIntegerField(blank=True, null=True)

    manager = models.Manager()

    def __str__(self):
        return self.title

