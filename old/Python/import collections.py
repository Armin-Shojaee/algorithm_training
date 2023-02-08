import collections 
 
 
a = [1 ,1 ,2 ,2 ,2 ,8 ] 
b = [0 ,2 ,2 ,2] 
 
if collections.Counter(a) == collections.Counter(b):
    print ("The lists a and b are the same") 
else: 
    print ("The lists a and b are not the same") 
 