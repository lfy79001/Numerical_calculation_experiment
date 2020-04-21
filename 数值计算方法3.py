# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt

def f(x):
    return math.sqrt(x-3*x*x+2*x*x*x+math.exp(x))


def ReiterationOfSimpson(a, b, n):
    h = (b - a) / n
    fa = f(a)
    fb = f(b)
    s1 = 0.0
    s2 = 0.0
    for k in range(1, n):
        xk = a + k * h
        s1 = s1 + f(xk)
    for j in range(0, n):
        xj = a + (j + 0.5) * h
        s2 = s2 + f(xj)
    sn = h / 6 * (fa + fb + 2 * s1 + 4 * s2)
    return sn

def Cotes(a, b, n):
    h = (b - a) / n
    fa = f(a)
    fb = f(b)
    s1 = 0.0
    s2 = 0.0
    s3 = 0.0
    s4 = 0.0
    for k in range(1, n):
        xk = a + k * h
        s1 = s1 + f(xk)
    for j in range(0, n):
        xj = a + (j + 0.5) * h
        s2 = s2 + f(xj)
    for t in range(0, n):
        xt = a + (t + 0.25) * h
        s3 = s3 + f(xt)
    for w in range(0, n):
        xw = a + (w + 0.75) * h
        s4 = s4 + f(xw)
    sn = h / 90 * (7*fa+32*s3+12*s2+32*s4+14*s1+7*fb)
    return sn

def Trapezoid(a, b, n):
    h = (b - a) / n
    fa = f(a)
    fb = f(b)
    s1 = 0.0
    for k in range(1, int(n)):
        xk = a + k * h
        s1 = s1 + f(xk)
    sn = h / 2 *(fa + 2 * s1 + fb)
    return sn

value_Simpson = []
value_Cotes = []
value_Trapezoid = []

n = 2
h = 1 / n
S = []
i = 0
print("===============复合Simpson公式法=============\n\n")
print("迭代步数\t步长\t积分数值\t\t误差\n")
S.append(ReiterationOfSimpson(0, 2, n))
print("%d\t%f\t%f\n"%(n, h, S[0]))
value_Simpson.append(S[0])
n = n + 1
h = 1 / n
S.append(ReiterationOfSimpson(0, 2, n))
print("%d\t%f\t%f\t%f\n"%(n, h, S[1], S[1] - S[0]))
value_Simpson.append(S[1])
i = 2
while(abs(S[i-1] - S[i-2]) >=1e-5):
    n = i + 2
    h = 1 / n
    S.append(ReiterationOfSimpson(0, 2, n))
    print("%d\t%f\t%f\t%f\n"%(n, h, S[i], S[i] - S[i-1]))
    value_Simpson.append(S[i])
    i = i + 1
print()
    
n = 2
h = 1 / n
s = []
i = 0
print("===============复合科茨公式法==============\n\n")
print("迭代步数\t步长\t积分数值\t\t误差\n")
s.append(Cotes(0, 2, n))
print("%d\t%f\t%f\n"%(n, h, s[0]))
value_Cotes.append(s[0])
n = n + 1
h = 1 / n
s.append(Cotes(0, 2, n))
print("%d\t%f\t%f\t%f\n"%(n, h, s[1], s[1] - s[0]))
value_Cotes.append(s[1])
i = 2
while(s[i-1] - s[i-2] >=1e-5):
    n = i + 2
    h = 1 / n
    s.append(Cotes(0, 2, n))
    print("%d\t%f\t%f\t%f\n"%(n, h, s[i], s[i] - s[i-1]))
    value_Cotes.append(s[i])
    i = i + 1
    
print()
    
n = 2
h = 1 / n
s = []
i = 0
print("===============复合梯形公式法==============\n\n")
print("迭代步数\t步长\t积分数值\t\t误差\n")
s.append(Trapezoid(0, 2, n))
print("%d\t%f\t%f\n"%(n, h, s[0]))
value_Trapezoid.append(s[0])
n = 4
h = 1 / n
s.append(Trapezoid(0, 2, n))
print("%d\t%f\t%f\t%f\n"%(n, h, s[1], s[1] - s[0]))
value_Trapezoid.append(s[1])
i = 2
while(abs(s[i-1] - s[i-2]) >=1e-5):
    n = math.pow(2.0, i + 1)
    h = 1 / n
    s.append(Trapezoid(0, 2, n))
    print("%d\t%f\t%f\t%f\n"%(n, h, s[i], s[i] - s[i-1]))
    value_Trapezoid.append(s[i])
    i = i + 1

iteration = []
for i in range(1, 10):
    iteration.append(i)

for i in range(4, 9):
    value_Cotes.append(value_Cotes[3])
for i in range(8, 9):
    value_Simpson.append(value_Simpson[3])
plt.figure(figsize=(9,6),dpi=100)
plt.plot(iteration, value_Trapezoid,color='red',label='Trapezoid')
plt.plot(iteration, value_Simpson,color='blue',label='Simpson')
plt.plot(iteration, value_Cotes,color='black',label='Cotes')
plt.legend()
plt.xlabel('n:iterations')
plt.ylabel('integral value')


    
    