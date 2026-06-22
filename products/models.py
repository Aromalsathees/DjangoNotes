from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    desc = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)   # datetime automatically

    def __str__(self):
        return self.category_name

class Add_Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True) #makes the field snullable
    product_name = models.CharField(max_length=30)
    product_desc = models.TextField(max_length=100)
    product_price = models.IntegerField()
    product_old_price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    image = models.ImageField(upload_to='photes/product_images',null=True, blank=True)

    def __str__(self):
        return self.product_name


# on_delete=models.CASCADE   when its primary key is deleted its foregin will delette automatically
    


# decimal value use cases 

# product price 
# salary 
# account balance 
# discount