#

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

# the slowest way it takes forever but it works

totaled  = False
n = 1
total = 0
A = 0
B = 0
C = 0 
while totaled == False:

    for a in range (1, 1000):
        for b in range (a + 1, 1000):
                for c in range(b + 1, 1000):
                    if c**2 == a**2 + b**2:
                        if a + b + c == 1000:
                            totaled = True
                            A = a
                            B = b
                            C = c



print('A:{} B:{} C:{} , ABC:{}'.format(A,B,C,A*B*C))


    
