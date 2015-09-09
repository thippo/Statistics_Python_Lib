from numpy import *

def PCA(dataMat,topNfeat, normalize=True):
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals #减去均值
    if normalize:
        stded = meanRemoved / std(dataMat) #用标准差归一化
        covMat = cov(stded, rowvar=0) #求协方差方阵
        eigVals, eigVects = linalg.eig(mat(covMat)) #求特征值和特征向量
        print(covMat)
        print(eigVals)
        print(eigVects)
        eigValInd = argsort(eigVals)  #对特征值进行排序
        eigValInd = eigValInd[:-(topNfeat + 1):-1]  
        redEigVects = eigVects[:, eigValInd]       # 除去不需要的特征向量
        lowDDataMat = stded * redEigVects    #求新的数据矩阵
        #reconMat = (lowDDataMat * redEigVects.T) * std(dataMat) + meanVals
        #return lowDDataMat, reconMat
        return lowDDataMat
    else:
        stded=meanRemoved
        covMat = cov(stded, rowvar=0) #求协方差方阵
        print(covMat)
        eigVals, eigVects = linalg.eig(mat(covMat)) #求特征值和特征向量
        eigValInd = argsort(eigVals)  #对特征值进行排序
        eigValInd = eigValInd[:-(topNfeat + 1):-1]  
        redEigVects = eigVects[:, eigValInd]       # 除去不需要的特征向量
        lowDDataMat = stded * redEigVects    #求新的数据矩阵
        #reconMat = (lowDDataMat * redEigVects.T) * std(dataMat) + meanVals
        #return lowDDataMat, reconMat
        return lowDDataMat
