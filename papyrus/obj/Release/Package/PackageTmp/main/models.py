from django.db import models

# Create your models here.

class test2(models.Model):
    reg_num=models.BigIntegerField(db_column='등록번호')
    date=models.IntegerField(db_column='재원일수')