# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:15:50 2020

@author: Tim
"""

# Make commands to type into GAP to test equality of groups in case D.
def GAP(n, d):
    m = 2*d*n
    a = [str(i+1) for i in range(3*m)]
    x = 'x:=(' + ",".join(a[:m]) + ");"
    y = 'y:=(' + ",".join(a[m:2*m]) + ");"
    z = 'z:=(' + ",".join(a[2*m:3*m]) + ");"
    sigma = [str((i, m + i, 2*m + i)) for i in range(1, m + 1)]
    sigma = "*".join(sigma)
    tau = [str((i, m + i)) for i in range(1, m + 1)]
    tau = "*".join(tau)
    print(x)
    print(y)
    print(z)
    print("sigma:=" + sigma + ";")
    print("tau:=" + tau + ";")
    
GAP(1, 6)
