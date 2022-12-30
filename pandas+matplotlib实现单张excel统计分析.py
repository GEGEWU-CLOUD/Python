import pandas as pd
import matplotlib.pyplot as plt

file_path = './py测试目录/七月下旬入库表.xlsx'  
tr = pd.read_excel(file_path).head(40)['日期'].tolist()          #截取表头（列名）为日期的前六行
tr1 = pd.read_excel(file_path).head(40)['入库量（吨）'].tolist()  #截取表头（列名）为入库量（吨）的前六行
print(tr)
print(tr1)

###柱状图###
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.plot(tr, tr1, color='yellow', label='入库量（吨）')
plt.title('每日入库量对比')  #标题
plt.xlabel('日期')  #横坐标标题日期
plt.ylabel('吨')    #纵坐标标题车次
plt.legend()        #把标签刻印出来
plt.show()
