from statspylib.MultivariateStatistics.PCA import *

import numpy as np

p=np.matrix([[2,1,5,2,3,4,4,1,3,5],[4,5,3,2,5,3,4,2,3,5],[5,1,4,3,5,2,3,1,2,3]]).T
PCA(p,2,normalize=True)