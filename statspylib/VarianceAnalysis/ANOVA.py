class One_Way_ANOVA():

    import numpy as np
    import scipy.stats
    import pandas as pd
    import itertools

    def __init__(self,dataframe):
        self.data=dataframe
        self.all_mean=(self.data.sum()).sum()/(self.data.count()).sum()
        self.SST=(((self.data-self.all_mean)**2).sum()).sum()
        self.SSA=((self.data.sum()/self.data.count()-self.all_mean)**2*self.data.count()).sum()
        self.SSE=self.SST-self.SSA
        self.df_SSA=len(self.data.columns)-1
        self.df_SST=(self.data.count()).sum()-1
        self.df_SSE=self.df_SST-self.df_SSA
        self.MSA=self.SSA/self.df_SSA
        self.MSE=self.SSE/self.df_SSE
        self.homogeneity_of_variance()
        
    def homogeneity_of_variance(self):
        print('homogeneity of variance result (Bartlett)')
        print('---------------------------------------------------------------------')
        statistic,pvalue=self.scipy.stats.bartlett(*[self.data[x].dropna() for x in self.data.columns])
        print('statistic: ',statistic)
        print('pvalue: ',pvalue)
        print('---------------------------------------------------------------------');print()
        print('homogeneity of variance result (Levene)')
        print('---------------------------------------------------------------------')
        statistic,pvalue=self.scipy.stats.levene(*[self.data[x].dropna() for x in self.data.columns])
        print('statistic: ',statistic)
        print('pvalue: ',pvalue)
        print('---------------------------------------------------------------------');print()
        
    
    def ANOVA(self,significance_level=0.05,LSD=True):
        return_DataFrame=self.pd.DataFrame({'SS':[self.SSA,self.SSE,self.SST],'df':[self.df_SSA,self.df_SSE,self.df_SST],
                                           'MS':[self.MSA,self.MSE,self.np.NaN],'F-value':[self.MSA/self.MSE,self.np.NaN,self.np.NaN],
                                           'F-crit':[self.scipy.stats.f.isf(significance_level,self.df_SSA,self.df_SSE),self.np.NaN,self.np.NaN],
                                           'result':['[accept]' if self.MSA/self.MSE<=self.scipy.stats.f.isf(significance_level,self.df_SSA,self.df_SSE) else '[refuse]',self.np.NaN,self.np.NaN],
                                           'R2':[self.SSA/self.SST,self.np.NaN,self.np.NaN]},
                                           index=['A','E','T'],columns=['SS','df','MS','F-value','F-crit','result','R2'])
        print('One-Way ANOVA result')
        print('---------------------------------------------------------------------')
        print(return_DataFrame)
        print('---------------------------------------------------------------------')
        if LSD:
            print()
            print('multiple_comparison_procedures result')
            print('---------------------------------------------------------------------')
            self.__multiple_comparison_procedures(significance_level)
            print('---------------------------------------------------------------------')
        return 'accept' if return_DataFrame['F-value'][0]<return_DataFrame['F-crit'][0] else 'refuse'

    def __multiple_comparison_procedures(self,significance_level):
        return_dict={'columns1':[],'columns2':[],'statistic':[],'LSD':[],'result':[]}
        t=self.scipy.stats.t.isf(significance_level/2,self.df_SSE)
        combinations_list=list(self.itertools.combinations(self.data.columns,2))
        for i,j in combinations_list:
            return_dict['columns1'].append(i)
            return_dict['columns2'].append(j)
            statistic=abs(self.data[i].mean()-self.data[j].mean());return_dict['statistic'].append(statistic)
            LSD=t*self.np.sqrt(self.MSE*(1/self.data[i].count()+1/self.data[j].count()));return_dict['LSD'].append(LSD)
            return_dict['result'].append('accept' if statistic<=LSD else '*refuse')
        return_DataFrame=self.pd.DataFrame(return_dict,columns=['columns1','columns2','statistic','LSD','result'])
        print(return_DataFrame)
    
class Two_Way_ANOVA():

    import numpy as np
    import scipy.stats
    import pandas as pd
    import itertools

    def __init__(self,dataframe,interaction=False):
        assert isinstance(interaction,bool),'interaction must be bool'
        self.data=dataframe
        self.interaction=interaction
        self.homogeneity_of_variance()
        
    def homogeneity_of_variance(self):
        print('homogeneity of variance result (Bartlett)')
        print('---------------------------------------------------------------------')
        statistic,pvalue=self.scipy.stats.bartlett(*[self.data[x].dropna() for x in self.data.columns])
        print('statistic: ',statistic)
        print('pvalue: ',pvalue)
        print('---------------------------------------------------------------------');print()
        print('homogeneity of variance result (Levene)')
        print('---------------------------------------------------------------------')
        statistic,pvalue=self.scipy.stats.levene(*[self.data[x].dropna() for x in self.data.columns])
        print('statistic: ',statistic)
        print('pvalue: ',pvalue)
        print('---------------------------------------------------------------------');print()

    def ANOVA(self,significance_level=0.05):
        if self.interaction:
            all_mean=(self.data.sum()).sum()/(self.data.count()).sum()
            m=(self.data.groupby(self.data.index).count().sum()).sum()/((self.data.groupby(self.data.index).count()).count()).sum()
            SST=(((self.data-all_mean)**2).sum()).sum()
            SSR=len(self.data.columns)*m*((self.data.groupby(self.data.index).mean().mean(1)-all_mean)**2).sum()
            SSC=len(list(set(self.data.index)))*m*((self.data.groupby(self.data.index).mean().mean()-all_mean)**2).sum()
            SSRC=m*sum([((self.data.groupby(self.data.index).mean()[k][r]-(self.data.groupby(self.data.index).mean()).mean()[k]-(self.data.groupby(self.data.index).mean()).mean(1)[r]+all_mean))**2 for r in set(self.data.index) for k in self.data.columns])
            SSE=SST-SSR-SSC-SSRC
            df_SST=(self.data.count()).sum()-1
            df_SSR=len(list(set(self.data.index)))-1
            df_SSC=len(self.data.columns)-1
            df_SSRC=df_SSR*df_SSC
            df_SSE=(df_SSR+1)*(df_SSC+1)*(m-1)
            MSR=SSR/df_SSR
            MSC=SSC/df_SSC
            MSRC=SSRC/df_SSRC
            MSE=SSE/df_SSE
            return_DataFrame=self.pd.DataFrame({'SS':[SSR,SSC,SSRC,SSE,SST],'df':[df_SSR,df_SSC,df_SSRC,df_SSE,df_SST],
                                               'MS':[MSR,MSC,MSRC,MSE,self.np.NaN],'F-value':[MSR/MSE,MSC/MSE,MSRC/MSE,self.np.NaN,self.np.NaN],
                                               'F-crit':[self.scipy.stats.f.isf(significance_level,df_SSR,df_SSE),self.scipy.stats.f.isf(significance_level,df_SSC,df_SSE),self.scipy.stats.f.isf(significance_level,df_SSRC,df_SSE),self.np.NaN,self.np.NaN],
                                               'result':['[accept]' if MSR/MSE<=self.scipy.stats.f.isf(significance_level,df_SSR,df_SSE) else '[refuse]',
                                                         '[accept]' if MSC/MSE<=self.scipy.stats.f.isf(significance_level,df_SSC,df_SSE) else '[refuse]',
                                                         '[accept]' if MSRC/MSE<=self.scipy.stats.f.isf(significance_level,df_SSRC,df_SSE) else '[refuse]',self.np.NaN,self.np.NaN],
                                               'R2':['unknown',self.np.NaN,self.np.NaN,self.np.NaN,self.np.NaN]},
                                               index=['R','C','RC','E','T'],columns=['SS','df','MS','F-value','F-crit','result','R2'])
            print('Two-Way ANOVA (interaction=True) result')
            print('---------------------------------------------------------------------')
            print(return_DataFrame)
            print('---------------------------------------------------------------------')
            return '[accept]' if MSR/MSE<=self.scipy.stats.f.isf(significance_level,df_SSR,df_SSE) else '[refuse]','[accept]' if MSC/MSE<=self.scipy.stats.f.isf(significance_level,df_SSC,df_SSE) else '[refuse]','[accept]' if MSRC/MSE<=self.scipy.stats.f.isf(significance_level,df_SSRC,df_SSE) else '[refuse]'

        else:
            all_mean=(self.data.sum()).sum()/(self.data.count()).sum()
            SST=(((self.data-all_mean)**2).sum()).sum()
            SSR=(len(self.data.columns)*(self.data.mean(1)-all_mean)**2).sum()
            SSC=(len(self.data.index)*(self.data.mean()-all_mean)**2).sum()
            SSE=SST-SSR-SSC
            df_SST=len(self.data.columns)*len(self.data.index)-1
            df_SSR=len(self.data.index)-1
            df_SSC=len(self.data.columns)-1
            df_SSE=df_SSR*df_SSC
            MSR=SSR/df_SSR
            MSC=SSC/df_SSC
            MSE=SSE/df_SSE
            return_DataFrame=self.pd.DataFrame({'SS':[SSR,SSC,SSE,SST],'df':[df_SSR,df_SSC,df_SSE,df_SST],
                                               'MS':[MSR,MSC,MSE,self.np.NaN],'F-value':[MSR/MSE,MSC/MSE,self.np.NaN,self.np.NaN],
                                               'F-crit':[self.scipy.stats.f.isf(significance_level,df_SSR,df_SSE),self.scipy.stats.f.isf(significance_level,df_SSC,df_SSE),self.np.NaN,self.np.NaN],
                                               'result':['[accept]' if MSR/MSE<=self.scipy.stats.f.isf(significance_level,df_SSR,df_SSE) else '[refuse]','[accept]' if MSC/MSE<=self.scipy.stats.f.isf(significance_level,df_SSC,df_SSE) else '[refuse]',self.np.NaN,self.np.NaN],
                                               'R2':[(SSR+SSC)/SST,self.np.NaN,self.np.NaN,self.np.NaN]},
                                               index=['R','C','E','T'],columns=['SS','df','MS','F-value','F-crit','result','R2'])
            print('Two-Way ANOVA (interaction=False) result')
            print('---------------------------------------------------------------------')
            print(return_DataFrame)
            print('---------------------------------------------------------------------')
            return 'accept' if return_DataFrame['F-value'][0]<return_DataFrame['F-crit'][0] else 'refuse','accept' if return_DataFrame['F-value'][1]<return_DataFrame['F-crit'][1] else 'refuse'

    