from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=10,default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.email


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=50)
    phone=models.CharField(max_length=11)

    def __str__(self):
        return self.email
