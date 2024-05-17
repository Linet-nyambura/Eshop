from django.db import models
from .models import Category #import category from models.py

#its a django model for products with fields for name,price, category, description and image
#also include staticmethos to retrieve the products by ID,
#retrieve all products and retrieve products by category ID
class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

@staticmethod
def get_products_by_id(ids):
    return Products.objects.filter(id_in=ids)
@staticmethod
def get_all_products():
    return Products.objects.all()
@staticmethod
def get_all_products_by_category(category_id):
    if category_id:
        return Products.objects.filter(category=category_id)
    else:
        return Products.get_all_products()
