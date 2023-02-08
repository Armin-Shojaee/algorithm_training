# ... saat ... 

hours,minutes= map(int,input().split())

if (hours<10) :
    print("0{}:{}".format(hours,minutes)) 

elif (minutes<10) :
    print("{}:0{}".format(hours,minutes))

else :
    print("{}:{}".format(hours,minutes))

        