def create_list(n):
    numbers = []

    for i in range(n):
        numbers.append(i)

    return numbers


n = int(input("Enter the size: "))

numbers = create_list(n)

print("List:", numbers)
print("Space Complexity: O(n)")