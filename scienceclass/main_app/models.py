from django.db import models
from django.urls import reverse

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class scienceclass(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="scienceclass")
    topic = models.CharField(max_length=200)
    labs = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('detail', kwargs={'scienceclass_id': self.id})
