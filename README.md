**Statistics Python Lib**
===================
Python3.4.3的统计学拓展包

----------

thippo   
thippo@163.com   
http://thippo.github.io   

####**必须依赖包**
- numpy
- scipy
- pandas
- matplotlib
- scikit-learn

####**安装**

    git clone git@github.com:thippo/Statistics_Python_Lib.git
    cd Statistics_Python_Lib
    python setup.py install

####**模块结构**
**statspylib**   
　　**ParameterEstimation**   
　　　　IntervalEstimate   
　　　　DetermineSampleSize   
　　**HypothesisTesting**   
　　　　ParametricHypothesisTesting   
　　　　NonparametricHypothesisTesting   
　　**VarianceAnalysis**   
　　　　ANOVA   
　　**LinearRegression**      
　　　　LinearRegression      
　　　　MultipleLinearRegression   
　　**MultivariateStatistics**   
　　　　PCA   
<br>
##- ParameterEstimation
###IntervalEstimate   
**单总体均值的区间估计（函数）**   
single_population_mean_interval_estimate(sample_list,confidence_level,population_standard_deviation)     
**单总体比例的区间估计（函数）**   
single_population_proportion_interval_estimate(sample_size,sample_proportion,confidence_level)   
**单总体方差的区间估计（函数）**   
single_population_variance_interval_estimate(sample_list,confidence_level)   
**双总体均值差的区间估计（函数）** 
double_population_mean_subtraction_interval_estimate(sampleA_list,sampleB_list,confidence_level,population_variance,populationA_variance='#',populationB_variance='#')      
**双总体均值差的区间估计：匹配样本（函数）**    
double_population_mean_subtraction_interval_estimate_matched_sample(sampleA_list,sampleB_list,confidence_level)      
**双总体比例差的区间估计（函数）**    
double_population_proportion_subtraction_interval_estimate(sampleA_size,sampleB_size,sampleA_proportion,sampleB_proportion,confidence_level)          
**双总体方差比的区间估计（函数）**    
double_population_variance_proportion_interval_estimate(sampleA_list,sampleB_list)      
      
###DetermineSampleSize               
**估计总体均值时样本量的确定（函数）**    
determine_population_mean_sample_size(population_standard_deviation,confidence_level,estimate_error)              
**估计总体比例时样本量的确定（函数）**    
determine_population_proportion_sample_size(population_proportion,confidence_level,estimate_error)      
      
##- HypothesisTesting
###ParametricHypothesisTesting   
**单总体均值的假设检验（函数）**   
single_population_mean_hypothesis_testing(test_direction,significant_level,sample_size,sample_mean,population_mean,population_standard_deviation,standard_deviation)       
**单总体比例的假设检验（函数）**   
single_population_proportion_hypothesis_testing(test_direction,significant_level,sample_size,sample_proportion,population_proportion)    
**单总体方差的假设检验（函数）**   
single_population_variance_hypothesis_testing(test_direction,significant_level,sample_size,sample_variance,population_variance)   
**双总体均值差的假设检验（函数）**   
double_population_mean_subtraction_hypothesis_testing(test_direction,significant_level,sampleA_size,sampleB_size,sampleA_mean,sampleB_mean,population_subtraction,population_variance,varianceA='#',varianceB='#')    
**双总体比例差的假设检验（函数）**   
double_population_proportion_subtraction_hypothesis_testing(test_direction,significant_level,sampleA_size,sampleB_size,sampleA_proportion,sampleB_proportion,population_proportion_subtraction)      
**双总体方差比的假设检验（函数）**   
double_population_variance_proportion_hypothesis_testing(test_direction,significant_level,sampleA_size,sampleB_size,sampleA_variance,sampleB_variance,population_variance_proportion)     
**双总体均值差的假设检验：匹配样本（函数）**   
double_population_mean_subtraction_hypothesis_testing_matched_sample(test_direction,significant_level,sample_size,sample_subtraction_mean,sample_subtraction_standard_deviation,population_subtraction_mean)      
       
###NonparametricHypothesisTesting               
**单总体假设检验（类）**    
Single_Population_Test()              
　　**中位数符号检验（方法）**       
　　median_sign_test(arr,median)       
　　**Wilcoxon符号秩检验（方法）**       
　　wilcoxon_signed_rank_test(arr)       
       
**分布的一致性检验：\[\chi^2\]检验/适合度检验（函数）**       
goodness_of_fit_test(f_obs,f_exp,significance_level=0.05)       
         
**双总体假设检验（类）**       
Double_Population_Test()          
　　**\[\chi^2\]独立性检验（方法）**       
　　test_of_independence(observed,significance_level=0.05)      
　　**Fisher精确检验（方法）**       
　　fisher_exact_test(table,alternative='two-sided')       
　　**Wilcoxon秩和检验（方法）**       
　　wilcoxon_rank_sum_test(x,y)      
　　**Mann-Whitney U检验（方法）**       
　　mann_whitney_U_test(x,y,use_continuity=True)       
　　**Mood检验（方法）**       
　　mood_test(x,y,axis=0)      
　　**Ansaru-Bradley检验（方法）**       
　　ansari_bradle_test(x,y)       
          
**多总体假设检验（类）**       
Multiple_Population_Test()          
　　**位置参数的Kruskal-Wallis秩和检验（方法）**       
　　kruskal_wallis_rank_sum_test(*arg)      
　　**尺度参数的Fligner-Killeen检验（方法）**      
　　fligner_killeen_test(*arg)       
      
##- VarianceAnalysis
###ANOVA    
**单因素方差分析（类）**       
One_Way_ANOVA(dataframe)          
　　**方差齐性检验（方法）**       
　　homogeneity_of_variancet()      
　　**方差分析（方法）**       
　　ANOVA(significance_level=0.05,LSD=True)       
          
**双因素方差分析（类）**       
Two_Way_ANOVA(dataframe,interaction=False)          
　　**方差齐性检验（方法）**       
　　homogeneity_of_variancet()      
　　**方差分析（方法）**       
　　ANOVA(significance_level=0.05)       
      
##- LinearRegression      
###LinearRegression      
**一元线性回归（类）**       
One_Dimensional_Linear_Regression(x,y,significance_level=0.05)          
　　**线性回归分析（方法）**       
　　linear_regression(details=True,graphic=True)      
　　**显著性检验（方法）**       
　　significance_test()       
　　**点估计（方法）**       
　　point_estimate(point)      
　　**区间估计（方法）**       
　　interval_estimate(point)        
　　**残差分析（方法）**       
　　residual_analysis()      
          
###MultipleLinearRegression      
**多元线性回归（类）**       
Multiple_Linear_Regression(x,y,significance_level=0.05)          
　　**线性回归分析（方法）**       
　　linear_regression()      
　　**共线性分析（方法）**       
　　multicollinearity()       
　　**预测（方法）**       
　　predict(x)       
      
##- MultivariateStatistics      
###PCA
**主成分分析（函数）**   
PCA(dataMat,topNfeat, normalize=True)       