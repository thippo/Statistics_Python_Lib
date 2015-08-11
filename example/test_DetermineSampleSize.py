import sys
sys.path.append("D:\\Statistics_In_Python")
from statspylib.ParameterEstimation.DetermineSampleSize import *

#p175 例7.12

print(determine_population_mean_sample_size(2000,0.95,400))


#p176 例7.13

print(determine_population_proportion_sample_size(0.9,0.95,0.05))
