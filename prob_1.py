# if we list all the natural number below 10 that are multiples of 3 or 5 we get 3,5,6, and9. The sum of these 
# multiples is 23. Find teh sum of all the multiples of 3 or 5 below 1000. 

num = 0
i = 0
while i <= 10:
    if i%3 == 0 or i%5 == 0:
        num = i + num

    i = i+1
print(num)