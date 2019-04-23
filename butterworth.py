import numpy as np
from matplotlib import pyplot as plt
import cmath
t=0.1#sec
#omegap=(input('enter omegap'))
#omegas=(input('enter omegas'))
#3delp=(input('enter delp'))
#dels=(input('enter dels'))
omegap=0.35*3.14
omegas=0.7*3.14
delp=0.6
dels=0.1
p1=omegap/2
aomegap=(2/t)*(np.tan(p1))
print(aomegap)
p2=omegas/2
aomegas=(2/t)*(np.tan(p2))
print(aomegas)
p3=(dels**-2)-1
p4=(delp**-2)-1
p5=(p3/p4)**0.5#nr
p6=aomegap/aomegas
p7=np.log(p5)
p8=np.log(p6)
p9=p7/p8
p91=np.abs(p9)
p10=np.ceil(p91)#order
print(p10)
p11=0.5/p10
aomegac=aomegas/(p3**p11)#cuttoff
print(aomegac)
k=p10/2
p12=(2*k)-1
p13=(p12*3.14)/(2*p10)
bk=2*np.sin(p13)
print(bk)
j=cmath.sqrt(-1)
w=np.arange(0,np.pi,0.01)
z=np.exp(j*w)
#p14=1-(1/(np.exp(j*w)))#s nr
#p15=1+(1/(np.exp(j*w)))
s=(2/0.1)*((z-1)/(z+1))
print(s)
h=(aomegac**2)/((s**2)+(bk*aomegac*s)+(aomegac**2))
print(h)
plt.plot(w,np.abs(h))
plt.show()
