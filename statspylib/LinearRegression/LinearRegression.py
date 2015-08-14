class One_Dimensional_Linear_Regression():
    
    import numpy as np
    import scipy.stats
    import pandas as pd
    import matplotlib.pyplot as plt
    
    def __init__(self,x,y,significance_level=0.05):
        self.x=x
        self.y=y
        self.significance_level=significance_level
        self.slope,self.intercept,self.correlation_coefficient,self.pvalue,self.std_err=self.scipy.stats.linregress(self.x,self.y)
        self.se=self.np.sqrt(((self.y-self.x.apply(lambda x:x*self.slope+self.intercept))**2).sum()/(len(self.x)-2))
    
    def linear_regression(self,details=True,graphic=True):
        significance_level=self.significance_level
        slope=self.slope
        intercept=self.intercept
        correlation_coefficient=self.correlation_coefficient
        pvalue=self.pvalue
        std_err=self.std_err
        if details:
            print('linear regression analysis')
            print('---------------------------------------------------------------------')
            print('correlation coefficient:',correlation_coefficient);print()
            print('t-statistic:',abs(correlation_coefficient)*self.np.sqrt((len(self.x)-2)/(1-correlation_coefficient**2)))
            print('t-crit:',self.scipy.stats.t.isf(significance_level/2,len(self.x)-2));print()
            print('P-value:',pvalue)
            print('P-crit',significance_level);print()
            print('standard error:',std_err);print()
            sign_intercept='+'+str(intercept) if intercept>=0 else str(intercept)
            print('regression equation:','y='+str(slope)+'x'+sign_intercept)
            print('confidence interval of slope:',slope-self.scipy.stats.t.isf(significance_level/2,len(self.x)-2)*(self.np.sqrt(((self.y-self.x.apply(lambda x:x*slope+intercept))**2).sum()/(len(self.x)-2)))/self.np.sqrt(sum((self.x-self.x.mean())**2)),slope+self.scipy.stats.t.isf(significance_level/2,len(self.x)-2)*(self.np.sqrt(((self.y-self.x.apply(lambda x:x*slope+intercept))**2).sum()/(len(self.x)-2)))/self.np.sqrt(sum((self.x-self.x.mean())**2)))
            print('?confidence interval of intercept:',intercept-self.scipy.stats.t.isf(significance_level/2,len(self.x)-2)*(self.np.sqrt(((self.y-self.x.apply(lambda x:x*slope+intercept))**2).sum()/(len(self.x)-2)))*self.np.sqrt(1/len(self.x)+self.x.mean()/(sum((self.x-self.x.mean())**2))),intercept+self.scipy.stats.t.isf(significance_level/2,len(self.x)-2)*(self.np.sqrt(((self.y-self.x.apply(lambda x:x*slope+intercept))**2).sum()/(len(self.x)-2)))*self.np.sqrt(1/len(self.x)+self.x.mean()/(sum((self.x-self.x.mean())**2))));print()
            print('R2 (coefficient of determination):',((self.x.apply(lambda x:x*slope+intercept)-self.y.mean())**2).sum()/((self.y-self.y.mean())**2).sum());print()
            print('se (standard error of estimate):',self.se)
            print('---------------------------------------------------------------------')
        else:
            print('linear regression analysis')
            print('---------------------------------------------------------------------')
            sign_intercept='+'+str(intercept) if intercept>=0 else str(intercept)
            print('regression equation:','y='+str(slope)+'x'+sign_intercept);print()
            print('R2 (coefficient of determination):',((self.x.apply(lambda x:x*slope+intercept)-self.y.mean())**2).sum()/((self.y-self.y.mean())**2).sum())
            print('---------------------------------------------------------------------')
        if graphic:
            self.plt.scatter(self.x,self.y)
            self.plt.plot(self.x,[slope*x for x in self.x],'g-')
            self.plt.show()
    
    def significance_test(self):
        print('linear relation test')
        print('---------------------------------------------------------------------')
        F_statistic=((self.x.apply(lambda x:x*self.slope+self.intercept)-self.y.mean())**2).sum()/((((self.y-self.y.mean())**2).sum()-((self.x.apply(lambda x:x*self.slope+self.intercept)-self.y.mean())**2).sum())/(len(self.x)-2))
        F_crit=self.scipy.stats.f.isf(self.significance_level,1,len(self.x)-2)
        print('F-statistic:',F_statistic)
        print('F-crit:',F_crit);print()
        print('accept' if F_statistic<=F_crit else 'refuse');bl=False if F_statistic<=F_crit else True
        print('---------------------------------------------------------------------');print()
        print('regression coefficient test')
        print('---------------------------------------------------------------------')
        t_statistic=self.slope/(self.se/self.np.sqrt(sum((self.x)**2)-sum(self.x)**2/len(self.x)))
        t_crit=self.scipy.stats.t.isf(self.significance_level/2,len(self.x)-2)
        print('t-statistic:',t_statistic)
        print('t-crit:',t_crit)
        print('accept' if t_statistic<=t_crit else 'refuse');bl=False if t_statistic<=t_crit else True
        print('---------------------------------------------------------------------');print()
        print('Can be predict' if bl else 'Can\'t be predict');print();print()
        return bl
    
    def point_estimate(self,point):
        if self.significance_test():
            print('Mean point estimation:',point*self.slope+self.intercept)
            print('Individual point estimate:',point*self.slope+self.intercept);print()
            return point*self.slope+self.intercept

    def interval_estimate(self,point):
        if self.significance_test():
            t=self.scipy.stats.t.isf(self.significance_level/2,len(self.x)-2)*self.se*self.np.sqrt(1/len(self.x)+(point-self.x.mean())**2/sum((self.x-self.x.mean())**2))
            print('Confidence interval estimate:',point*self.slope+self.intercept-t,point*self.slope+self.intercept+t)
            s=self.scipy.stats.t.isf(self.significance_level/2,len(self.x)-2)*self.se*self.np.sqrt(1+1/len(self.x)+(point-self.x.mean())**2/sum((self.x-self.x.mean())**2))
            print('Prediction interval estimate:',point*self.slope+self.intercept-s,point*self.slope+self.intercept+s)
            return (point*self.slope+self.intercept-t,point*self.slope+self.intercept+t),(point*self.slope+self.intercept-s,point*self.slope+self.intercept+s);print()
    
    def residual_analysis(self):
        fig=self.plt.figure()
        self.plt.subplots_adjust(right=2)
        fig.add_subplot(121)
        self.plt.scatter(self.x,self.y-self.x.apply(lambda x:x*self.slope+self.intercept))
        self.plt.grid(True)
        self.plt.title('residual')
        fig.add_subplot(122)
        self.plt.scatter(self.x,(self.y-self.x.apply(lambda x:x*self.slope+self.intercept))/self.se)
        self.plt.grid(True)
        self.plt.title('standardized residual')
        self.plt.show()
        
if __name__=='__main__':
    import pandas as pd
    bldk=[0.9,1.1,4.8,3.2,7.8,2.7,1.6,12.5,1,2.6,0.3,4,0.8,3.5,10.2,3,0.2,0.4,1,6.8,11.6,1.6,1.2,7.2,3.2]
    gxdkye=[67.3,111.3,173,80.8,199.7,16.2,107.4,185.4,96.1,72.8,64.2,132.2,58.6,174.6,263.5,79.3,14.8,73.5,24.7,139.4,368.2,95.7,109.6,196.2,102.2]
    bnljysdk=[6.8,19.8,7.7,7.2,16.5,2.2,10.7,27.1,1.7,9.1,2.1,11.2,6,12.7,15.6,8.9,0.6,5.9,5,7.2,16.8,3.8,10.3,15.8,12]
    dkxmgs=[5,16,17,10,19,1,17,18,10,14,11,23,14,26,34,15,2,11,4,28,32,10,14,16,10]
    bngdzctze=[51.9,90.9,73.7,14.5,63.2,2.2,20.2,43.8,55.9,64.3,42.7,76.7,22.8,117.1,146.7,29.9,42.1,25.3,13.4,64.3,163.9,44.5,67.9,39.7,97.1]
    data_dict={'bldk':bldk,'gxdkye':gxdkye,'bnljysdk':bnljysdk,'dkxmgs':dkxmgs,'bngdzctze':bngdzctze}
    data_dataframe=pd.DataFrame(data_dict,index=list(range(1,26)),columns=['bldk','gxdkye','bnljysdk','dkxmgs','bngdzctze'])
    a=One_Dimensional_Linear_Regression(data_dataframe['gxdkye'],data_dataframe['bldk'])
    a.interval_estimate(100)
    a.residual_analysis()