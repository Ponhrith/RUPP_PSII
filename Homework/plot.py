import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
def mean(ls):
    return (sum(ls)/len(ls))
data=[
    [11,11.3],
    [12,15.1],
    [13,6.6],
    [14,12.9],
    [15,12.1],
    [17,18.1],
    [18,20.9],
    [19,17.6],
    [20,11],
    [21,24.6],
    [24,11.3],
    [25,18.4],
    [27,16.2],
    [28,19.5],
    [31,35.8],
    [32,37.1],
    [33,45.7],
    [36,34.8],
    [37,25.6],
    [38,26.7],
    [40,22],
    [41,26],
    [44,10.5],
    [45,18.6],
    [46,21.1],
    [49,11.9],
    [50,13.7],
    [51,13.7],
    [54,6.3],
    [55,1.8]
]
x =np.array([i[0] for i in data])
y =np.array([i[1] for i in data])
a,b1,b2 = np.polynomial.polynomial.polyfit(x,y,deg=2)
e = f'y={round(a,4)}{"+" if b1>0 else ""}\
{round(b1,4)}x{"+" if b2>0 else ""}{round(b2,4)}x^2'
print(e)
n = len(x)
#predict_value quadratic
predict_value = [round((a+(b1*i)+(b2*i**2)),4) for i in x]
#Residual
residual = [round((y[i]-predict_value[i]),4) for i in range(n)]
#SSResid
SSResid = sum([(y[i]-predict_value[i])**2 for i in range(n) ])
#SSTo
y_mean = mean(y)
SSTo = sum([(y[i] - y_mean)**2 for i in range(n)])
r_square = round((1-(SSResid/SSTo))*100,2)
se = round((SSResid/(n-2))**0.5,4)
data = list(zip(x,y,predict_value,residual))
data_table = tabulate(data,headers=["x","y","predicted_value","residual"])
print(data_table)
print(f'r^2 = {r_square}%')
print(f'se = {se}')
plt.figure(figsize=(10,4))
ax1 = plt.subplot(1,2,1)
ax1.scatter(x,y)
ax1.plot(x,(a+b1*x+b2*(x**2)),'-',c='r',label=r'$\hat{y} = a + b_1x + b_2x^2$')
ax1.legend()
ax1.set_title('Data')
ax1.set_xlabel('Date')
ax1.set_ylabel('Fishing Time')
ax2 = plt.subplot(1,2,2)
ax2.scatter(x,residual,label=r'$x,residual$')
ax2.legend()
ax2.set_title('x, residual plot')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.show()