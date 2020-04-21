import numpy as np
import matplotlib.pyplot as plt
import math


def solve_function(x):
    ex = math.exp(x)
    return ex + 3*x**3 - 2*x**2 + x - 2;

def solve_derivatives(x):
    ex = math.exp(x)
    return ex + 9*x**2 - 4*x + 1;

def function_diedai(x):
    ex = math.exp(x)
    return ((2*x**2-x+2-ex)/3)**(1/3);
def Newton(x,eps):
    print("牛顿法：")
    print('n--------x--------y')
    count = 0;
    while abs(solve_function(x))>eps:
        x = x-solve_function(x)/solve_derivatives(x)
        count = count+1
        print("%d----%8.6f----%8.6f"%(count,x,solve_function(x)))
    return count,x
def SimpleIteration(x0, eps):
    print("迭代法：")
    print('n--------x--------y')
    count = 0;
    x1 =function_diedai(x0)
    print("%d----%8.6f----%8.6f" % (count, x0, x1))
    while abs(x1 - x0)>eps:
        x0 =x1
        x1 = function_diedai(x0)
        count = count + 1
        print("%d----%8.6f----%8.6f"%(count,x0,x1))
    return count,x1
def dichotomy(left,right,eps):
    print("二分法：")
    print('n--------a--------b-------x-------y')
    middle = (left+right)/2
    count = 0
    while abs(solve_function(middle))>eps:
        middle = (left+right)/2
        if solve_function(left)*solve_function(middle)<=0:
            right = middle
        else:
            left = middle
        count = count+1
        print("%d---%8.6f----%8.6f---%8.6f---%8.6f"
              %(count,left,right,middle,solve_function(middle)))
    return count,middle

left = 0
right = 1
eps = 0.0001
Binary_count,answer = dichotomy(left,right,eps)
print("迭代%d次得到的根是%f"%(Binary_count,answer))

x = 0.5
eps = 0.0001
SimpleIteration_count,answer = SimpleIteration(x,eps)
print("迭代%d次得到的根是%f"%(SimpleIteration_count,answer))

x = 0.5
eps = 0.0001
Newton_count,answer = Newton(x,eps)
print("迭代%d次得到的根是%f"%(Newton_count,answer))


x = np.linspace(0,1,1000)
ex = np.exp(x)
y = ex + 3*x**3 - 2*x**2 +x - 2
plt.figure(figsize=(8,4))
plt.plot(x,y,"red",linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


N = 11
epss = [0.1**x for x in range(1, N)]
left = 0
right = 1
Binary_count = []
SimpleIteration_count = []
Newton_count = []
for eps in epss:
    count, ans = dichotomy(left, right, eps)
    Binary_count.append(count)AA
    count, ans = Newton(0.5, eps)
    Newton_count.append(count)
    count, ans = SimpleIteration(0.5, eps)
    SimpleIteration_count.append(count)

# 画图比较三种方法的性能
number=[x for x in range(1,N)]
plt.figure(figsize=(8,6))
line1,=plt.plot(number,Binary_count, label="Line 1",color="red",linewidth=2)
line2,=plt.plot(number,Newton_count, label="Line 2",color="blue",linewidth=2)
line3,=plt.plot(number,SimpleIteration_count, label="Line 3",color="green",linewidth=2)
l1 = plt.legend([line1, line2,line3], ["Binary", "NewtonIteration","SimpleIteration"], loc='upper left')
plt.xlabel("-lg(error)")
plt.ylabel("iterations")
