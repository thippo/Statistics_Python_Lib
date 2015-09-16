class Multiple_Linear_Regression():
    
    import numpy as np
    import pandas as pd
    import scipy.stats as ss
    from sklearn import linear_model
    
    def __init__(self,x,y,significance_level=0.05):
        self.x=x.transpose()
        self.y=y
        self.significance_level=significance_level
        self.clf = self.linear_model.LinearRegression()
        self.clf.fit(self.x,self.y)
    
    def linear_regression(self):
        print('multiple linear regression analysis')
        print('---------------------------------------------------------------------')
        x_side=''
        for i in range(len(self.clf.coef_)):
            x_side=x_side+('+'+str(self.clf.coef_[i]) if self.clf.coef_[i]>=0 else str(self.clf.coef_[i]))+'x'+str(i+1)
        print('regression equation:','y='+(str(self.clf.intercept_) if self.clf.intercept_>=0 else str(self.clf.intercept_))+x_side);print()
        self.x_pd=self.pd.DataFrame(self.x)
        y_fit=(self.x_pd*self.clf.coef_).sum(1)+self.clf.intercept_
        self.SST=((self.y-self.y.mean())**2).sum()
        self.SSR=((y_fit-self.y.mean())**2).sum()
        print('R2 (multiple coefficient of determination):',self.SSR/self.SST)
        print('R2 (adjusted multiple coefficient of determination):',1-(1-self.SSR/self.SST)*((len(self.y)-1)/(len(self.y)-1-len(self.x.transpose()))));print()
        self.se=self.np.sqrt((self.SST-self.SSR)/(len(self.y)-1-len(self.x.transpose())))
        print('standard error:',self.se)
        print('---------------------------------------------------------------------');print()
        self._significance_test()
        
    def _significance_test(self):
        print('linear relation test')
        print('---------------------------------------------------------------------')
        F_statistic=(self.SSR/len(self.x.transpose()))/((self.SST-self.SSR)/(len(self.y)-1-len(self.x.transpose())))
        F_crit=self.ss.f.isf(self.significance_level,len(self.x.transpose()),len(self.y)-1-len(self.x.transpose()))
        print('F-statistic:',F_statistic)
        print('F-crit:',F_crit);print()
        pvalue=self.ss.f.sf(F_statistic,len(self.x.transpose()),len(self.y)-1-len(self.x.transpose()))
        print('p-value:',pvalue)
        print('---------------------------------------------------------------------');print()
        print('regression coefficient test')
        print('---------------------------------------------------------------------')
        test_dict={'x'+str(q+1):[self.clf.coef_[q],
                                self.clf.coef_[q]-self.ss.t.isf(self.significance_level,len(self.y)-1-len(self.x.transpose()))*self.se/self.np.sqrt((self.x.transpose()[q]**2).sum()-((self.x.transpose()[q]).sum())**2/len(self.y)),
                                self.clf.coef_[q]+self.ss.t.isf(self.significance_level,len(self.y)-1-len(self.x.transpose()))*self.se/self.np.sqrt((self.x.transpose()[q]**2).sum()-((self.x.transpose()[q]).sum())**2/len(self.y)),
                                self.clf.coef_[q]*self.np.sqrt((self.x.transpose()[q]**2).sum()-((self.x.transpose()[q]).sum())**2/len(self.y))/self.se,
                                self.ss.t.sf(self.clf.coef_[q]*self.np.sqrt((self.x.transpose()[q]**2).sum()-((self.x.transpose()[q]).sum())**2/len(self.y))/self.se,len(self.y)-1-len(self.x.transpose()))] for q in range(len(self.clf.coef_))}
        print(self.pd.DataFrame(test_dict,columns=['x'+str(q+1) for q in range(len(self.clf.coef_))],index=['coef','low','up','t-statistic','pvalue']).T);print()
        

    def multicollinearity(self):
        import itertools
        print('multicollinearity test')
        print('---------------------------------------------------------------------')
        print('#correlation coefficient')
        for i in itertools.combinations(range(len(self.clf.coef_)),2):
            r=self.np.corrcoef(self.x.transpose()[i[0]],self.x.transpose()[i[1]])[0,1]
            print('x'+str(i[0]+1),'x'+str(i[1]+1),'|',r)
        print();print('#correlation coefficient statistic')
        corcrit=self.ss.t.isf(self.significance_level/2,len(self.y)-2)
        for i in itertools.combinations(range(len(self.clf.coef_)),2):
            r=self.np.corrcoef(self.x.transpose()[i[0]],self.x.transpose()[i[1]])[0,1]
            corstatistic=r*self.np.sqrt(len(self.y)-2)/self.np.sqrt(1-r**2)
            print('x'+str(i[0]+1),'x'+str(i[1]+1),'|',corstatistic,'>=' if corstatistic>=corcrit else '<',corcrit)
        print();print('#VIF variance inflation factor')
        for i in range(len(self.x.transpose())):
            vif=self._VIF(self.x.transpose()[[j for j in range(len(self.x.transpose())) if j!=i]].transpose(),self.x.transpose()[i])
            print('x'+str(i+1),'|',vif,'*' if vif>=10 else '')
    
    def _VIF(self,x,y):
        clf = self.linear_model.LinearRegression()
        clf.fit(x,y)
        x_pd=self.pd.DataFrame(x)
        y_fit=(x_pd*clf.coef_).sum(1)+clf.intercept_
        SST=((y-y.mean())**2).sum()
        SSR=((y_fit-y.mean())**2).sum()
        VIF=1/(1-SSR/SST)
        return VIF
    
    def predict(self,x):
        assert isinstance(x,(tuple,list)),'x must be tulpe or list'
        return self.clf.predict(x)
        