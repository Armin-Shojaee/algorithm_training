x = str(input())
a = x [::-1]
y = str(input())
b = y [::-1]

if a < b :
    print (int(x) , '<' ,int(y))
if b < a :
    print (int(y) , '<' ,int(x))
if b == a or a == b :
    print (int(x) , '=' ,int(y))