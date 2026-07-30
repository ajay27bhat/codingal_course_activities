# Matrix Multiplication using Nested Loops

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of Matrix A:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

print("Enter elements of Matrix B:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    B.append(row)

# Result matrix
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    C.append(row)

# Matrix multiplication
for i in range(rows):
    for j in range(cols):
        for k in range(cols):
            C[i][j] += A[i][k] * B[k][j]

print("Product Matrix:")
for i in range(rows):
    for j in range(cols):
        print(C[i][j], end=" ")
    print()