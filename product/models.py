from django.db import models

# Create your models here.

# 사진, 상품명, 가격, 설명
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="images/", blank=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)


