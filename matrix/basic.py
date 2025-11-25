matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rows = 4
col = 3
#matrix[0][1] = 10
#print(matrix[0][1])

for row in matrix:
    print (row)

rows = 2
cols = 2
matrixx =[]

# user input
for row in range(rows):
    row = []
    for col in range(cols):
        value = int(input("enter the values:"))
        row.append(value)
    matrixx.append(row)

# output
for val in matrixx:
    for val2 in val:
        print(val2, end= '')
    
    print() 

# Search an element in matrix
target = 4
for i in range (len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == target:
             print([i,j], matrix[i][j])


# Diagnoal element sum
Sum = 0
n = len(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i ==j:
            Sum +=matrix[i][j]
        elif j == n-i-1:
            Sum+= matrix[i][j]

print(Sum)
