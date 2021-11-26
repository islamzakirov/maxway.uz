from django.db import models


# Create your models here.
class Burger(models.Model):

    name = models.CharField(max_length=300, db_index=True)
    content = models.TextField()
    rasmi = models.ImageField()
    price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name