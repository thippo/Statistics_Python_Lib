**Statistics Python Lib**
===================
Python的统计学拓展包

----------

thippo   
thippo@163.com   
http://thippo.github.io   

#####**必须依赖包**
- numpy
- scipy
- pandas
- matplotlib
- scikit-learn

#####**模块结构**
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
###IntervalEstimate   
**单总体均值的区间估计（函数）**   
   
 single_population_mean_interval_estimate(sample_list,confidence_level,population_standard_deviation)   
 
参数：   
　　sample_list：样本的数据列表   
　　confidence_level：置信水平，取值0-1之间   
　　population_variance：总体方差，取值'unknown'(未知)或大于0的数   
返回值：   
　　包含置信下限和置信上限的元组   
   
**单总体比例的区间估计（函数）**   
   
single_population_proportion_interval_estimate(sample_size,sample_proportion,confidence_level)   

参数：   
　　sample_size：样本容积，取值大于0的整数   
　　sample_proportion：样本比例，取值0-1之间   
　　confidence_level：置信水平，取值0-1之间   
返回值：   
　　包含置信下限和置信上限的元组   
   
**单总体方差的区间估计（函数）**   
    
single_population_variance_interval_estimate(sample_list,confidence_level)   
   
参数：   
　　sample_list：样本的数据列表   
　　confidence_level：置信水平，取值0-1之间    
返回值：     
　　包含置信下限和置信上限的元组     