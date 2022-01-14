from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="director")
    screenplay = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="screenplay")
    starring = models.ManyToManyField(Person, through='Role')
    release_date = models.DateField()
    rating = models.FloatField(null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Role(models.Model):
    actor = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True)

