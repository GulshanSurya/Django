#from os import name
from django.db import models

class Category(models.Model):    #category is a sub class of model class
    name = models.CharField(max_length=20)
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name #category ki list m category show hoga