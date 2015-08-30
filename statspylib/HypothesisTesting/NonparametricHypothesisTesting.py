class Single_Population_Test():

    import scipy.stats as ss
    import pandas as pd

    def median_sign_test(self,arr,median):
        arr=self.pd.Series(arr)
        S_positive=arr[arr>median].count()
        S_negative=arr[arr<median].count()
        p_value=self.ss.binom.cdf(S_positive,arr[arr!=median].count(),0.5)
        print('median sign test result')
        print('---------------------------------------------------------------------')
        print('p-value:',p_value)
        print('---------------------------------------------------------------------');print()
        
    def wilcoxon_signed_rank_test(self,arr):
        print('wilcoxon signed rank test result')
        print('---------------------------------------------------------------------')
        statistic,pvalue=self.ss.wilcoxon(arr)
        print('statistic:',statistic)
        print('p-value:',pvalue)
        print('---------------------------------------------------------------------');print()

def goodness_of_fit_test(f_obs,f_exp,significance_level=0.05):
    import scipy.stats as ss
    chisq_statics,pvalue=ss.chisquare(f_obs,f_exp)
    chi2_crit=ss.chi2.isf(significance_level,len(f_obs)-1)
    print('goodness of fit test result')
    print('---------------------------------------------------------------------')
    print('chisq_statics',chisq_statics)
    print('chi2_crit:',chi2_crit)
    print('p-value:',pvalue)
    print('result: [accept]' if chisq_statics<=chi2_crit else 'result: [refuse]')
    print('---------------------------------------------------------------------');print()
    return 'accept' if chisq_statics<=chi2_crit else 'refuse'

class Double_Population_Test():

    import scipy.stats as ss
    
    def test_of_independence(self,observed,significance_level=0.05):
        chisq_statics,pvalue,dof,ex=self.ss.chi2_contingency(observed)
        chi2_crit=self.ss.chi2.isf(significance_level,dof)
        print('test of independence result')
        print('---------------------------------------------------------------------')
        print('chisq_statics',chisq_statics)
        print('chi2_crit:',chi2_crit)
        print('degree of freedom:',dof)
        print('p-value:',pvalue)    
        print('result: [accept]' if chisq_statics<=chi2_crit else 'result: [refuse]')
        print('---------------------------------------------------------------------');print()
        return 'accept' if chisq_statics<=chi2_crit else 'refuse'
    
    def fisher_exact_test(self,table,alternative='two-sided'):
        oddsratio,pvalue=self.ss.fisher_exact(table,alternative)
        print('fisher exact test result')
        print('---------------------------------------------------------------------')
        print('oddsratio',oddsratio)
        print('p-value',pvalue)
        print('---------------------------------------------------------------------');print()
        
    def wilcoxon_rank_sum_test(self,x,y):
        statistic,pvalue=self.ss.ranksums(x, y)
        print('wilcoxon rank sum test result')
        print('---------------------------------------------------------------------')
        print('statistic',statistic)
        print('p-value',pvalue)
        print('---------------------------------------------------------------------');print()
        
    
    def mann_whitney_U_test(self,x,y,use_continuity=True):
        statistic,pvalue =self.ss.mstats.mannwhitneyu(x,y,use_continuity)
        print('mann whitney U test result')
        print('---------------------------------------------------------------------')
        print('statistic:',statistic)
        print('p-value:',pvalue)
        print('---------------------------------------------------------------------');print()
    
    def mood_test(self,x,y,axis=0):
        z,pvalue=self.ss.mood(x,y,axis)
        print('mood scale parameters test result')
        print('---------------------------------------------------------------------')
        print('z-statistic:',z)
        print('p-value:',pvalue)
        print('---------------------------------------------------------------------');print()
    
    def ansari_bradle_test(self,x,y):
        statistic,pvalue=self.ss.ansari(x,y)
        print('ansari bradle test result')
        print('---------------------------------------------------------------------')
        print('statistic:',statistic)
        print('p-value:',pvalue)
        print('---------------------------------------------------------------------');print()
        
        
class Multiple_Population_Test(): 

    import scipy.stats as ss
    
    def kruskal_wallis_rank_sum_test(self,*arg):
        statistic,pvalue =self.ss.kruskal(*arg)
        print('kruskal wallis rank sum test result')
        print('---------------------------------------------------------------------')
        print('statistic:',statistic)
        print('p-value:',pvalue)
        print('---------------------------------------------------------------------');print()
    
    def fligner_killeen_test(self,*arg):
        statistic,pvalue =self.ss.fligner(*arg)
        print('fligner killeen test result')
        print('---------------------------------------------------------------------')
        print('statistic:',statistic)
        print('p-value:',pvalue)
        print('---------------------------------------------------------------------');print()
        
        
        
if __name__=='__main__':

    import pandas as pd

    a=Single_Population_Test()
    a.median_sign_test([4632,4728,5052,5064,5484,6972,7696,9048,14760,15013,18730,21240,22836,52788,67200],6064)
    
    b=Single_Population_Test()
    b.wilcoxon_signed_rank_test([4632,4728,5052,5064,5484,6972,7696,9048,14760,15013,18730,21240,22836,52788,67200])

    goodness_of_fit_test([35,16,15,17,17,19,11,16,30,24],[sum([35,16,15,17,17,19,11,16,30,24])/len([35,16,15,17,17,19,11,16,30,24])]*10,0.05)

    c=Double_Population_Test()    
    c.test_of_independence(pd.DataFrame({'one':[52,60,50],'two':[64,59,65],'three':[24,52,74]},index=['jia','yi','bing'],columns=['one','two','three']))

    d=Double_Population_Test()
    d.fisher_exact_test(pd.DataFrame({'xi':[60,32],'buxi':[3,11]},index=['fei','dui'],columns=['xi','buxi']),alternative="greater")
    
    e=Double_Population_Test()
    e.wilcoxon_rank_sum_test([42,44,38,52,48,46,34,44,38],[34,43,35,33,34,26,30,31,31,27,28,27,30,37,32])
    e.mann_whitney_U_test([42,44,38,52,48,46,34,44,38],[34,43,35,33,34,26,30,31,31,27,28,27,30,37,32])
    
    f=Double_Population_Test()
    A=pd.Series([321, 266, 256, 388, 330, 329, 303, 334, 299, 221, 365, 250, 258, 342,343, 298, 238, 317, 354])
    B=pd.Series([488, 598, 507, 428, 807, 342, 512, 350, 672, 589, 665, 549, 451, 481, 514, 391, 366, 468])
    f.mood_test(A+(B.median()-A.median()),B)
    
    g=Double_Population_Test()
    g.ansari_bradle_test([18.0,17.1,16.4,16.9,16.9,16.7,16.7,17.2,17.5,16.9],[17.0,16.9,17.0,16.9,17.2,17.1,16.8,17.1,17.1,17.2])
    
    h=Multiple_Population_Test()
    h.kruskal_wallis_rank_sum_test([306, 385, 300, 319, 320],[311, 364, 315, 338, 398],[289, 198, 201, 302, 289])

    i=Multiple_Population_Test()
    i.fligner_killeen_test([8,7,9,10,9,6,5,8,10,5],[8,7,9,6,8,9,10,7,8,9],[10,10,9,6,8,3,5,6,7,4])