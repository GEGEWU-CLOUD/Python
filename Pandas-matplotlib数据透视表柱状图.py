
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#每个销售商在各省采购的量统计
e_file = pd.ExcelFile('./py测试目录/七月下旬入库表.xlsx')
data = e_file.parse('七月下旬入库表')
pd.set_option('display.max_columns', None)      #数据显示完全 显示最大的列数  
pt1 = pd.pivot_table(data, index=['销售商'],columns=['来源省份'],values=['入库量（吨）'],aggfunc=np.sum,margins=True)  
#数据透视表行列对来源各省入库量顿求和 后再将所有省份的吨数求和写入总计
'''
margins=True     所有求和总计
aggfunc=np.sum   对出现的吨数求和
'''       
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

#将已有的数据生成柱状图表 
pt1.plot(kind='bar')
plt.xticks(rotation=0)    
'''
pt1.plot(kind='bar')    改变图表样式只需要修改kind值  
plt.show()              显示图表  
plt.xticks(rotation=45) x轴标签旋转45度  
'''
#加上标签
plt.title('每日入库量对比')  #标题
plt.xlabel('客户')    #横坐标标题日期
plt.ylabel('入库量')  #纵坐标标题车次
plt.legend()    
plt.show()

