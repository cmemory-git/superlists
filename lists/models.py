from django.db import models
from django.template.defaultfilters import default

# Create your models here.
class Item(models.Model):
    text = models.TextField(default = '')