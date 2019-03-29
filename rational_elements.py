# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 23:27:33 2019

@author: Tim
"""

import collections

def compare(list1,list2):
  return collections.Counter(list1) == collections.Counter(list2)

def check_rationality(a,b,k,R = [1]): # R is a list storing generators
  for s in range(1,k):
    for t in range(s):
      inv = [(s*a+t*b)%k,(-s*a-t*b)%k,(t*a+s*b)%k,(-t*a-s*b)%k,
             (-s*a+(s+t)*b)%k,(s*a-(s+t)*b)%k,(-t*a+(s+t)*b)%k,
             (t*a-(s+t)*b)%k,((s+t)*a-s*b)%k,(-(s+t)*a+s*b)%k,((s+t)*a-t*b)%k,
             (-(s+t)*a+t*b)%k]
      for r in R:
        r_inv = [(r*x)%k for x in inv]
        if compare(inv,r_inv):
            continue
        else:
            return "Bad"
  return "Good"

# Sample inputs:
check_rationality(0,1,3,[-1])
# Returns: 'Good', as expected
check_rationality(4,11,12,[5,7])
# Returns: 'Good'
check_rationality(4,9,12,[5,7])
# Returns: 'Bad', as expected, since it was not on the tensor square list. 
