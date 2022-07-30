from django.db import models
from store.utils.models import BaseModel

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    class Meta:
        app_label = "products"

    def __str__(self):  
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=255)
    descrption = models.TextField(max_length=500, blank=True, null=True)
    price = models.IntegerField(default=0)
    photo = models.ImageField()
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name