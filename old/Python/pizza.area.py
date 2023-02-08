# a program for calculate area of a pizza

r = input ("please give me r ? ")
pi = float (3.14)

radius =r = input (int)
pizza_area= ((radius**2) *pi)

if pizza_area < 100 :
    print ("small pizza")

if pizza_area >= 100 and pizza_area < 200 :
    print ("normal pizza")

if pizza_area >= 200 and pizza_area < 300 :
    print ("good pizza")

if pizza_area >= 300 and pizza_area < 400 :
    print ("big pizza")

print ("good boy")
