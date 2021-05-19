import matplotlib.pyplot as plt  #添加matplotlib 库，用来输出信号
import numpy as np      #添加numpy库，用于计算
x=np.linspace(0,3*(np.pi),100)  #在0到3*pi当中等分采样100个点
y=np.sin(x)     #生成正弦信号
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

plt.subplot(1,2,1)#生成图像，一共一行两列
plt.title('正弦函数')#注释信号
plt.plot(x,y)#划线

x1=[t*0.375*np.pi for t in x]#for t in x，将t遍历x,生成x1
y1=np.sin(x1)#生成y1图像

plt.subplot(1,2,2)#生成图像，第二个图像
plt.title('正弦函数1')#注释信号
plt.plot(x1,y1)#生成信号
plt.show()

