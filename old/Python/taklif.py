k = 1
count = 0
while count < 10:
    if k % 4 == 0:
        break
    count = count + k
    k = k + 1
print(count)
