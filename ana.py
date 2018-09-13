import matplotlib as mb
from matplotlib import pyplot
import numpy as np
from pylab import mpl
import random 
y = []
# mpl.rcParams['font.sans-serif'] = ['SimHei']
def entropy(k=2,dis='blance'):
    if(dis=='blance'):
        return -k*(1/k)*np.emath.log2(1/k)

def plot_func(func,domain):
    x = np.linspace(domain[0],domain[1],30)
    funcy = np.frompyfunc(func,1,1)
    y =  funcy(x)
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    # pyplot.scatter(x,y)
    pyplot.plot(x,y)
    pyplot.show()

def plot_sca(x,y):
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.scatter(x,y)
    # pyplot.plot(x,y)
    pyplot.show()

def get_ROC(distribute=(0,0,0,0,0,0,0,1,1,1,1,1,1),title=''):
     TPR_list = []
     FPR_list = []
     positive = distribute.count(1)
     negative = distribute.count(0)
     for i in range(len(distribute)+1):
         tpr = distribute[0:i].count(1)/positive
         print(i,tpr)
         fpr = distribute[0:i].count(0)/negative
         TPR_list.append(tpr)
         FPR_list.append(fpr)
     print(FPR_list)
     print(TPR_list)
     pyplot.xlabel("FPR")
     pyplot.ylabel("TPR")
     pyplot.title(title)
     pyplot.plot(FPR_list,TPR_list)
     pyplot.show()
def f_huigui(x,k=2,b=0):
    a = ((random.random()-0.5)/2+k)*x+b
    y.append(a)
    return a
if __name__ == '__main__':
    import math
    # x = list(range(1,30))
    
    # y2 =[(math.e)**a for a in y1]
    # plot_sca(x,y2)
    # plot_sca(x,y1)
    ax = pyplot.gca()   
    ax.spines['right'].set_color('none') 
    ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边

    ax.xaxis.set_ticks_position('bottom')   
    ax.yaxis.set_ticks_position('left')   
    
    ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    ax.spines['left'].set_position(('data', 0))   
    f = lambda x:0.1*x+0.02
    g = lambda x:math.e**f(x)
    j = lambda x:1/(1+math.e**(-x))
    plot_func(j,(-10,10))
    # plot_func(f,(1,20))
    # plot_func(g,(1,20))
    # get_ROC([0]*20+[1]*20,"完全错误ROC曲线")
    # get_ROC([1,0]*20,"随机预测ROC曲线")
    # get_ROC([1]*20+[0]*20,"随机预测ROC曲线")
    # plot_func(f_huigui,(1,100))
    # plot_func(entropy,(1,8))
    # pyplot.show()
