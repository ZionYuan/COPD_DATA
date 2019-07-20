'''
@Description: 
@Author: YuanZi
@Github: https://github.com/yzmean
@Date: 2019-07-20 15:09:36
@LastEditTime: 2019-07-20 15:18:53
'''
import pandas as  pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
from pylab import mpl
from scipy.stats import kstest
from matplotlib.backends.backend_pdf import PdfPages
from tqdm import tqdm


mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 150 #分辨率

import os 
t = list(os.walk('/Users/yuanzi/学习/yz/COPD/COPD_DATA/olds_modification'))[0][2]
t.sort()
count = 0
ln=[]

features = ['体温','呼吸率','脉率','血压(低)','血压(高)','血氧饱和度']
for feature in features:
    with PdfPages(feature+'散点图.pdf') as pdf:
        with tqdm(t[1:20]) as tt:
            for fname in tt:
                try:
                    df = pd.read_csv('/Users/yuanzi/学习/yz/COPD/COPD_DATA/olds_modification/'+fname
                                    ,usecols=[0,1,3,5,6,7,8])
                    df.dropna(axis=0, how='any', inplace=True)
                    df['ind'] = range(df.shape[0])

                    dic = df.boxplot(column=feature,figsize=(20,8),return_type = 'dict')

                    exception_list = list(dic['fliers'][0].get_ydata())

                    df2 = df[df[feature].isin(exception_list)]
                    #print(df2)

                    ax = df.plot.scatter(x='ind',y=feature,figsize=(20,8),label='正常值',color='b',title = fname+'-'+feature)
                    df2.plot.scatter(x='ind',y=feature,figsize=(20,8),label='异常值',ax=ax,color='r')
                    #print(df)
                    #plt.show()
                    pdf.savefig()
                    plt.close()
                except Exception:
                    print(fname)
