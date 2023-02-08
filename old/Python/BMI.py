n = int(input())
m = float(input())
BMI  = n / (m * m)
# information 
print ("%.2f" %BMI)
# 2 ragham aashar 
if (BMI<18.5) : 
    print("underweight") 

elif (BMI >= 18.5 and BMI < 25): 
    print("Normal")

elif (BMI >= 25 and BMI < 30 ) :
    print("overweight") 

else :
    print("obese") 


