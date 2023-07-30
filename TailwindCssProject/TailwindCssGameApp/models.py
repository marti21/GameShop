from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=120, default="")
    description = models.TextField(default="")
    score = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    image = models.ImageField(upload_to='gameImages', blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)


class UserActualized(User):
    image = models.ImageField(upload_to='userImages', blank=True)