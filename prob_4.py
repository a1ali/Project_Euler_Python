

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

from math import ceil , floor

def palincheck(x):
    palindrom = False
    list_p = [int(x) for x in str(x)] 
    new_p = list_p.copy()
    new_p = new_p[::-1]

    if new_p == list_p:
        palindrom = True
    
    return palindrom

#print(palincheck(115729411))


palins = []
for i in range(100, 1000):
    for j in range(100,1000):
        k = i*j
        if(palincheck(k)):
            palins.append(k)
            
print("answer is {}".format(max(palins)))
                



      
   

