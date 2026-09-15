def count_down(n):
    if n == 0:
        return

    print(n)
    count_down(n - 1)


count_down(5)

print("\nTime Complexity: O(n)")
print("Space Complexity: O(n)")