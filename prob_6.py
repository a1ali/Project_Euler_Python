

#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_of_squares(n):
    sum_1 = 0
    for i in range(0,n+1):
        sum_1 = sum_1 + i**2
    
    return sum_1


def square_of_sum(n):
    sum_2 = 0
    for i in range(0,n+1):
        sum_2 = sum_2 + i
        
    sum_2 = sum_2**2

    return sum_2

print(square_of_sum(100) - sum_of_squares(100))
