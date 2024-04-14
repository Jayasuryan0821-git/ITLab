from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    num_visits = models.IntegerField()
    num_likes = models.IntegerField()

    def __str__(self):
        return self.name 

class Page(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    views = models.IntegerField()

    def __str__(self):
        return self.title
