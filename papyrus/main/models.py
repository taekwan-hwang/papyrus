from django.db import models

# Create your models here.

class tong6(models.Model):
    reg_num=models.BigIntegerField(db_column='등록번호')
    date=models.DateField('기록실시일자')
    datetime=models.DateTimeField(db_column='기록실시일시')
    look_code=models.CharField(max_length=20, db_column='임상관찰코드')
    look_codeNM=models.CharField(max_length=50, db_column='임상관찰코드NM')
    source=models.CharField(max_length=50, db_column='측정값_Source')
    numeric=models.FloatField(db_column='측정값_Numeric')
    
    class Meta:
        db_table = 'TB_TONG_6'
        managed=False