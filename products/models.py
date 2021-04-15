from django.db import models

# Create your models here.
class Product (models.Model):
    title=models.CharField(max_length=120)
    price=models.DecimalField(decimal_places=2, max_digits=10000)
    description=models.TextField(null=True)
    summary=models.TextField(default="Summary")

    #def__str__(self):
     #  return self.title

