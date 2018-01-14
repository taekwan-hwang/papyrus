from django.db import models

# Create your models here.
'''
class tong6(models.Model):
    reg_num=models.BigIntegerField(db_column='등록번호', primary_key=True)
    date=models.DateField(db_column='기록실시일자')
    datetime=models.DateTimeField(db_column='기록실시일시')
    look_code=models.CharField(max_length=20, db_column='임상관찰코드')
    look_codeNM=models.CharField(max_length=50, db_column='임상관찰코드NM')
    source=models.CharField(max_length=50, db_column='측정값_Source')
    numeric=models.FloatField(db_column='측정값_Numeric')
    
    class Meta:
        db_table = 'TB_TONG_6'
        managed=False
'''
class Final2(models.Model):
    reg_num=models.BigIntegerField(db_column='등록번호', primary_key=True)
    hp_day=models.DateField(db_column='입원일자')
    hl=models.CharField(max_length=5, db_column='HL')

    class Meta:
        db_table='final2'
        managed=False

class Hpday(models.Model):
    pi=models.BigIntegerField(db_column='PI', primary_key=True)
    hpday2=models.DateField(db_column='Hpday2')

    class Meta:
        db_table='Hpday'
        managed=False

class Test(models.Model):
    reg_num=models.BigIntegerField(db_column='등록번호', primary_key=True)
    hp_day=models.DateField(db_column='입원일자')
    sex=models.CharField(max_length=1, db_column='성별')
    age=models.IntegerField(db_column='나이')
    height=models.FloatField(db_column='신장')
    weight=models.FloatField(db_column='현재체중')
    bmi_data=models.FloatField(db_column='BMI_data')
    adl=models.CharField(db_column='ADL', max_length=50)
    albumin_data=models.FloatField(db_column='Albumin_data')
    neutrophil=models.FloatField(db_column='Neutrophil')
    crp=models.FloatField(db_column='CRP')
    plt=models.FloatField(db_column='PLT')
    hg=models.FloatField(db_column='HG')
    ht=models.FloatField(db_column='HT')
    tbc=models.FloatField(db_column='TBC')
    dm=models.FloatField(db_column='DM')
    hp=models.FloatField(db_column='HP')
    d1=models.FloatField(db_column='D1')
    d2=models.FloatField(db_column='D2')
    d3=models.FloatField(db_column='D3')
    d4=models.FloatField(db_column='D4')
    d5=models.FloatField(db_column='D5')
    d6=models.FloatField(db_column='D6')
    d7=models.FloatField(db_column='D7')
    d8=models.FloatField(db_column='D8')
    d9=models.FloatField(db_column='D9')
    d10=models.FloatField(db_column='D10')
    y=models.CharField(max_length=1, db_column='y')
    isSmoking=models.CharField(max_length=1, db_column='흡연여부')
    isDrinking=models.CharField(max_length=1, db_column='음주여부')
    exercise_hour=models.CharField(max_length=1, db_column='운동시간')
    exercise_num=models.CharField(max_length=1, db_column='운동횟수')
    pain_score=models.FloatField(db_column='통증점수')
    weight_variant=models.CharField(max_length=1, db_column='체중변화')
    class Meta:
        managed=False
        db_table='TEST'

class Time(models.Model):
    pi=models.BigIntegerField(primary_key=True, db_column='PI')
    hpday=models.DateField(db_column='Hpday')
    hptime=models.DateTimeField(db_column='HPtime')
    pain=models.CharField(max_length=200, db_column='Pain')
    class Meta:
        managed=False
        db_table='Time'