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
        
