from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birthdate = models.DateField()


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="director")
    screenplay = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="screenplay")
    starring = models.ManyToManyField(Person, through='Role', null=True)
    release_date = models.DateField()
    rating = models.FloatField(null=True)
    genre = models.ManyToManyField(Genre)


class Role(models.Model):
    actor = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True)

