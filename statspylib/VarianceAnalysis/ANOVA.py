class One_Way_ANOVA():

    import numpy as np
    import scipy.stats
    import pandas as pd
    import itertools

    def __init__(self,dataframe):
        self.data=dataframe
        self.all_mean=(self.data.sum()).sum()/(self.data.count()).sum()
        self.SST=(((data-self.all_mean)**2).sum()).sum()
        self.SSA=((self.data.sum()/self.data.count()-self.all_mean)**2*self.data.count()).sum()
        self.SSE=self.SST-self.SSA
        self.df_SSA=len(self.data.columns)-1
        self.df_SST=(self.data.count()).sum()-1
        self.df_SSE=self.df_SST-self.df_SSA
        self.MSA=self.SSA/self.df_SSA
        self.MSE=self.SSE/self.df_SSE
    
    def ANOVA(self,significance_level=0.05,LSD=True):
        return_DataFrame=self.pd.DataFrame({'SS':[self.SSA,self.SSE,self.SST],'df':[self.df_SSA,self.df_SSE,self.df_SST],
                                           'MS':[self.MSA,self.MSE,np.NaN],'F-value':[self.MSA/self.MSE,np.NaN,np.NaN],
                                           'F-crit':[self.scipy.stats.f.isf(significance_level,self.df_SSA,self.df_SSE),np.NaN,np.NaN],
                                           'result':['[accept]' if self.MSA/self.MSE<=self.scipy.stats.f.isf(significance_level,self.df_SSA,self.df_SSE) else '[refuse]',np.NaN,np.NaN],
                                           'R2':[self.SSA/self.SST,np.NaN,np.NaN]},
                                           index=['A','E','T'],columns=['SS','df','MS','F-value','F-crit','result','R2'])
        print('ANOVA result')
        print('----------------------------------------------------------------------')
        print(return_DataFrame)
        print('----------------------------------------------------------------------')
        if LSD:
            print()
            print('multiple_comparison_procedures result')
            print('----------------------------------------------------------------------')
            self.__multiple_comparison_procedures(significance_level)
            print('----------------------------------------------------------------------')
        return 'accept' if return_DataFrame['F-value'][0]<return_DataFrame['F-crit'][0] else 'refuse'

    def __multiple_comparison_procedures(self,significance_level):
        return_dict={'columns1':[],'columns2':[],'statistic':[],'LSD':[],'result':[]}
        t=self.scipy.stats.t.isf(significance_level/2,self.df_SSE)
        combinations_list=list(self.itertools.combinations(self.data.columns,2))
        for i,j in combinations_list:
            return_dict['columns1'].append(i)
            return_dict['columns2'].append(j)
            statistic=abs(self.data[i].mean()-self.data[j].mean());return_dict['statistic'].append(statistic)
            LSD=t*np.sqrt(self.MSE*(1/self.data[i].count()+1/self.data[j].count()));return_dict['LSD'].append(LSD)
            return_dict['result'].append('accept' if statistic<=LSD else '*refuse')
        return_DataFrame=self.pd.DataFrame(return_dict,columns=['columns1','columns2','statistic','LSD','result'])
        print(return_DataFrame)
    
    
    
    
if __name__=='__main__':
    import numpy as np
    import pandas as pd
    retail=[57,66,49,40,34,53,44]
    tourism=[68,39,29,45,56,51]+[np.NaN]*1
    aircraft=[31,49,21,34,40]+[np.NaN]*2
    manufacturing=[44,51,65,77,58]+[np.NaN]*2
    data=pd.DataFrame({'retail':retail,'tourism':tourism,'aircraft':aircraft,'manufacturing':manufacturing},columns=['retail','tourism','aircraft','manufacturing'])
    a=One_Way_ANOVA(data)
    a.ANOVA()