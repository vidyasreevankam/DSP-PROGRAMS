import random
import numpy as np
a=int(input('enter no of rows in matrix A:'));
b=int(input('enter no of cols in matrix A:'));
c=int(input('enter no of rows in matrix B:'));
d=int(input('enter no of cols in matrix B:'));
if (b!=c):
	print('matrix mul is not possible');
A=[[random.random() for col in range(int(b))] for row in range(int(a))]
for i in range(int(a)):
	for j in range(int(b)):
		A[i][j]=input()
	print
B=[[random.random() for col in range(int(d))] for row in range(int(c))]
for i in range(int(c)):
	for j in range(int(d)):
		B[i][j]=input()
	print
m=np.zeros((int(a),int(d)));
for i in range(a):
	for j in range(d):
		m=np.zeros((int(a),int(d)));
		for k in range(c):
			m[i][j] += A[i][k]*B[k][j]
print(m)
#for i in range(len(A)):
#	for j in range(len(B[0])):
#		for k in range(len(B)):
#			m[i][j] += A[i][k]*B[k][j]
			


