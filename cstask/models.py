from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    name        = models.CharField(max_length=15)
    created_at  = models.DateTimeField(auto_now_add=True)
    owner       = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Entry(models.Model):
    text     = models.CharField(max_length=200)
    topic    = models.ForeignKey(Topic,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Entries'
    def __str__(self):
        return self.text[:50]+'......'
