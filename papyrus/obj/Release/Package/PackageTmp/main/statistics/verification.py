from main.statistics.cycle_divider import mean_pain_variance_by_cycle, getHpdays
from main.util.query import custom_sql
import statistics
from main.models import Tong2, VarianceInCycle
from scipy.stats import chi2
class Verification:
    def verify_by_pchisq(pi):
        hpdays=getHpdays(pi)
        cycle=len(hpdays)
        variances=[i[0] for i in custom_sql("select Var_cycle_{} from Var_Cycle where PI={}".format(cycle, pi))]
        sigma_cycle=statistics.mean(variances)
        tong2=Tong2.objects.filter(pi=pi).filter(n_attr_codeNM='통증 강도')
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