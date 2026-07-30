# Character Occurrence using Nested Loops

text = input("Enter a string: ")

for i in range(len(text)):
    count = 0

    # Check if character has already been counted
    already_counted = False
    for k in range(i):
        if text[i] == text[k]:
            already_counted = True
            break

    if not already_counted:
        for j in range(len(text)):
            if text[i] == text[j]:
                count += 1

        print(text[i], "occurs", count, "times")