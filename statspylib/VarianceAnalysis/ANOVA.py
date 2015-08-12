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
    
    def ANOVA(self,significance_level=0.05,LSD=True):
        return_DataFrame=self.pd.DataFrame({'SS':[self.SSA,self.SSE,self.SST],'df':[self.df_SSA,self.df_SSE,self.df_SST],
                                           'MS':[self.MSA,self.MSE,np.NaN],'F-value':[self.MSA/self.MSE,np.NaN,np.NaN],
                                           'F-crit':[self.scipy.stats.f.isf(significance_level,self.df_SSA,self.df_SSE),np.NaN,np.NaN],
                                           'result':['[accept]' if self.MSA/self.MSE<=self.scipy.stats.f.isf(significance_level,self.df_SSA,self.df_SSE) else '[refuse]',np.NaN,np.NaN],
                                           'R2':[self.SSA/self.SST,np.NaN,np.NaN]},
                                           index=['A','E','T'],columns=['SS','df','MS','F-value','F-crit','result','R2'])
        print('ANOVA result')
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
            LSD=t*np.sqrt(self.MSE*(1/self.data[i].count()+1/self.data[j].count()));return_dict['LSD'].append(LSD)
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

    def ANOVA(self,significance_level=0.05):
        if ~self.interaction:
            self.all_mean=(self.data.sum()).sum()/(self.data.count()).sum()
            self.SST=(((self.data-self.all_mean)**2).sum()).sum()
            self.SSR=(len(self.data.columns)*(self.data.mean(1)-self.all_mean)**2).sum()
            self.SSC=(len(self.data.index)*(self.data.mean()-self.all_mean)**2).sum()
            self.SSE=self.SST-self.SSR-self.SSC
            self.df_SST=len(self.data.columns)*len(self.data.index)-1
            self.df_SSR=len(self.data.index)-1
            self.df_SSC=len(self.data.columns)-1
            self.df_SSE=self.df_SSR*self.df_SSC
            self.MSR=self.SSR/self.df_SSR
            self.MSC=self.SSC/self.df_SSC
            self.MSE=self.SSE/self.df_SSE
            return_DataFrame=self.pd.DataFrame({'SS':[self.SSR,self.SSC,self.SSE,self.SST],'df':[self.df_SSR,self.df_SSC,self.df_SSE,self.df_SST],
                                               'MS':[self.MSR,self.MSC,self.MSE,np.NaN],'F-value':[self.MSR/self.MSE,self.MSC/self.MSE,np.NaN,np.NaN],
                                               'F-crit':[self.scipy.stats.f.isf(significance_level,self.df_SSR,self.df_SSE),self.scipy.stats.f.isf(significance_level,self.df_SSC,self.df_SSE),np.NaN,np.NaN],
                                               'result':['[accept]' if self.MSR/self.MSE<=self.scipy.stats.f.isf(significance_level,self.df_SSR,self.df_SSE) else '[refuse]','[accept]' if self.MSC/self.MSE<=self.scipy.stats.f.isf(significance_level,self.df_SSC,self.df_SSE) else '[refuse]',np.NaN,np.NaN],
                                               'R2':[(self.SSR+self.SSC)/self.SST,np.NaN,np.NaN,np.NaN]},
                                               index=['R','C','E','T'],columns=['SS','df','MS','F-value','F-crit','result','R2'])
            print('ANOVA result')
            print('---------------------------------------------------------------------')
            print(return_DataFrame)
            print('---------------------------------------------------------------------')
            return 'accept' if return_DataFrame['F-value'][0]<return_DataFrame['F-crit'][0] else 'refuse','accept' if return_DataFrame['F-value'][1]<return_DataFrame['F-crit'][1] else 'refuse'
    
    
    
    
if __name__=='__main__':
    import numpy as np
    import pandas as pd
    
    retail=[57,66,49,40,34,53,44]
    tourism=[68,39,29,45,56,51]+[np.NaN]*1
    aircraft=[31,49,21,34,40]+[np.NaN]*2
    manufacturing=[44,51,65,77,58]+[np.NaN]*2
    data1=pd.DataFrame({'retail':retail,'tourism':tourism,'aircraft':aircraft,'manufacturing':manufacturing},columns=['retail','tourism','aircraft','manufacturing'])
    a=One_Way_ANOVA(data1)
    a.ANOVA()
    print()
    
    area1=[365,345,358,288]
    area2=[350,368,323,280]
    area3=[343,363,353,298]
    area4=[340,330,343,260]
    area5=[323,333,308,298]
    data2=pd.DataFrame({'area1':area1,'area2':area2,'area3':area3,'area4':area4,'area5':area5},columns=['area1','area2','area3','area4','area5'],index=['brand1','brand2','brand3','brand4'])
    data2.columns.name='area factor'
    data2.index.name='brand factor'
    b=Two_Way_ANOVA(data2)
    b.ANOVA()
    print()

    