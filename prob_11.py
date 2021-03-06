
'''
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

num = 'long_list'

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?


import numpy as np

long_list = np.array([
            [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
            [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
            [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
            [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
            [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
            [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
            [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
            [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
            [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
            [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
            [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
            [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
            [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
            [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
            [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
            [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
            [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
            [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
            [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
            [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
            ])

products = []
rows  = long_list.shape[0]

columns = long_list.shape[1]
#print(rows,columns)


i = 0 
def horizontal(x):
    mult = 1
    for i in range(0,rows):
        p = 0 
        while p < columns-3: # chek it out it works 

            for j in range(p, p + 4):
                mult = mult * x[i][j]
                print('[{}],[{}]'.format(i,j))

            products.append(mult)
            mult = 1
            p+=1


def vertical(x):
    mult = 1
    for i in range(0,columns):
        p = 0 
        while p < rows-3: # chek it out it works 

            for j in range(p, p + 4):
                mult = mult * x[j][i]
                print('[{}],[{}]'.format(i,j))

            products.append(mult)
            mult = 1
            p+=1

#horizontal(long_list)

def diagonal(x):
    mult = 1
    i = 0
    new_mat = np.ones((20,20))
    while i < 20:
        for j in range(0,i):
            for k in range(0,i):
                new_mat[j][k] = long_list[j][k]
                #print(new_mat)
            
        i +=1
                
        

    
#vertical(long_list)
#horizontal(long_list)
diagonal(long_list)
#print(max(products))


'''
#from numba import jit

grid =[[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8,],
[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0,],
[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65,],
[52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91,],
[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80,],
[24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50,],
[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70,],
[67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21,],
[24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72,],
[21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95,],
[78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92,],
[16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57,],
[86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58,],
[19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40,],
[4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66,],
[88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69,],
[4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36,],
[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16,],
[20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54,],
[1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]

#horizontal and vertical
largest=[0,0,0,0]
for h in range(0,20):
    for hsub in range(0,17):
        horizontal = grid[h][hsub] * grid[h][hsub+1] * grid[h][hsub+2] * grid[h][hsub+3]
        vertical   = grid[hsub][h] * grid[hsub+1][h] * grid[hsub+2][h] * grid[hsub+3][h]
        if horizontal > largest[0]:
            largest[0] = horizontal
        if vertical > largest[1]:
            largest[1] = vertical

#diagonal right and left
for r in range(0,17):
    for rsub in range (0,17):
        right_diagonal = grid[rsub][0+r] * grid[rsub+1][1+r] * grid[rsub+2][2+r] * grid[rsub+3][3+r]
        left_diagonal  = grid[rsub][3+r] * grid[rsub+1][2+r] * grid[rsub+2][1+r] * grid[rsub+3][r]
        if right_diagonal > largest[2]:
            largest[2] = right_diagonal
        if left_diagonal > largest[3]:
            largest[3] = left_diagonal

print(largest)
