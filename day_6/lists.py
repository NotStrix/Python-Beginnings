# Jose Rosario
# Lists task
# Day 6
numbers = [10, 4 , 28, 8, 11, 12, 3, 7, 2, 9, 5]

# Print Numbers
for num in numbers:
    print(num)

# Add Number
numbers.append(int(input("Enter a number to add to the list: ")))

# Remove Number
numbers.remove(int(input("Enter a number to remove from the list: ")))

# Sort Numbers
numbers.sort()
for num in numbers:
    if num % 2 == 0:
        print("Even number:", num)