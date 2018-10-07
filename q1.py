# program to sum multiples of 3 or 5
n = int ( input ("n : "))
i = 1
sum = 0
while i < n :
    if int(i%3) is 0 or int(i%5) is 0 :
        sum = sum + i
        i += 1
print(sum)
