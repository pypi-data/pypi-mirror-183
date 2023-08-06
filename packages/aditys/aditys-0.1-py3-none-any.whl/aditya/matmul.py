m=int(input("enter the number of rows:"))
n=int(input("enter the number of columns:"))
p=int(input("enter the number of elements rowwise or columnwise:"))

print("enter the elements for matrix1:")
mat1=[[int(input()) for i in range(m)] for j in range(n)]
print(mat1)

print("enter the elements for matrix2:")
mat2=[[int(input()) for i in range(m)] for j in range(n)]
print(mat2)

print("Multiplication of the two given matrice:")
result=[[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        for k in range(p):
            result[i][j]=mat1[i][j]+mat2[i][j]
        print(result) 