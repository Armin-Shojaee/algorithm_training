# prime_number 

a =int(input())
b =int(input())
listt=[]
prime_temp=(1,2,3,4,5,6,7,8,9)

def is_prime():
    for i in range(a, b+1): 
        for j in range (1,10):
            if (i%prime_temp==0):
                listt.append(i)
                return

            else:
                pass

is_prime()
print(listt) 
