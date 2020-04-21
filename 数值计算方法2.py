# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == 2:
        return x * x
    elif n == 3:
        return x * x * x
    elif n == 4:
        return np.exp(x)
    elif n == 5:
        return np.log(x)

X = np.mat([[1,1.4,1.8,2.2,2.6,3,3.4,3.8,4.2,4.6,5.0]])
Y = np.mat([[4.7187,9.4496,13.3248,16.0722,17.4894,17.5794,16.6755,15.6332,16.0858,20.8430,34.4605]])
D = np.mat(np.zeros((6,6)))
F = np.mat(np.zeros((1,6)).T)

for k in range(0, 6):
    for i in range(0, 6):
        for j in range(0, 11):
            D[k, i] = f(X[0, j], k) * f(X[0, j], i) + D[k, i]
for l in range(0, 6):
    for m in range(0, 11):
        F[l, 0] = f(X[0, m], l) * Y[0, m] + F[l, 0]

ans = np.around(D.I * F, decimals = 2)
print(ans)

plt.figure(figsize=(9,6),dpi=100)
X = [1,1.4,1.8,2.2,2.6,3,3.4,3.8,4.2,4.6,5.0]
Y = [4.7187,9.4496,13.3248,16.0722,17.4894,17.5794,16.6755,15.6332,16.0858,20.8430,34.4605]
plt.plot(X,Y,'o',color = 'b',label='scatter')
x = np.linspace(0,5,200)
y = ans[0][0]+ans[1][0]*f(x,1)+ans[2][0]*f(x,2)+ans[3][0]*f(x,3)+ans[4][0]*f(x,4)+ans[5][0]*f(x,5)
plt.plot(x,y,color = 'g',label='fitting curve')
plt.legend()
plt.show()

def function(x):
    return -2.01+1.01*x+5*x*x-2*x*x*x+1*math.exp(x)+4.99*math.log(x)
print("x-------------拟合值--------------真实值-------------差")
for i in range(0, 11):
    print("%f------%f----------%f--------%f"%(X[i], Y[i], function(X[i]), Y[i]-function(X[i])))
    








            
