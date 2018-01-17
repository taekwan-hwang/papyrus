from main.models import Test, Time
from django.db import connection
from django.db import models
import gc
def custom_sql(query):
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    return row

def get_by_cycle(n):#싸이클별로 데이터 모아주는 코드
    all=Test.objects.all().order_by('reg_num')
    reg_nums=[]
    objs=[]
    return_obj=[]
    for i in all:
        if not i.reg_num in reg_nums:
            reg_nums.append(i.reg_num)
    for i in reg_nums:
        objs.append(Test.objects.filter(reg_num=i).order_by('hp_day'))#[[],[],[],[]]
    temp=[]
    for i in objs:
        tmp=[]
        for j in i:
            flag=True
            for k in tmp:
                if j.hp_day == k.hp_day:
                    flag=False
            if flag:
                tmp.append(j)
        temp.append(tmp)

    for i in temp:
        if len(i)<n:#i[n] == undifined:
            continue
        else:
            return_obj.append(i[n-1])

    return return_obj

def get_by_person(n):
    t=Time.objects.all().order_by('pi')
    pis=[]
    objs=[]
    return_obj=[]
    for i in t:
        if not i.pi in pis:
            pis.append(i.pi)
    for i in pis:
        tmp=[]
        hpdays=[]
        time=Time.objects.filter(pi=i).order_by('hptime')
        for j in time:
            if j.hpday in hpdays:
                tmp.append(j)
            elif len(hpdays)<n:#cycle수를 3까지, 그 외에는 생각하지 않음
                hpdays.append(j.hpday)
                tmp.append(j)
            else:
                break
        if len(hpdays)>=n:
            for j in tmp:
                if j.hpday==hpdays[n-1]:
                    objs.append(j)

    for i in objs:
        return_obj.append(i)
    return return_obj

def mean_pain_variance_by_cycle(cycle):
    import statistics
    
    variances=[]
    pis= [i[0] for i in custom_sql('SELECT DISTINCT PI FROM Time order by PI')]
    for i in pis:
        gc.collect()
        hpdays=[]
        count=0
        time=custom_sql('SELECT Hpday FROM Time where PI={} order by Hpday'.format(i))
        #time=Time.objects.filter(pi=i).order_by('hptime')
        for j in time:
            gc.collect()
            hpday=j[0]
            if count<cycle and not hpday in hpdays:
                hpdays.append(hpday)
                count+=1
            if count>=cycle:
                break
        if count<cycle:
            continue
        pains=[]
        tmp_arr=str(hpdays[cycle-1]).split('-')
        day=''
        for j in tmp_arr:
            gc.collect()
            day+=j
        c=custom_sql("SELECT Pain FROM Time where Hpday='{}'AND PI={}".format(day,i))
        for obj in c:
            gc.collect()
            try:
                pains.append(int(obj[0]))
            except ValueError:
                continue
        try:
            variances.append(statistics.variance(pains))
        except :
            pass
    return statistics.mean(variances)