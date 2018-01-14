from main.models import Test, Time

def get_by_cycle(n):#싸이클별로 데이터 모아주는 코드
    all=Test.objects.all().order_by('reg_num', 'hp_day')
    reg_nums=[]
    objs=[]
    return_obj=[]
    for i in all:
        if not i.reg_num in reg_nums:
            reg_nums.append(i.reg_num)
    for i in reg_nums:
        objs.append(Test.objects.filter(reg_num=i).order_by('hp_day'))
    temp=[]
    for i in objs:
        tmp=[]
        for j in i:
            if not j.hp_day in tmp:
                tmp.append(j)
        temp.append(tmp)

    for i in temp:
        if len(i)<n:#i[n] == None:
            continue
        else:
            return_obj.append(i[n-1])

    return return_obj

def order():
    t=Time.objects.all().order_by('pi', 'hptime')
    d1=get_by_cycle(1)
    d2=get_by_cycle(2)
    d3=get_by_cycle(3)