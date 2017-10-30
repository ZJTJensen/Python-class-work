# y=0
# while y <= 100:
#     print y 
#     y = y+1

# y = 5

# while y < 1000000:
#     if y%5==0:
#         print y
#     y=y+1

# for num in range(1, 101):   #print values 1 to 100
#     print num 
# for num in range(5, 1000000): #print multiples of 5 to 1000000
#     if num%5==0:
#         print num

# for num in range(5, 1000000, 5): #print multiples of 5 to 1000000
#     print num

sum=0
a = [1, 2, 5, 10, 255, 3] #adds all the numbers together
for val in a:
    sum = sum + val

print sum


sum = sum/ len(a)  #creates the average of values
print sum