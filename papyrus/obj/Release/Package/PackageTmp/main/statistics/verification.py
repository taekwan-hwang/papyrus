from main.statistics.cycle_divider import mean_pain_variance_by_cycle
from main.util.query import custom_sql
import statistics
from main.models import Tong2, VarianceInCycle
from scipy.stats import chi2
class Verification:
    def verify_by_pchisq(pi, cycle):
        sigma_cycle=mean_pain_variance_by_cycle(cycle)
        hpday=custom_sql("select distinct 입원일자 from TB_TONG_2 where 등록번호={}".format(pi))[cycle-1][0]
        tong2=Tong2.objects.filter(pi=pi).filter(n_attr_codeNM='통증 강도').filter(hospitalization_date=hpday)
        pains=[]

        for pain in tong2:
            try:
                pains.append(int(pain.attr))
            except ValueError:
                pass
        sigma=statistics.variance(pains)
        n=len(pains)
        df=n-1
        v=df*sigma/sigma_cycle
        return 1-chi2.cdf(v, df)