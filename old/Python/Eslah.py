a,b = map(int, input().split())

if(a==b):
    print("Same")
else:
    c = a
    a = b
    b = c
    print(a,b)

print("The End!")