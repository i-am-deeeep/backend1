from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class Show(models.Model):

    CATEGORY_CHOICES = [
        ('ACT', 'Action'),
        ('COM', 'Comedy'),
        ('DRA', 'Drama'),
        ('THR', 'Thriller'),
        ('HOR', 'Horror'),
        ('ROM', 'Romance'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='shows')

    def __str__(self):
        return self.title
