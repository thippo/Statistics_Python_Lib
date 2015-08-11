import sys
sys.path.append("D:\\Statistics_In_Python")
from statspylib.HypothesisTesting.ParametricHypothesisTesting import *

#p192 例8.4
print(single_population_mean_hypothesis_testing('double',0.05,200,0.076,0.081,'unknown',0.025))


#p193 例8.5

print(single_population_mean_hypothesis_testing('single',0.05,100,960,1000,'known',200))


#p194 例8.6

print(single_population_mean_hypothesis_testing('single',0.05,20,1245,1200,'known',150))


#p194 例8.7

print(single_population_mean_hypothesis_testing('double',0.05,10,5.3,5,'unknown',0.3))


#p196 例8.8

print(single_population_proportion_hypothesis_testing('double',0.05,400,0.1425,0.147))


#p197 例8.9

print(single_population_variance_hypothesis_testing('single',0.05,25,0.866,1))


#p199 例8.10

print(double_population_mean_subtraction_hypothesis_testing('double',0.05,32,40,50,44,0,'known',8**2,10**2))


#p201 例8.11

print(double_population_mean_subtraction_hypothesis_testing('single',0.05,15,20,589.67,629.25,0,'unknown',2431.429,3675.461))


#p203 例8.12

print(double_population_proportion_subtraction_hypothesis_testing('double',0.05,100,100,0.76,0.69,0))



#p204 例8.13

print(double_population_proportion_subtraction_hypothesis_testing('single',0.05,150,150,0.45,0.36,0.1))


#p206 例8.14

print(double_population_variance_proportion_hypothesis_testing('double',0.05,15,20,2431.429,3675.461,1))


#p206 例8.15

print(double_population__mean_subtraction_hypothesis_testing_matched_sample('single',0.05,10,9.85,2.199,8.5))