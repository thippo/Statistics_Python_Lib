import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt

class Single_Population_Test():

    import numpy as np
    import scipy.stats
    import pandas as pd

    def median_sign_test(self,arr,median):
        arr=self.pd.Series(arr)
        S_positive=arr[arr>median].count()
        S_negative=arr[arr<median].count()
        p_value=self.scipy.stats.binom.cdf(S_positive,arr[arr!=median].count(),0.5)
        print(p_value)
        
    def Wilcoxon_signed_rank_test(self,arr):
        print(self.scipy.stats.wilcoxon(arr))

def goodness_of_fit_test(f_obs,f_exp,significance_level=0.05):
    chisq_statics,pvalue=scipy.stats.chisquare(f_obs,f_exp)
    chi2_crit=scipy.stats.chi2.isf(significance_level,len(f_obs)-1)
    print('goodness of fit test result')
    print('---------------------------------------------------------------------')
    print('chisq_statics',chisq_statics)
    print('chi2_crit:',chi2_crit)
    print('p-value:',pvalue)
    print('result: [accept]' if chisq_statics<=chi2_crit else 'result: [refuse]')
    print('---------------------------------------------------------------------');print()
    return 'accept' if chisq_statics<=chi2_crit else 'refuse'

class Double_Population_Test():

    import numpy as np
    import scipy.stats
    import pandas as pd
    
    def test_of_independence(self,observed,significance_level=0.05):
        chisq_statics,pvalue,dof,ex=self.scipy.stats.chi2_contingency(observed)
        chi2_crit=self.scipy.stats.chi2.isf(significance_level,dof)
        print('goodness of fit test result')
        print('---------------------------------------------------------------------')
        print('chisq_statics',chisq_statics)
        print('chi2_crit:',chi2_crit)
        print('degree of freedom:',dof)
        print('p-value:',pvalue)    
        print('result: [accept]' if chisq_statics<=chi2_crit else 'result: [refuse]')
        print('---------------------------------------------------------------------');print()
        return 'accept' if chisq_statics<=chi2_crit else 'refuse'
    
    def fisher_exact_test(self,table,alternative='two-sided'):
        oddsratio,pvalue=self.scipy.stats.fisher_exact(table,alternative)
        print('fisher exact test result')
        print('---------------------------------------------------------------------')
        print('oddsratio',oddsratio)
        print('p-value',pvalue)
        print('---------------------------------------------------------------------');print()
        
    def wilcoxon_rank_sum_test(self,x,y):
        statistic,pvalue=self.scipy.stats.ranksums(x, y)
        print('wilcoxon rank sum test result')
        print('---------------------------------------------------------------------')
        print('statistic',statistic)
        print('p-value',pvalue)
        print('---------------------------------------------------------------------');print()
        
    
    def mann_whitney_U_test(self,x,y,use_continuity=True):
        statistic,pvalue =self.scipy.stats.mstats.mannwhitneyu(x,y,use_continuity)
        print('mann whitney U test result')
        print('---------------------------------------------------------------------')
        print('statistic:',statistic)
        print('p-value:',pvalue)
        print('---------------------------------------------------------------------');print()
    
    def mood_test(self,x,y,axis=0):
        z,pvalue=self.scipy.stats.mood(x,y,axis)
        print('mood scale parameters test result')
        print('---------------------------------------------------------------------')
        print('z-statistic:',z)
        print('p-value:',pvalue)
        print('---------------------------------------------------------------------');print()
        
        
        
        
        
if __name__=='__main__':
    import pandas as pd
    
    goodness_of_fit_test([35,16,15,17,17,19,11,16,30,24],[sum([35,16,15,17,17,19,11,16,30,24])/len([35,16,15,17,17,19,11,16,30,24])]*10,0.05)

    '''
    a=Single_Population_Test()
    a.median_sign_test([4632,4728,5052,5064,5484,6972,7696,9048,14760,15013,18730,21240,22836,52788,67200],6064)
    '''
    #b=Single_Population_Test()
    #b.Wilcoxon_signed_rank_test([4.12,5.18,7.63,9.74,10.39,11.92,12.32,12.9,13.54,14.45],8)
    c=Double_Population_Test()    
    c.test_of_independence(pd.DataFrame({'one':[52,60,50],'two':[64,59,65],'three':[24,52,74]},index=['jia','yi','bing'],columns=['one','two','three']))

    d=Double_Population_Test()
    d.fisher_exact_test(pd.DataFrame({'xi':[60,32],'buxi':[3,11]},index=['fei','dui'],columns=['xi','buxi']),alternative="greater")
    
    e=Double_Population_Test()
    e.wilcoxon_rank_sum_test([42,44,38,52,48,46,34,44,38],[34,43,35,33,34,26,30,31,31,27,28,27,30,37,32])
    
    f=Double_Population_Test()
    A=pd.Series([321, 266, 256, 388, 330, 329, 303, 334, 299, 221, 365, 250, 258, 342,343, 298, 238, 317, 354])
    B=pd.Series([488, 598, 507, 428, 807, 342, 512, 350, 672, 589, 665, 549, 451, 481, 514, 391, 366, 468])
    f.mood_test(A+(B.median()-A.median()),B)