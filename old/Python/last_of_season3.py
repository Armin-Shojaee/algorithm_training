# |a,b,c,d|< 1000
a=int(input())
b=int(input())
c=int(input())
d=int(input())

# Hesab kardan;
total=(a + b + c + d)
average=(( a + b + c + d ) / 4)
product=(a * b * c * d)
maximum=max(a, b, c, d)
minimum=min(a, b, c, d)

# All of print
print('Sum :', "%.2f" %total)
print('Average :', "%.2f" %average)
print('Product :' , "%.2f" %product)
print('Max :' , "%.2f" %maximum)
print('Min :' , "%.2f" %minimum)