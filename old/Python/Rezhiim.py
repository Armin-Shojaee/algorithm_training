G = 0
Y = 0
R = 0 

(c1 , c2 , c3 , c4 , c5) = (input())

if c1 == 'G' :
    G = G+1
elif c1 == 'Y' :
    Y = Y+1 
if c1 == 'R' :
    R = R+1

if c2 == 'G' : 
    G = G+1
elif c2 == 'Y' :
    Y = Y+1
if c2 == 'R' :
    R = R+1 

if c3 == 'G' : 
    G = G+1
elif c3 == 'Y' :
    Y = Y+1
if c3 == 'R' :
    R = R+1 

if c4 == 'G' :
    G = G+1
elif c4 == 'Y' :
    Y = Y+1
if c4 == 'R' :
    R = R+1 

if c5 == 'G' :
    G = G+1
elif c5 == 'Y' :
    Y = Y+1
if c5 == 'R' :
    R = R+1 

if (R >= 3) or (Y >= 2 and R >= 2) or (G == 0):
    print("nakhor lite")

else :
    print("rahat baash")