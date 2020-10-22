from django.db import models

# Create your models here.
# Database is like excel workbook
# Models--> Table --> Sheet

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=13)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(blank=True)


    def __str__(self):
        return 'Title by : ' + self.author