import numpy as np
import scipy.sparse
def M():
    M=np.zeros((2000,2000),dtype=np.int64)
    M[0,1998:2000]=1
    for i in range(1,2000):
        M[i,i-1]=1
    return M
def calc(k):
    n=k-1999
    powers=bin(n)[2:][::-1]
    i=0
    current=M()
    res=np.identity(2000,dtype=np.int64)
    while i<len(powers):
        print(i,len(powers))
        if powers[i]=="1":
            res= np.mod(current @ res, 20092010 )
        current=current @ current
        current= np.mod(current, 20092010 )
        i+=1
    return np.sum(res[0])%20092010




print(calc(10**18))