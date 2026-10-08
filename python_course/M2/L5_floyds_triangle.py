"""
OUTPUT:

Please Enter the total Number of Rows  : 4
1  
2  3  
4  5  6  
7  8  9  10 
"""

#Take input from user
rows = int(input("Please Enter the total Number of Rows  : "))
number = 1 #initialise by 1

print("Floyd's Triangle") 
#outer loop for number of rows
for i in range(1, rows + 1):
  #inner loop for number of columns
    for j in range(1, i + 1):   
      #display result     
        print(number, end = '  ')
        number = number + 1
    print()