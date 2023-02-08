# barabar kardan 3 adad

a , b , c =map(int,input().split())

if (a > b > c) :
    b = ((a - b)+ b)
    c = ((a - c)+ c)
    
if (a > b) and (b < c) :
    b = ((c - b)+ b)
    a = ((b - a)+ a)
    
if (a < b) and (b < c) :
    a = ((c - a)+ a)
    b = ((c - b)+ b)
    
if (a < b) and (b > c) :
    a = ((b - a)+ a)
    c = ((b - c)+ c)
    
    
print(a , b , c)