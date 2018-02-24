import numpy as np
import matplotlib.pyplot as plt
from time import time

def fib_req(n):
    if n < 2:
        return n
    return fib_req(n-2) + fib_req(n-1)

def loop_fib(n):
 	a,b = 1,1
 	for i in range(n-1):
 		a,b = b,a+b
 	return a

n = int(raw_input("n value: "))
array1 = []
array2 = []
arrayx = []

for i in range(1,n+1):
	arrayx.append(i)

for i in range(1,n+1):
	start = time()
	num = fib_req(i)
	ntime = time() - start
	array1.append(ntime)

	start = time()
	num = loop_fib(i)
	ntime = time() - start
	array2.append(ntime)

plt.figure(figsize=(12,5))
plt.bar(arrayx, array1)
plt.xticks(arrayx,arrayx)
plt.ylabel('Results')
plt.xlabel('Entries')
plt.title('Reqursive Function of Ficonacci')
plt.show()

plt.figure(figsize=(12,5))
plt.bar(arrayx, array2)
plt.xticks(arrayx,arrayx)
plt.ylabel('Results')
plt.xlabel('Entries')
plt.title('Loop Function of Ficonacci')
plt.show()

# alternative
#	print "num=" , num
#	print "%f reqursive " % (time() - start)
#	print int(time() - start) * "-"