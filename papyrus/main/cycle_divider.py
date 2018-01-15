from main.models import Test, Time

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

def get_by_person():
    t=Time.objects.all().order_by('pi')
    pis=[]
	objs=[]
	return_obj=[]
	for i in t:
		if not i.pi in pis:
			pis.append(i.pi)
    for i in pis:
		objs.append(Time.objects.filter(pi=i).order_by('hptime'))
	for i in objs:
		return_obj+=i
	return return_obj