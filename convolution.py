import numpy as np
l1=int(input("length1"))
l2=int(input("length2"))
x=np.zeros(l1)
h=np.zeros(l2)
c=l1+l2-1
y=np.zeros(c)
for i in range(0,l1):
	x[i]=input("")
for i in range(0,l2):
	h[i]=input("")
for n in range(0,c):
	p=0
	for k in range(0,l1):
		if (n-k>=0 and n-k<l2):
			p=p+x[k]*h[n-k]
		y[n]=p
		

