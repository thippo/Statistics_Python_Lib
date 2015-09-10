import numpy
import scipy.stats
from .. import tools

'''
区间估计（总体必须是正态分布）
single_population_mean_interval_estimate(sample_list,confidence_level,population_standard_deviation)
single_population_proportion_interval_estimate(sample_size,sample_proportion,confidence_level)
single_population_variance_interval_estimate(sample_list,confidence_level)
double_population_mean_subtraction_interval_estimate(sampleA_list,sampleB_list,confidence_level,population_variance,populationA_variance='#',populationB_variance='#')
double_population_mean_subtraction_interval_estimate_matched_sample(sampleA_list,sampleB_list,confidence_level)
double_population_proportion_subtraction_interval_estimate(sampleA_size,sampleB_size,sampleA_proportion,sampleB_proportion,confidence_level)
double_population_variance_proportion_interval_estimate
'''

def single_population_mean_interval_estimate(sample_list,confidence_level,population_standard_deviation):
	'''
	单总体均值的区间估计
	
	参数：
	sample_list：样本的数据列表
	confidence_level：置信水平，取值0-1之间
	population_variance：总体方差，取值'unknown'(未知)或大于0的数
	
	返回值：
	包含置信下限和置信上限的元组

	'''
	n=len(sample_list)
	sample_mean=numpy.mean(sample_list)
	if population_standard_deviation == 'unknown' and n<30:
		population_standard_deviation=tools.compute_standard_deviation(sample_list)
		confidence_lower_limit='%.2f' % (sample_mean-scipy.stats.t.isf((1-confidence_level)/2,n-1)*population_standard_deviation/numpy.sqrt(n))
		confidence_upper_limit='%.2f' % (sample_mean+scipy.stats.t.isf((1-confidence_level)/2,n-1)*population_standard_deviation/numpy.sqrt(n))
		return (confidence_lower_limit,confidence_upper_limit)
	elif population_standard_deviation == 'unknown' and n>=30:
		population_standard_deviation=tools.compute_standard_deviation(sample_list)
		confidence_lower_limit='%.2f' % (sample_mean-abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*population_standard_deviation/numpy.sqrt(n))
		confidence_upper_limit='%.2f' % (sample_mean+abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*population_standard_deviation/numpy.sqrt(n))
		return (confidence_lower_limit,confidence_upper_limit)
	else:
		confidence_lower_limit='%.2f' % (sample_mean-abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*population_standard_deviation/numpy.sqrt(n))
		confidence_upper_limit='%.2f' % (sample_mean+abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*population_standard_deviation/numpy.sqrt(n))
		return (confidence_lower_limit,confidence_upper_limit)

def single_population_proportion_interval_estimate(sample_size,sample_proportion,confidence_level):
	'''
	单总体比例的区间估计
	
	参数：
	sample_size：样本容积，取值大于0的整数
	sample_proportion：样本比例，取值0-1之间
	confidence_level：置信水平，取值0-1之间
	
	返回值：
	包含置信下限和置信上限的元组
	'''
	confidence_lower_limit='%.4f' % (sample_proportion-abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*numpy.sqrt(sample_proportion*(1-sample_proportion)/sample_size))
	confidence_upper_limit='%.4f' % (sample_proportion+abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*numpy.sqrt(sample_proportion*(1-sample_proportion)/sample_size))
	return (confidence_lower_limit,confidence_upper_limit)
	
def single_population_variance_interval_estimate(sample_list,confidence_level):
	'''
	单总体方差的区间估计
	
	参数：
	sample_list：样本的数据列表
	confidence_level：置信水平，取值0-1之间
	
	返回值：
	包含置信下限和置信上限的元组
	'''
	population_variance=tools.compute_variance(sample_list)
	confidence_lower_limit='%.2f' % ((len(sample_list)-1)*population_variance/scipy.stats.chi2.isf((1-confidence_level)/2,len(sample_list)-1))
	confidence_upper_limit='%.2f' % ((len(sample_list)-1)*population_variance/scipy.stats.chi2.isf(1-(1-confidence_level)/2,len(sample_list)-1))
	return (confidence_lower_limit,confidence_upper_limit)
	
def double_population_mean_subtraction_interval_estimate(sampleA_list,sampleB_list,confidence_level,population_variance,populationA_variance='#',populationB_variance='#'):
	'''
	双总体均值差的区间估计
	
	参数：
	sampleA_list：样本A的数据列表
	sampleB_list：样本B的数据列表
	confidence_level：置信水平，取值0-1之间
	population_variance：总体方差，取值'unknown'(未知)，'equal'(未知但相等)，'known'(已知)
	populationA_variance：总体A的方差，取值大于0，如果未知可不填
	populationB_variance：总体B的方差，取值大于0，如果未知可不填
	
	返回值：
	包含置信下限和置信上限的元组
	
	注意：
	population_variance参数不可省略
	'''
	nA=len(sampleA_list)
	nB=len(sampleB_list)
	sampleA_mean=numpy.mean(sampleA_list)
	sampleB_mean=numpy.mean(sampleB_list)
	sampleA_variance=tools.compute_variance(sampleA_list)
	sampleB_variance=tools.compute_variance(sampleB_list)
	if (nA<30 or nB<30) and population_variance=='unknown':
		if nA>=30 and nB>=30:
			confidence_lower_limit='%.2f' % ((sampleA_mean-sampleB_mean)-abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*numpy.sqrt(sampleA_variance/nA+sampleB_variance/nB))
			confidence_upper_limit='%.2f' % ((sampleA_mean-sampleB_mean)+abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*numpy.sqrt(sampleA_variance/nA+sampleB_variance/nB))
			return (confidence_lower_limit,confidence_upper_limit)
		else:
			v=int(round((sampleA_variance/nA+sampleB_variance/nB)**2/((sampleA_variance/nA)**2/(nA-1)+(sampleB_variance/nB)**2/(nB-1))))
			confidence_lower_limit='%.2f' % ((sampleA_mean-sampleB_mean)-scipy.stats.t.isf((1-confidence_level)/2,v)*numpy.sqrt(sampleA_variance/nA+sampleB_variance/nB))
			confidence_upper_limit='%.2f' % ((sampleA_mean-sampleB_mean)+scipy.stats.t.isf((1-confidence_level)/2,v)*numpy.sqrt(sampleA_variance/nA+sampleB_variance/nB))
			return (confidence_lower_limit,confidence_upper_limit)
	elif population_variance=='equal':
		sp2=((nA-1)*sampleA_variance+(nB-1)*sampleB_variance)/(nA+nB-2)
		confidence_lower_limit='%.2f' % ((sampleA_mean-sampleB_mean)-scipy.stats.t.isf((1-confidence_level)/2,nA+nB-2)*numpy.sqrt(sp2/nA+sp2/nB))
		confidence_upper_limit='%.2f' % ((sampleA_mean-sampleB_mean)+scipy.stats.t.isf((1-confidence_level)/2,nA+nB-2)*numpy.sqrt(sp2/nA+sp2/nB))
		return (confidence_lower_limit,confidence_upper_limit)
	elif population_variance=='known':
		confidence_lower_limit='%.2f' % ((sampleA_mean-sampleB_mean)-abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*numpy.sqrt(populationA_variance/nA+populationB_variance/nB))
		confidence_upper_limit='%.2f' % ((sampleA_mean-sampleB_mean)+abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*numpy.sqrt(populationA_variance/nA+populationB_variance/nB))
		return (confidence_lower_limit,confidence_upper_limit)
	else:
		return 'wrong parameter !'

def double_population_mean_subtraction_interval_estimate_matched_sample(sampleA_list,sampleB_list,confidence_level):
	'''
	双总体均值差的区间估计：匹配样本
	
	参数：
	sampleA_list：样本A的数据列表
	sampleB_list：样本B的数据列表
	confidence_level：置信水平，取值0-1之间
	
	返回值：
	包含置信下限和置信上限的元组
	
	注意：
	此函数只能用于总体方差未知的情况
	'''
	nA=len(sampleA_list)
	nB=len(sampleB_list)
	if nA!=nB:
		return 'wrong parameter: the length of datas are not equel !'
	else:
		d_list=list(numpy.array(sampleA_list)-numpy.array(sampleB_list))
		d_mean=numpy.mean(d_list)
		sd=numpy.sqrt(sum([(x-d_mean)**2 for x in d_list])/(nA-1))
		if nA>=30 and nB>=30:
			confidence_lower_limit=d_mean-abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*sd/numpy.sqrt(nA)
			confidence_upper_limit=d_mean+abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*sd/numpy.sqrt(nA)
			return (confidence_lower_limit,confidence_upper_limit)
		else:
			confidence_lower_limit='%.2f' % (d_mean-scipy.stats.t.isf((1-confidence_level)/2,nA-1)*sd/numpy.sqrt(nA))
			confidence_upper_limit='%.2f' % (d_mean+scipy.stats.t.isf((1-confidence_level)/2,nA-1)*sd/numpy.sqrt(nA))
			return (confidence_lower_limit,confidence_upper_limit)

def double_population_proportion_subtraction_interval_estimate(sampleA_size,sampleB_size,sampleA_proportion,sampleB_proportion,confidence_level):
	'''
	双总体比例差的区间估计
	
	参数：
	sampleA_size：样本A的数据容量，大于0的整数
	sampleA_size：样本B的数据容量，大于0的整数
	sampleA_proportion：样本A的比比例，取值0-1之间
	sampleA_proportion：样本B的比比例，取值0-1之间
	confidence_level：置信水平，取值0-1之间
	
	返回值：
	包含置信下限和置信上限的元组
	'''
	confidence_lower_limit='%.4f' % (abs(sampleA_proportion-sampleB_proportion)-abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*numpy.sqrt(sampleA_proportion*(1-sampleA_proportion)/sampleA_size+sampleB_proportion*(1-sampleB_proportion)/sampleB_size))
	confidence_upper_limit='%.4f' % (abs(sampleA_proportion-sampleB_proportion)+abs(scipy.stats.norm.isf((1-(1-confidence_level)/2)))*numpy.sqrt(sampleA_proportion*(1-sampleA_proportion)/sampleA_size+sampleB_proportion*(1-sampleB_proportion)/sampleB_size))
	return (confidence_lower_limit,confidence_upper_limit)

def double_population_variance_proportion_interval_estimate(sampleA_list,sampleB_list):
	nA=len(sampleA_list)
	nB=len(sampleB_list)
	sampleA_variance=tools.compute_variance(sampleA_list)
	sampleB_variance=tools.compute_variance(sampleB_list)
	confidence_lower_limit='%.2f' % ((sampleA_variance/sampleB_variance)/scipy.stats.f.isf((1-confidence_level)/2,nA-1,nB-1))
	confidence_upper_limit='%.2f' % ((sampleA_variance/sampleB_variance)*scipy.stats.f.isf((1-confidence_level)/2,nB-1,nA-1))
	return (confidence_lower_limit,confidence_upper_limit)
