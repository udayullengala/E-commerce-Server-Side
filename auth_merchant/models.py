from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=50)

class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)