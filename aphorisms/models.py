from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag

# Create your models here.


class Aphorism(models.Model):
    text = models.CharField(max_length=1000, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

