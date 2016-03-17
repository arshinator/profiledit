from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=255)
    pan = models.TextField()
    slug = models.SlugField(unique=True)
    # adding this line so the user can own thing
    user = models.OneToOneField(User, blank=True, null=True)
