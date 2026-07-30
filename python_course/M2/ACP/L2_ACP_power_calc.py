# Power Calculator using For Loop

n = int(input("Enter the base number: "))
p = int(input("Enter the power: "))

result = 1

for i in range(p):
    result = result * n

print(n, "raised to the power", p, "=", result)