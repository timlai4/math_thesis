# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:08:04 2020

@author: Tim

Similar to diagonal_elements.py, we apply rationality condition
to find the possible subgroups in the scalar embedding case.
"""

import collections
import json
import pickle
from functools import reduce
from itertools import product, groupby

def compare(list1,list2):
    return collections.Counter(list1) == collections.Counter(list2)

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
#  return abs(a) if b==0 else gcd(b, a%b)
def gcd_vec(*args):
    return reduce(gcd, args)

generators = {1: [1], 2: [1], 3: [2], 4: [3], 5: [2], 6: [5], 7: [3], 8: [3,5], 
              9: [2], 10: [3], 11: [2], 12: [5,7], 13: [2], 14: [3], 
              15: [2, 14], 16: [3, 15], 17: [3], 18: [5], 19: [2], 20: [3,19], 
              21: [2,20], 22: [7], 23: [5], 24: [5,7,13], 25: [2], 26: [7], 
              27: [2], 28: [3,13], 29: [2], 30: [7,11], 31: [3], 32: [3,31], 
              33: [2,10], 34: [3], 35: [2,6], 36: [5,19], 42: [5, 13], 
              48: [5, 7, 47], 54: [5], 56: [3, 13, 29], 63: [2, 5], 72: [5, 7, 19], 
              84: [5, 11, 13], 96: [5, 7, 31], 108: [5, 107], 126: [5, 13],
              144: [5, 7, 13], 162: [5], 216: [5, 7, 13], 252: [5, 11, 13], 
              288: [5, 7, 13], 324: [5, 7], 378: [5, 11, 13], 432: [5, 11, 13], 
              504: [5, 11, 13, 17], 648: [5, 7, 13], 756: [5, 11, 13], 
              40: [3, 11, 39], 60: [7, 11, 19], 64: [3, 63], 90: [7, 11],
              80: [3, 7, 79], 112: [3, 5, 111], 120: [7, 11, 19, 29], 
              128: [3, 127], 168: [5, 11, 13, 17], 180: [7, 11, 13], 
              192: [5, 7, 13], 140: [3, 11, 19], 196: [3, 5], 210: [11, 13, 19],
              224: [3, 5, 11], 270: [7, 11], 240: [7, 11, 13, 17], 
              336: [5, 11, 13, 17], 360: [7, 11, 13, 17], 384: [5, 7, 13],
              540: [7, 11, 13], 576: [5, 7, 13], 420: [11, 13, 17, 19],
              588: [5, 11, 13], 630: [11, 13, 19], 672: [5, 11, 13, 17]}
# Consider the scalar embedding case.
# Classify all rational elements of the form 
#(\zeta_n^a, \zeta_n^b, \zeta_n^{-a-b}).

all_solutions = {}
for k in generators:
    R = generators[k]
    all_solutions[str(k)] = []
    for a in range(k):
        for b in range(k):  
            inv = [(a+2*b)%k,-(a+2*b)%k,(2*a+b)%k,-(2*a+b)%k,(a-b)%k,(b-a)%k]
            flag = True
            for r in R:
                r_inv = [(r*x)%k for x in inv]
                if not compare(inv,r_inv):
                    flag = False
                    break
            if flag:
              all_solutions[str(k)].append([a,b]) 

base = {}
for k in generators:
    R = generators[k]
#    solutions = []
    base[str(k)] = []
    for a in range(k):
        for b in range(k):  
            if gcd_vec(a, b, k) > 1:
                continue
            inv = [(a+2*b)%k,-(a+2*b)%k,(2*a+b)%k,-(2*a+b)%k,(a-b)%k,(b-a)%k]
            flag = True
            for r in R:
                r_inv = [(r*x)%k for x in inv]
                if not compare(inv,r_inv):
                    flag = False
                    break                        
            if flag:
                base[str(k)].append([a,b]) 
C = {}
for n in base:
    n = int(n)
    solutions = []
    for pair in base[str(n)]:
        a, b = pair
        flag = True
        for k in range(n):
            for l in range(n):
                if [(k*a + l*b)%n, (-l*a + (k - l)*b)%n] not in all_solutions[str(n)]:
                    flag = False
                    break
        if flag:
            solutions.append(pair)  
    C[n] = solutions


# Remove the empty values from C. 
empty_keys = [k for k,v in C.items() if len(v) == 0]
for k in empty_keys:
    del C[k]

# Not all the values in C are distinct

C_perm = {}
for n in C:
    temp = [sorted([a, b, (n - a - b)%n]) for a, b in C[n]]
    temp.sort()
    temp2 = [[x[0], x[1]] for x in temp]
    C_perm[n] = list(temp2 for temp2,_ in groupby(temp2))

C = C_perm
for n in C:
    file = open("C_grps.txt","a")
    file.write(str(n) + '\n')
    json.dump(C[n],file)
    file.write('\n')
    file.close()

# Case D

# First, analyze A
A = {}
for d in range(4, 19):
    A[d] = []
    for r in range(1, d):
        if gcd(d, r) > 1:
            continue
        k = 2*d
        G = generators[k]
        inv = [(6*r - d) % k, -(6*r - d) % k]
        count = 0
        for g in G:
            r_inv = [(g*x)%k for x in inv]
            if compare(inv,r_inv):
                count += 1
        if count==len(G):
            A[d].append(r)

empty_keys = [k for k,v in A.items() if len(v) == 0]
for k in empty_keys:
    del A[k]
            

# Bootstrap classification of C to D. 
# Analyze AF
AF = {}
for n in C:
    for d in A:
        k = 2*d*n
        R = generators[k]
        AF[(n, d)] = []
        for a, b, in C[n]:
            for r in range(d):
                x = 6*n*r + 2*a*d - 2*b*d - d*n
                y = 6*n*r + 4*a*d - d*n + 2*b*d
                z = 4*b*d + 2*a*d
                inv = [(x)%k, (-x)%k, (y)%k, (-y)%k, (z)%k, (-z)%k]
                flag = True
                for gen in R:
                    r_inv = [(gen*w)%k for w in inv]
                    if not compare(inv, r_inv):
                        flag = False
                        break
                if flag:
                    AF[(n, d)].append([a, b, r])

# Using the solutions for AF, let's analyze arbitrary words comprised of AF.
empty_keys = [k for k,v in AF.items() if len(v) == 0]
AF_final = {}
for k in empty_keys:
    del AF[k]    
for n, d in AF:
    k = 2*d*n
    R = generators[k]
    AF_final[(n, d)] = []
    for a, b, r in AF[(n, d)]:
        flag = True
        for f in range(n):
            for g in range(d):
                x = 6*n*r*g + 2*a*d*f - 2*b*d*f - d*n*g
                y = 6*n*r*g + 4*a*d*f - d*n*g + 2*b*d*f
                z = f*(4*b*d + 2*a*d)
                inv = [(x)%k, (-x)%k, (y)%k, (-y)%k, (z)%k, (-z)%k]
                for gen in R:
                    r_inv = [(gen*w)%k for w in inv]
                    if not compare(inv, r_inv):
                        flag = False
                        break
        if flag:
            AF_final[(n, d)].append([a, b, r])

empty_keys = [k for k,v in AF_final.items() if len(v) == 0]
for k in empty_keys:
    del AF_final[k]
D_diag = {}
for n, d in AF_final:
    k = 2*d*n
    R = generators[k]
    D_diag[(n, d)] = []
    for [a, b, r], s in product(AF_final[(n, d)], range(d)):
        # Exclude the case when both r and s are 0. 
        # This would be the case of C.
        if gcd_vec(r, 2*r, 2*r+s) != 1: 
            continue
        flag = True
        for etas in product(range(n), repeat = 4):
            for deltas in product(range(d), repeat = 4):
                eta_one = 2*d*n*etas[0] - 2*d*(etas[1]+etas[3])*(a+b) + 2*a*d*etas[2]
                eta_two = 2*a*d*etas[1] + 2*b*d*(etas[0]+etas[3]) - 2*d*etas[2]*(a+b)
                eta_three = 2*a*d*etas[3] + 2*b*d*(etas[1]+etas[2]) - 2*d*etas[0]*(a+b)
            
                delta_one = 4*n*r*deltas[0] + (8*r+4*s)*n*deltas[1] + (d-2*r)*n*deltas[2] + (d-2*r-s)*n*deltas[3]
                delta_two = (d-2*r)*n*deltas[0] + (d-2*r-s)*n*deltas[1] + 4*n*r*deltas[2] + (8*r+4*s)*n*deltas[3]
                delta_three = (d-2*r)*n*deltas[0] + (d-2*r-s)*n*deltas[1]+ (d-2*r)*n*deltas[2] + (d-2*r-s)*n*deltas[3]
                    
                x = (eta_one + delta_one) - (eta_two + delta_two)
                y = (eta_one + delta_one) - (eta_three + delta_three)
                z = eta_two + delta_two - (eta_three + delta_three)
                    
                inv = [(x)%k, (-x)%k, (y)%k, (-y)%k, (z)%k, (-z)%k]
                for gen in R:
                    r_inv = [(gen*w)%k for w in inv]
                    if not compare(inv, r_inv): 
                        flag = False
                        break        
        if flag:
            D_diag[(n, d)].append([a, b, r, s])   
empty_keys = [k for k,v in D_diag.items() if len(v) == 0]
for k in empty_keys:
    del D_diag[k]
with open('D_diag.pickle', 'wb') as f:
    pickle.dump(D_diag, f)