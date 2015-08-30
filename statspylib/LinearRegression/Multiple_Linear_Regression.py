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
        print(self.SST,self.SSR)
        print('R2 (multiple coefficient of determination):',self.SSR/self.SST)
        print('R2 (adjusted multiple coefficient of determination):',1-(1-self.SSR/self.SST)*((len(self.y)-1)/(len(self.y)-1-len(self.x.transpose()))));print()
        self.se=np.sqrt((self.SST-self.SSR)/(len(self.y)-1-len(self.x.transpose())))
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
        print(self.pd.DataFrame(test_dict,columns=['x'+str(q+1) for q in range(len(self.clf.coef_))],index=['coef','low','up','t-statistic','pvalue']).T)
        

        
        
        
if __name__=='__main__':    
    import numpy as np
    #'''
    x = np.array([[274,180,375,205,86,265,98,330,195,53,430,372,236,157,370],[2450,3250,3802,2838,2347,3782,3008,2450,2137,2560,4020,4427,2660,2088,2605]])
    y = np.array([162,120,223,131,67,169,81,192,116,55,252,232,144,103,212])
    a=Multiple_Linear_Regression(x,y)
    a.linear_regression()
    #'''
    '''
    bldk=[0.9,1.1,4.8,3.2,7.8,2.7,1.6,12.5,1,2.6,0.3,4,0.8,3.5,10.2,3,0.2,0.4,1,6.8,11.6,1.6,1.2,7.2,3.2]
    gxdkye=[67.3,111.3,173,80.8,199.7,16.2,107.4,185.4,96.1,72.8,64.2,132.2,58.6,174.6,263.5,79.3,14.8,73.5,24.7,139.4,368.2,95.7,109.6,196.2,102.2]
    bnljysdk=[6.8,19.8,7.7,7.2,16.5,2.2,10.7,27.1,1.7,9.1,2.1,11.2,6,12.7,15.6,8.9,0.6,5.9,5,7.2,16.8,3.8,10.3,15.8,12]
    dkxmgs=[5,16,17,10,19,1,17,18,10,14,11,23,14,26,34,15,2,11,4,28,32,10,14,16,10]
    bngdzctze=[51.9,90.9,73.7,14.5,63.2,2.2,20.2,43.8,55.9,64.3,42.7,76.7,22.8,117.1,146.7,29.9,42.1,25.3,13.4,64.3,163.9,44.5,67.9,39.7,97.1]
    x=np.array([gxdkye,bnljysdk,dkxmgs,bngdzctze])
    y=np.array(bldk)
    b=Multiple_Linear_Regression(x,y)
    b.linear_regression()
    '''