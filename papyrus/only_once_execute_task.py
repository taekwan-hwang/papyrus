import pyodbc
import statistics
cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=tcp:severancebigcon.database.windows.net;DATABASE=severancebigcon;UID=sbigcon05;PWD=P@ssw0rd;Connection Timeout=;', autocommit=True, timeout=900)
cursor = cnxn.cursor()
pis= [i[0] for i in cursor.execute('SELECT DISTINCT PI FROM Time order by PI')]
cnxn.close()
for pi in pis:
    cnxn1 = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=tcp:severancebigcon.database.windows.net;DATABASE=severancebigcon;UID=sbigcon05;PWD=P@ssw0rd;Connection Timeout=;', autocommit=True, timeout=900)
    cursor1 = cnxn1.cursor()
    hpdays=[i[0] for i in cursor1.execute('SELECT DISTINCT Hpday FROM Time where PI={} order by Hpday'.format(pi))]
    cycle=1
    variance_by_cycle=[]
    for cycle_cur, hpday in enumerate(hpdays):
        if cycle_cur == 3:
            break
        hpday=hpday
        pain_arr=[]
        
        pains=[i[0] for i in cursor1.execute("SELECT Pain From Time where PI={} AND Hpday='{}'".format(pi, hpday))]
        for pain in pains:
            try:
                pain_arr.append(int(pain))
            except ValueError:
                continue
        try:
            variances.append(statistics.variance(pains))
        except :
            pass
        cycle+=1
    if len(variance_by_cycle)==3:
        
        cursor1.execute('INSERT INTO Var_Table (PI,var_cycle_1,var_cycle_2,var_cycle_3) VALUES (%s,%.3f,%.3f,%.3f)'%(pi, variance_by_cycle[0], variance_by_cycle[1], variance_by_cycle[2]))
    elif len(variance_by_cycle)==2:
        
        cursor1.execute('INSERT INTO Var_Table (PI,var_cycle_1,var_cycle_2) VALUES (%s,%.3f,%.3f)'%(pi, variance_by_cycle[0], variance_by_cycle[1]))
    elif len(variance_by_cycle)==1:
        
        cursor1.execute('INSERT INTO Var_Table(PI,var_cycle_1) VALUES (%s, %.3f)'%(pi, variance_by_cycle[0]))
    cnxn1.commit()
    cnxn1.close()