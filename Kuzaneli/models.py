from django.db import models


# Create your models here.

class Catgory(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Picture(models.Model):
    title = models.CharField(max_length=64, db_column='name')
    overview = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    categories = models.ManyToManyField(Catgory)
    priority = models.BooleanField()
    VORH_CHOICE = (
        ('V', 'Vertical'),
        ('H', 'Horizontal')
    )
    vorh = models.CharField(max_length=1, choices=VORH_CHOICE, default=None)
    cart = models.BooleanField(default=False)

    def __str__(self):
        return self.title
