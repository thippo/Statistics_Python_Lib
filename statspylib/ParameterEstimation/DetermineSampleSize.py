import scipy.stats
from .. import tools

'''
确定样本量（总体必须是正态分布）
determine_population_mean_sample_size(population_standard_deviation,confidence_level,estimate_error)
determine_population_proportion_sample_size(population_proportion,confidence_level,estimate_error)
'''

def determine_population_mean_sample_size(population_standard_deviation,confidence_level,estimate_error):
	'''
	估计总体均值时样本量的确定
	
	参数：
	population_standard_deviation：样本的标准差，取大于0的数
	confidence_level：置信水平，取值0-1之间
	estimate_error：估计误差，取大于0的数
	
	返回值：
	一个正整数值

	'''
	return int(round(abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))**2*population_standard_deviation**2/estimate_error**2+0.5))
	
def determine_population_proportion_sample_size(population_proportion,confidence_level,estimate_error):
	'''
	估计总体比例时样本量的确定
	
	参数：
	population_proportion：总体比例，取值0-1之间
	confidence_level：置信水平，取值0-1之间
	estimate_error：估计误差，取大于0的数
	
	返回值：
	一个正整数值

	'''
	return int(round(abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))**2*population_proportion*(1-population_proportion)/estimate_error**2+0.49999))