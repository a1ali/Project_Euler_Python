

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Python program to find the smallest number evenly  
# divisible by all number 1 to n 
import fractions 
  
# Returns the lcm of first n numbers 
def lcm(n): 
    ans = 1    
    for i in range(1, n + 1): 
        ans = (ans * i)/fractions.gcd(ans, i)         
    return ans 
  
# main 
n = 20
print (lcm(n)) 


