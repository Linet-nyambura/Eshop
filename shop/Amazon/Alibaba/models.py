from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
    
#customer.py with fiels for name,phone,email and password
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_lenght=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

#to save the data
def register(self):
    self.save()

@staticmethod
def get_customer_by_email(email):
    try:
        return Customer.objects.get(email=email)
    except:
        return False

def isExists(self):
    if Customer.objects.filter(email=self.email):
        return True
    
    return False
