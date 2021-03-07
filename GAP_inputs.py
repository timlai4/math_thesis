# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:15:50 2020

@author: Tim
"""

from functools import reduce

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def gcd_vec(*args):
    return reduce(gcd, args)

# Make commands to type into GAP to test equality of groups in case D.
def SymGrpConstructor(n, d):
    m = 2*d*n
    a = [str(i+1) for i in range(3*m)]
    x = 'x:=(' + ",".join(a[:m]) + ");"
    y = 'y:=(' + ",".join(a[m:2*m]) + ");"
    z = 'z:=(' + ",".join(a[2*m:3*m]) + ");"
    sigma = [str((i, m + i, 2*m + i)) for i in range(1, m + 1)]
    sigma = "*".join(sigma)
    tau = [str((i, m + i)) for i in range(1, m + 1)]
    tau = "*".join(tau)
    print("m:=" + str(m) + ";;")
    print("g:=SymmetricGroup(3*m);;")
    print(x)
    print(y)
    print(z)
    print("sigma:=" + sigma + ";")
    print("tau:=" + tau + ";")
    
def groups(D_final):
    assert len(D_final) == 1
    test = []
    index = 1
    for value in D_final.values():
        for a, b, r, s in value:
            if gcd_vec(r, 2*r, 2*r+s) > 1:
                continue
            print("a:=" + str(a) + ";;" + "b:=" + str(b) + ";;" + "r:=" + str(r) + ";;" + "s:=" + str(s) + ";;")
            print("first:=x^(4*r*n) * y^(r*n) * z^(r*n);; second:=x^(2*a*d) * y^(2*b*d) * z^(-2*d*(a+b));; third:=x^((4*r+2*s) * 2*n) * y^(-n*(2*r + s)) * z^(-n*(2*r + s));;")
            print("u" + str(index) + ":=Subgroup(g, [first, second, third, sigma, tau]);")
            index += 1
            test.append([a,b,r,s])
    isom_test = ["IsomorphismGroups(u1,u"+ str(i) + ");" for i in range(2, index)]
    return isom_test, test

SymGrpConstructor(1, 12)
D_final = {} # Fill out
isom_test, test = groups(D_final)
if len(isom_test) == 0:
    print("Nothing to test!")
for string in isom_test:
    print(string)
print(test)