from functools import reduce
import collections
import json

def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)

def gcd_vec(*args):
  return reduce(gcd, args)

def remove_duplicates(list):
  cleaned_list = []
  for triple in list: # My list will be a list of triples
    if triple not in cleaned_list:
      cleaned_list.append(triple)
  return cleaned_list

def compare(list1,list2):
  return collections.Counter(list1) == collections.Counter(list2)

def sort(list): #insertion sort
  for j in range(1,len(list)):
    key = list[j]
    i = j-1
    while i > -1 and list[i] > key:
      list[i+1] = list[i]
      i -= 1
    list[i+1] = key
  return list

k = 3 # Initialize k
R = [2] # Manually store generators of (Z/k)*
solutions = []
for a in range(k):
  for b in range(k):
    for c in range(k):  
      if gcd_vec(a,b,c,k) > 1:
        #print([a,b,c])
        continue
      inv = [(a+c)%k,(b+c)%k,(-a-c)%k,(-b-c)%k,(a-b)%k,(b-a)%k]
      count = 0
      for r in R:
        r_inv = [(r*x)%k for x in inv]
        if compare(inv,r_inv):
          count += 1
      if count==len(R):
        solutions.append(sort([a,b,c]))        
# (1,2,2) = (2,1,1) but (1,2,2) != (1,2)      
solutions2= remove_duplicates(solutions) 
file = open("cyclic_results.txt","a")
file.write(str(k) + '\n')
json.dump(solutions2,file)
file.write('\n')
file.close()
print(solutions2)
              
            
