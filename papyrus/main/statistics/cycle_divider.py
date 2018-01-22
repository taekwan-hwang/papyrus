from main.models import Test, Time, VarianceInCycle
from django.db import connection
from django.db import models
from main.util.query import custom_sql

def get_by_cycle(n):#싸이클별로 데이터 모아주는 코드, cycle이 정해질 때 해당 사이클이 존재하는 환자들의 모든 데이터를 가져옴
    all=Test.objects.all().order_by('pi')
    reg_nums=[]
    objs=[]
    return_obj=[]
    for i in all:
        if not i.reg_num in reg_nums:
            reg_nums.append(i.reg_num)
    for i in reg_nums:
        objs.append(Test.objects.filter(pi=i).order_by('hpday'))#[[],[],[],[]]
    temp=[]
    for i in objs:
        tmp=[]
        for j in i:
            flag=True
            for k in tmp:
                if j.hpday == k.hpday:
                    flag=False
            if flag:
                tmp.append(j)
        temp.append(tmp)

    for i in temp:
        if len(i)<n:#i[n] == undefined:
            continue
        else:
            return_obj.append(i[n-1])

    return return_obj

def get_cycle_by_person(pi):#환자번호를 넣으면 해당 환자가 몇 번째 입원인지 알 수 있음
    return custom_sql("select count(distinct 입원일자) from TEST where 등록번호={}".format(pi))[0][0]

def mean_pain_variance_by_cycle(cycle):
    import statistics
    obj_all=VarianceInCycle.objects.all()
    variances=[]
    for obj in obj_all:
        if cycle==1:
            var=obj.var_cycle_1
            if var is not None:
                variances.append(obj.var_cycle_1)
        elif cycle==2:
            var=obj.var_cycle_2
            if var is not None:
                variances.append(obj.var_cycle_2)
        elif cycle==3:
            var=obj.var_cycle_3
            if var is not None:
                variances.append(obj.var_cycle_3)
        else :
            raise ValueError("cycle out of range")
    return statistics.mean(variances)
