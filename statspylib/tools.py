import numpy

def compute_standard_deviation(data_list):
	return numpy.sqrt(sum([(x-numpy.mean(data_list))**2 for x in data_list])/(len(data_list)-1))
	
def compute_variance(data_list):
	return sum([(x-numpy.mean(data_list))**2 for x in data_list])/(len(data_list)-1)