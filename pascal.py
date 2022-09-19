import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
def ncr(a):
    l=[]
    f=math.factorial
    for i in range(0,a+1):
        l.append(f(a)//(f(i)*f(a-i)))
    return l
s=int(input("enter number of sides"))
k=int(input("enter k value"))
t=[]
T=[]
M=[]
a=np.array([0])
for i in range(1,s+1):
    t.append(float(input("enter value"+str(i)+"of T")))
    T.append(float(input("enter value"+str(i)+"of T*")))
    M.append(float(input("enter value"+str(i)+"of M")))
t.append(t[0])
T.append(T[0])
M.append(M[0])
print(t)
t=np.array(t)
T=np.array(T)
M=np.array(M)
a=((M**2)*(T*3)*(t*3))-(2*k*((T**2)*(t**2)))+((k**2)*T*t)
l=np.array(ncr(s))
a=a*l
a=a/(2**(s-1))
y1=[i for i in range(s)]
y1.append(0)
y1=np.array(y1)
plt.plot(a,y1,color='blue')
plt.show()