import numpy
import scipy.stats
from .. import tools

def single_population_mean_hypothesis_testing(test_direction,significant_level,sample_size,sample_mean,population_mean,population_standard_deviation,standard_deviation):
	def z_statistics():
		return abs((sample_mean-population_mean)/(standard_deviation/numpy.sqrt(sample_size)))
	def t_statistics():
		return abs((sample_mean-population_mean)/(standard_deviation/numpy.sqrt(sample_size)))	
	def p_value_z_statistics():
		if test_direction=='double':
			return 2*(1-scipy.stats.norm.cdf(z_statistics()))
		elif test_direction=='single':
			return 1-scipy.stats.norm.cdf(z_statistics())
	def p_value_t_statistics():
		if test_direction=='double':
			return 2*(1-scipy.stats.t.cdf(t_statistics(),sample_size-1))
		elif test_direction=='single':
			return 1-scipy.stats.t.cdf(t_statistics(),sample_size-1)
	if sample_size>=30:
		if test_direction=='double':
			z_significant_level_value=abs(scipy.stats.norm.isf(1-significant_level/2))
			return {'z_statistics':(z_statistics(),z_significant_level_value),'p_value':(p_value_z_statistics(),significant_level)}
		elif test_direction=='single':
			z_significant_level_value=abs(scipy.stats.norm.isf(1-significant_level))
			return {'z_statistics':(z_statistics(),z_significant_level_value),'p_value':(p_value_z_statistics(),significant_level)}
		else:
			print('wrong parameter! Check test_direction!')
	elif sample_size<30 and sample_size>0:
		if population_standard_deviation=='known':
			if test_direction=='double':
				z_significant_level_value=abs(scipy.stats.norm.isf(1-significant_level/2))
				return {'z_statistics':(z_statistics(),z_significant_level_value),'p_value':(p_value_z_statistics(),significant_level)}
			elif test_direction=='single':
				z_significant_level_value=abs(scipy.stats.norm.isf(1-significant_level))
				return {'z_statistics':(z_statistics(),z_significant_level_value),'p_value':(p_value_z_statistics(),significant_level)}
			else:
				print('wrong parameter! Check test_direction!')
		elif population_standard_deviation=='unknown':
			if test_direction=='double':
				t_significant_level_value=abs(scipy.stats.t.isf(significant_level/2,sample_size-1))
				return {'t_statistics':(t_statistics(),t_significant_level_value),'p_value':(p_value_t_statistics(),significant_level)}
			elif test_direction=='single':
				t_significant_level_value=abs(scipy.stats.t.isf(significant_level,sample_size-1))
				return {'t_statistics':(t_statistics(),t_significant_level_value),'p_value':(p_value_t_statistics(),significant_level)}
			else:
				print('wrong parameter! Check test_direction!')
		else:
			print('wrong parameter! Check population_standard_deviation!')
	else:
		print('wrong parameter! Check sample_size!')
		
def single_population_proportion_hypothesis_testing(test_direction,significant_level,sample_size,sample_proportion,population_proportion):
	def z_statistics():
		return abs((sample_proportion-population_proportion)/numpy.sqrt(population_proportion*(1-population_proportion)/sample_size))
	def p_value_z_statistics():
		if test_direction=='double':
			return 2*(1-scipy.stats.norm.cdf(z_statistics()))
		elif test_direction=='single':
			return 1-scipy.stats.norm.cdf(z_statistics())
		else:
			print('wrong parameter! Check test_direction!')
	if test_direction=='double':
		z_significant_level_value=abs(scipy.stats.norm.isf(1-significant_level/2))
		return {'z_statistics':(z_statistics(),z_significant_level_value),'p_value':(p_value_z_statistics(),significant_level)}
	elif test_direction=='single':
		z_significant_level_value=abs(scipy.stats.norm.isf(1-significant_level))
		return {'z_statistics':(z_statistics(),z_significant_level_value),'p_value':(p_value_z_statistics(),significant_level)}
	else:
		print('wrong parameter! Check test_direction!')

def single_population_variance_hypothesis_testing(test_direction,significant_level,sample_size,sample_variance,population_variance):
	def chi2_statistics():
		return (sample_size-1)*sample_variance/population_variance
	def p_value_chi2_statistics():
		if test_direction=='double':
			return 2*(1-scipy.stats.chi2.cdf(chi2_statistics(),sample_size-1))
		elif test_direction=='single':
			return 1-scipy.stats.chi2.cdf(chi2_statistics(),sample_size-1)
		else:
			print('wrong parameter! Check test_direction!')
	if test_direction=='double':
		chi2_significant_level_value=abs(scipy.stats.chi2.isf(significant_level/2,sample_size-1))
		return {'chi2_statistics':(chi2_statistics(),chi2_significant_level_value),'p_value':(p_value_chi2_statistics(),significant_level)}
	elif test_direction=='single':
		chi2_significant_level_value=abs(scipy.stats.chi2.isf(significant_level,sample_size-1))
		return {'chi2_statistics':(chi2_statistics(),chi2_significant_level_value),'p_value':(p_value_chi2_statistics(),significant_level)}
	else:
		print('wrong parameter! Check test_direction!')

def double_population_mean_subtraction_hypothesis_testing(test_direction,significant_level,sampleA_size,sampleB_size,sampleA_mean,sampleB_mean,population_subtraction,population_variance,varianceA='#',varianceB='#'):
	def z_statistics():
		return abs((sampleA_mean-sampleB_mean-population_subtraction)/numpy.sqrt(varianceA/sampleA_size+varianceB/sampleB_size))
	def t_statistics_equal():
		s2p=((sampleA_size-1)*varianceA+(sampleB_size-1)*varianceB)/(sampleA_size+sampleB_size-2)
		return abs((sampleA_mean-sampleB_mean-population_subtraction)/numpy.sqrt(s2p/sampleA_size+s2p/sampleB_size))	
	def t_statistics_unequal():
		return abs((sampleA_mean-sampleB_mean-population_subtraction)/numpy.sqrt(varianceA/sampleA_size+varianceB/sampleB_size))	
	def p_value_z_statistics():
		if test_direction=='double':
			return 2*(1-scipy.stats.norm.cdf(z_statistics()))
		elif test_direction=='single':
			return 1-scipy.stats.norm.cdf(z_statistics())
	def p_value_t_statistics_equal():
		if test_direction=='double':
			return 2*(1-scipy.stats.t.cdf(t_statistics_equal(),sampleA_size+sampleB_size-2))
		elif test_direction=='single':
			return 1-scipy.stats.t.cdf(t_statistics_equal(),sampleA_size+sampleB_size-2)
	def p_value_t_statistics_unequal():
		f=int(round((varianceA/sampleA_size+varianceB/sampleB_size)**2/((varianceA/sampleA_size)**2/(sampleA_size-1)+(varianceB/sampleB_size)**2/(sampleB_size-1))))
		if test_direction=='double':
			return 2*(1-scipy.stats.t.cdf(t_statistics_unequal(),f-1))
		elif test_direction=='single':
			return 1-scipy.stats.t.cdf(t_statistics_unequal(),f-1)
	if (sampleA_size<30 or sampleB_size<30) and population_variance=='unknown':
		if test_direction=='double':
			t_significant_level_value=abs(scipy.stats.t.isf(significant_level/2,(varianceA/sampleA_size+varianceB/sampleB_size)**2/((varianceA/sampleA_size)**2/(sampleA_size-1)+(varianceB/sampleB_size)**2/(sampleB_size-1))))
			return {'t_statistics':(t_statistics_unequal(),t_significant_level_value),'p_value':(p_value_t_statistics_unequal(),significant_level)}
		elif test_direction=='single':
			t_significant_level_value=abs(scipy.stats.t.isf(significant_level,(varianceA/sampleA_size+varianceB/sampleB_size)**2/((varianceA/sampleA_size)**2/(sampleA_size-1)+(varianceB/sampleB_size)**2/(sampleB_size-1))))
			return {'t_statistics':(t_statistics_unequal(),t_significant_level_value),'p_value':(p_value_t_statistics_unequal(),significant_level)}
		else:
			print('wrong parameter! Check test_direction!')
	elif (sampleA_size<30 or sampleB_size<30) and population_variance=='equal':
		if test_direction=='double':
			t_significant_level_value=abs(scipy.stats.t.isf(significant_level/2,sampleA_size+sampleB_size-2))
			return {'t_statistics':(t_statistics_equal(),t_significant_level_value),'p_value':(p_value_t_statistics_equal(),significant_level)}
		elif test_direction=='single':
			t_significant_level_value=abs(scipy.stats.t.isf(significant_level,sampleA_size+sampleB_size-2))
			return {'t_statistics':(t_statistics_equal(),t_significant_level_value),'p_value':(p_value_t_statistics_equal(),significant_level)}
		else:
			print('wrong parameter! Check test_direction!')
	elif  (sampleA_size>=30 and sampleB_size>=30) or population_variance=='known':
		if test_direction=='double':
			z_significant_level_value=abs(scipy.stats.norm.isf(1-significant_level/2))
			return {'z_statistics':(z_statistics(),z_significant_level_value),'p_value':(p_value_z_statistics(),significant_level)}
		elif test_direction=='single':
			z_significant_level_value=abs(scipy.stats.norm.isf(1-significant_level))
			return {'z_statistics':(z_statistics(),z_significant_level_value),'p_value':(p_value_z_statistics(),significant_level)}
		else:
			print('wrong parameter! Check test_direction!')
	else:
		print('wrong parameter! Check population_standard_deviation!')
	
def double_population_proportion_subtraction_hypothesis_testing(test_direction,significant_level,sampleA_size,sampleB_size,sampleA_proportion,sampleB_proportion,population_proportion_subtraction):
	if population_proportion_subtraction==0:
		p=(sampleA_proportion*sampleA_size+sampleB_proportion*sampleB_size)/(sampleA_size+sampleB_size)
		z_statistics=(sampleA_proportion-sampleB_proportion)/numpy.sqrt(p*(1-p)*(1/sampleA_size+1/sampleB_size))
		z_significant_level_value=abs(scipy.stats.norm.isf(1-significant_level))
		if test_direction=='double':
			return {'z_statistics':(z_statistics,z_significant_level_value),'p_value':(2*(1-scipy.stats.norm.cdf(z_statistics)),significant_level)}
		elif test_direction=='single':
			return {'z_statistics':(z_statistics,z_significant_level_value),'p_value':(1-scipy.stats.norm.cdf(z_statistics),significant_level)}
		else:
			print('wrong parameter! Check test_direction!')
	elif population_proportion_subtraction!=0:
		z_statistics=abs((sampleA_proportion-sampleB_proportion-population_proportion_subtraction)/numpy.sqrt(sampleA_proportion*(1-sampleA_proportion)/sampleA_size+sampleB_proportion*(1-sampleB_proportion)/sampleB_size))
		z_significant_level_value=abs(scipy.stats.norm.isf(1-significant_level))
		if test_direction=='double':
			return {'z_statistics':(z_statistics,z_significant_level_value),'p_value':(2*(1-scipy.stats.norm.cdf(z_statistics)),significant_level)}
		elif test_direction=='single':
			return {'z_statistics':(z_statistics,z_significant_level_value),'p_value':(1-scipy.stats.norm.cdf(z_statistics),significant_level)}
		else:
			print('wrong parameter! Check test_direction!')

def double_population_variance_proportion_hypothesis_testing(test_direction,significant_level,sampleA_size,sampleB_size,sampleA_variance,sampleB_variance,population_variance_proportion):
	f_statistics=(sampleA_variance/sampleB_variance)*(1/population_variance_proportion)
	if test_direction=='double':
		return {'f_statistics':(1/abs(scipy.stats.f.isf(significant_level/2,sampleB_size-1,sampleA_size)),f_statistics,abs(scipy.stats.f.isf(significant_level/2,sampleA_size-1,sampleB_size)))}
	elif test_direction=='single':
		return {'f_statistics':(1/abs(scipy.stats.f.isf(significant_level,sampleB_size-1,sampleA_size)),f_statistics,abs(scipy.stats.f.isf(significant_level,sampleA_size-1,sampleB_size)))}
	else:
		print('wrong parameter! Check test_direction!')

def double_population__mean_subtraction_hypothesis_testing_matched_sample(test_direction,significant_level,sample_size,sample_subtraction_mean,sample_subtraction_standard_deviation,population_subtraction_mean):
	if sample_size<30 and test_direction=='single':
		return (population_subtraction_mean+scipy.stats.t.isf(significant_level,sample_size-1)*sample_subtraction_standard_deviation/numpy.sqrt(sample_size),population_subtraction_mean)
