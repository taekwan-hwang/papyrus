from cycle_divider import mean_pain_variance_by_cycle
import statistics
from main.models import Tong2, VarianceInCycle
from scipy.stats import chi2
class Verification:
    def verify_by_pchisq(pi, cycle):
        sigma_cycle=mean_pain_variance_by_cycle(cycle)
        tong2=Tong2.objects.filter(pi=pi).filter(n_attr_codeNM='통증 강도')
        pains=[]
        for pain in tong2:
            pains.append(pain.attr)
        sigma=statistics.variance(pains)
        n=Tong2.objects.filter(pi=pi).filter(n_attr_codeNM='통증 강도').count()
        df=n-1
        v=df*sigma/sigma_cycle
        return chi2.cdf(v, df)