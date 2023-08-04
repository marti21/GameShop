from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File

class UserActualized(User):
    image = models.ImageField(upload_to='userImages', blank=True)

def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=1) 
    new_image = File(im_io, name=image.name)
    return new_image

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=120, default="")
    description = models.TextField(default="")
    score = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    image = models.ImageField(upload_to='gameImages', blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    trend = models.BooleanField(default=False)

    #calling image compression function before saving the data
    def save(self, *args, **kwargs):
                new_image = compress(self.image)
                self.image = new_image
                super().save(*args, **kwargs)