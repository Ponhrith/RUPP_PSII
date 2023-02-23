from tabulate import tabulate
def mean(ls):
    return (sum(ls)/len(ls))
def lsl(x,y):
    x_deviation = [u-mean(x) for u in x]
    y_deviation = [u-mean(y) for u in y]
    multi = [x_deviation[i] * y_deviation[i] for i in range(0, len(x))]
    squared_deviation = [((u-mean(x))**2)for u in x]
    b = sum(multi)/sum(squared_deviation)
    a = mean(y) - (b*mean(x))
    return (a,b)
x = [6.94,5.23,5.21,7.10,8.16,5.50,9.19,9.05,9.36]
y = [0.00,6.13,11.29,14.35,12.03,22.72,20.11,26.11,30.65]
n = len(x)
#call function lsl
a,b = lsl(x,y)
#prediction value
y_hat = [round((a+(b*i)),4) for i in x]
#Residual
residual = [round((y[i]-y_hat[i]),4) for i in range(n)]
#SSResid sum((y-y_hat)^2)
SSResid = sum([(y[i]-y_hat[i])**2 for i in range(n) ])
#SSTo sum((y-y_mean)^2)
y_mean = mean(y)
SSTo = sum([(y[i] - y_mean)**2 for i in range(n)])
r_square = round((1-(SSResid/SSTo))*100,2)
se = round((SSResid/(n-2))**0.5,4)
#table
data = list(zip(x,y,y_hat,residual))
data_table = tabulate(data,headers=["x","y","predicted_value","residual"])
print(data_table)
print(f'r^2 = {r_square}%')
print(f'se = {se}')