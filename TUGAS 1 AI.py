import numpy as np
import matplotlib.pyplot as plt
import math as math

def rumus(x_1,x2):
    f=-(np.absolute(np.sin(x_1)*np.cos(x2)*math.exp(np.absolute(1-(np.sqrt((x_1**2)+(x2**2)))/3.14))))
    return f
x_1=0
x2=0
CS=rumus(x_1,x2)
print(CS)
BSF=CS
result=BSF
T= 1000
for i in range(T):
    x_1=x_1+(np.random.uniform(0,1)*4-2)
    if x_1>10:
         x_1=-10
    elif x_1<-10:
         x_1=-10
    x2=x2+(np.random.uniform(0,1)*2-1)
    if x2>10:
         x2=-10
    elif x2<-10:
         x2=-10
    NS=rumus(x_1,x2)
    delE=CS-NS
    if delE>0:
        CS=NS
        BSF=CS
        if result > BSF:
            result=BSF
            nilai1=x_1
            nilai2=x2
            suhu=T
            iterasi=i+1
    elif delE<=0:
        p=math.exp(-delE/T)
        bilacak=np.random.uniform(0,1)
        if bilacak<p:
            CS=NS       
        T=T*0.99
    plt.scatter(x_1,BSF)
    print("iterasi ",i+1)
    print("Suhu        =>",T)
    print("nilai X1    =>",x_1)
    print("nilai X2    =>",x2)
    print("Best So Far =>", BSF)
    print("=====================================")
print("=====================================")
print("Iterasi       =>",iterasi)
print("nilai X1      =>",nilai1)
print("nilai X2      =>",nilai2)
print("NILAI MINIMUM =>", result) 
  
#rangevis1 = np.arange(-10,10,0.05)
#rangevis2 = np.arange(-10,10,0.05)
#x_1,x2 = np.meshgrid(rangevis1,rangevis2)
#fm=np.zeros(x_1.shape)
#for i in range(x_1.shape[0]):
#    for j in range(x_1.shape[0]):
#          fm[i][j]= rumus(x_1[i][j],x2[i][j])
#        
#plt.figure(num=None, figsize=(5,5), dpi=100)
#vis=plt.contour(x_1,x2,fm)
#plt.clabel(vis,inline=1,fontsize=10)
#plt.show()
   
    