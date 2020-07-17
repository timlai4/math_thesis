# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:08:04 2020

@author: Tim

Similar to diagonal_elements.py, we apply rationality condition
to find the possible subgroups in the scalar embedding case.
"""

import collections
import json
from functools import reduce

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

generators = {3: [2], 4: [3], 5: [2], 6: [5], 7: [3], 8: [3,5], 9: [2], 10: [3],
              11: [2], 12: [5,7], 13: [2], 14: [3], 15: [2, 14], 16: [3, 15],
              17: [3], 18: [5], 19: [2], 20: [3,19], 21: [2,20], 22: [7], 
              23: [5], 24: [5,7,13], 25: [2], 26: [7], 27: [2], 28: [3,13],
              29: [2], 30: [7,11], 31: [3], 32: [3,31], 33: [2,10], 34: [3], 
              35: [2,6], 36: [5,19]}
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
write = False # Whether to write outputs to scalar_C.txt
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
    if write:
        file = open("C_grps.txt","a")
        file.write(str(n) + '\n')
        json.dump(solutions,file)
        file.write('\n')
        file.close()
    C[n] = solutions

# Bootstrap classification of C to D. 
# First, remove the empty values from C. 
empty_keys = [k for k,v in C.items() if len(v) == 0]
for k in empty_keys:
    del C[k]

# Analyze AF


