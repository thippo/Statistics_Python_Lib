from statspylib.ParameterEstimation.IntervalEstimate import *

#p159 例7.1

data=[112.5,101,103,102,100.5,102.6,107.5,95,108.8,115.6,100,123.5,102,101.6,102.2,116.6,95.4,97.8,108.6,105,136.8,102.8,101.5,98.4,93.3]
print(single_population_mean_interval_estimate(data,0.95,10))


#p160 例7.2

data=[23,35,39,27,36,44,36,42,46,43,31,33,42,53,45,54,47,24,34,28,39,36,44,40,39,49,38,34,48,50,34,39,45,48,45,32]
print(single_population_mean_interval_estimate(data,0.9,'unknown'))


#p161 例7.3

data=[1510,1450,1480,1460,1520,1480,1490,1460,1480,1510,1530,1470,1500,1520,1510,1470]
print(single_population_mean_interval_estimate(data,0.95,'unknown'))


#163 例7.4

print(single_population_proportion_interval_estimate(100,0.65,0.95))


#p164 例7.5

data=[112.5,101,103,102,100.5,102.6,107.5,95,108.8,115.6,100,123.5,102,101.6,102.2,116.6,95.4,97.8,108.6,105,136.8,102.8,101.5,98.4,93.3]
print(single_population_variance_interval_estimate(data,0.95))


#p166 例7.7

data1=[28.3,30.1,29,37.6,32.1,28.8,36,37.2,38.5,34.4,28,30]
data2=[27.6,22.2,31,33.8,20,30.2,31.7,26,32,31.2,33.4,26.5]
print(double_population_mean_subtraction_interval_estimate(data1,data2,0.95,'equal'))


#p167 例7.8

data1=[28.3,30.1,29,37.6,32.1,28.8,36,37.2,38.5,34.4,28,30]
data2=[27.6,22.2,31,33.8,20,30.2,31.7,26.5]
print(double_population_mean_subtraction_interval_estimate(data1,data2,0.95,'unknown'))


#p169 例7.9

data1=[78,63,72,89,91,49,68,76,85,55]
data2=[71,44,61,84,74,51,55,60,77,39]
print(double_population_mean_subtraction_interval_estimate_matched_sample(data1,data2,0.95))


#p170 例7.10

print(double_population_proportion_subtraction_interval_estimate(400,500,0.32,0.45,0.95))

