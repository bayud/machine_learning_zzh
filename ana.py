import matplotlib as mb
from matplotlib import pyplot
import numpy as np

def entropy(k=2,dis='blance'):
    if(dis=='blance'):
        return -k*(1/k)*np.emath.log2(1/k)

def plot_func(func,domain):
    x = np.linspace(domain[0],domain[1],500)
    funcy = np.frompyfunc(func,1,1)
    y =  funcy(x)
    pyplot.plot(x,y)

def get_ROC(distribute=(0,0,0,0,0,0,0,1,1,1,1,1,1)):
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
     pyplot.plot(FPR_list,TPR_list)
     pyplot.show()
if __name__ == '__main__':
    get_ROC([0]*20+[1]*20)
    # plot_func(entropy,(1,8))
    # pyplot.show()
