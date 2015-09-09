from statspylib.VarianceAnalysis.ANOVA import *

import numpy as np
import pandas as pd

retail=[57,66,49,40,34,53,44]
tourism=[68,39,29,45,56,51]+[np.NaN]*1
aircraft=[31,49,21,34,40]+[np.NaN]*2
manufacturing=[44,51,65,77,58]+[np.NaN]*2
data1=pd.DataFrame({'retail':retail,'tourism':tourism,'aircraft':aircraft,'manufacturing':manufacturing},columns=['retail','tourism','aircraft','manufacturing'])
a=One_Way_ANOVA(data1)
a.ANOVA()
print()

area1=[365,345,358,288]
area2=[350,368,323,280]
area3=[343,363,353,298]
area4=[340,330,343,260]
area5=[323,333,308,298]
data2=pd.DataFrame({'area1':area1,'area2':area2,'area3':area3,'area4':area4,'area5':area5},columns=['area1','area2','area3','area4','area5'],index=['brand1','brand2','brand3','brand4'])
data2.columns.name='area factor'
data2.index.name='brand factor'
b=Two_Way_ANOVA(data2)
b.ANOVA()
print()

road1=[26,24,27,25,25,20,17,22,21,17]
road2=[19,20,23,22,21,18,17,13,16,12]
data3=pd.DataFrame({'road1':road1,'road2':road2},columns=['road1','road2'],index=['peak']*5+['nopeak']*5)
c=Two_Way_ANOVA(data3,interaction=True)
c.ANOVA()