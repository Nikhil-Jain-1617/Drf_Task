from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_id = models.IntegerField()
    product_price = models.IntegerField()
    product_model = models.CharField(max_length=20)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name