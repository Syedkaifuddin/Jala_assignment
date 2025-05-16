# 1. Write a function to add integer values of an array
def add_array_elements():
    arr = [1, 2, 3, 4, 5]
    total = 0
    for i in arr:
        total += i
    print("\n1. Sum of array elements:", total)

add_array_elements()

# 2. Write a function to calculate the average value of an array of integers
def average_array():
    arr = [10, 20, 30, 40, 50]
    total = 0
    count = 0
    for i in arr:
        total += i
        count += 1
    avg = total / count if count != 0 else 0
    print("\n2. Average value of array:", avg)

average_array()

# 3. Write a program to find the index of an array element
def find_index():
    arr = [3, 8, 4, 6, 7]
    target = 4
    index = -1
    i = 0
    for val in arr:
        if val == target:
            index = i
            break
        i += 1
    print("\n3. Index of", target, "is:", index if index != -1 else "Not Found")

find_index()

# 4. Write a function to test if array contains a specific value
def contains_value():
    arr = [5, 9, 1, 4, 2]
    value = 9
    found = False
    for i in arr:
        if i == value:
            found = True
            break
    print("\n4. Array contains", value, ":", found)

contains_value()

# 5. Write a function to remove a specific element from an array
def remove_element():
    arr = [1, 3, 5, 7, 3, 9]
    value = 3
    result = []
    for i in arr:
        if i != value:
            result.append(i)
    print("\n5. Array after removing", value, ":", result)

remove_element()

# 6. Write a function to copy an array to another array
def copy_array():
    arr = [2, 4, 6, 8]
    new_array = []
    for i in arr:
        new_array.append(i)
    print("\n6. Copied array:", new_array)

copy_array()

# 7. Write a function to insert an element at a specific position in the array
def insert_at_position():
    arr = [10, 20, 30, 50]
    value = 40
    pos = 3  
    result = []
    i = 0
    inserted = False
    for item in arr:
        if i == pos:
            result.append(value)
            inserted = True
        result.append(item)
        i += 1
    if not inserted:
        result.append(value)
    print("\n7. Array after inserting", value, "at position", pos, ":", result)

insert_at_position()

# 8. Write a function to find the minimum and maximum value of an array
def find_min_max():
    arr = [13, 7, 22, 5, 19]
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    print("\n8. Minimum value:", min_val)
    print("   Maximum value:", max_val)

find_min_max()

# 9. Write a function to reverse an array of integer values
def reverse_array():
    arr = [1, 2, 3, 4, 5]
    reversed_arr = []
    count = 0
    for _ in arr:
        count += 1
    i = count - 1
    while i >= 0:
        reversed_arr.append(arr[i])
        i -= 1
    print("\n9. Reversed array:", reversed_arr)

reverse_array()


# 10. Write a function to find the duplicate values of an array
def find_duplicates():
    arr = [1, 3, 5, 3, 7, 1, 9, 5]
    duplicates = []
    count = 0
    for i in arr:
        inner_count = 0
        for j in arr:
            if i == j:
                inner_count += 1
        if inner_count > 1:
            already_added = False
            for d in duplicates:
                if d == i:
                    already_added = True
                    break
            if not already_added:
                duplicates.append(i)
    print("\n10. Duplicate values:", duplicates)

find_duplicates()

# 11. Write a program to find the common values between two arrays
def find_common_values():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    common = []
    for i in arr1:
        for j in arr2:
            if i == j:
                already_added = False
                for c in common:
                    if c == i:
                        already_added = True
                        break
                if not already_added:
                    common.append(i)
    print("\n11. Common values:", common)

find_common_values()

# 12. Write a method to remove duplicate elements from an array
def remove_duplicates():
    arr = [2, 3, 2, 5, 3, 7]
    unique = []
    for i in arr:
        found = False
        for u in unique:
            if i == u:
                found = True
                break
        if not found:
            unique.append(i)
    print("\n12. Array after removing duplicates:", unique)

remove_duplicates()

# 13. Write a method to find the second largest number in an array
def second_largest():
    arr = [10, 20, 4, 45, 99]
    largest = arr[0]
    second = arr[0]
    for i in arr:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i
    print("\n13. Second largest number:", second)

second_largest()

# 14. Write a method to find the second smallest number in an array
def second_smallest():
    arr = [10, 20, 4, 45, 5]
    smallest = arr[0]
    second = arr[0]
    for i in arr:
        if i < smallest:
            second = smallest
            smallest = i
        elif i < second and i != smallest:
            second = i
    print("\n14. Second smallest number:", second)

second_smallest()

# 15. Write a method to find number of even number and odd numbers in an array
def count_even_odd():
    arr = [1, 2, 3, 4, 5, 6]
    even = 0
    odd = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print("\n15. Even numbers:", even)
    print("    Odd numbers:", odd)

count_even_odd()

# 16. Write a function to get the difference of largest and smallest value
def diff_largest_smallest():
    arr = [5, 1, 9, 3, 7]
    min_val = arr[0]
    max_val = arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    diff = max_val - min_val
    print("\n16. Difference between largest and smallest:", diff)

diff_largest_smallest()

# 17. Write a method to verify if the array contains two specified elements (12, 23)
def contains_two_elements():
    arr = [5, 12, 7, 9, 23, 4]
    has_12 = False
    has_23 = False
    for i in arr:
        if i == 12:
            has_12 = True
        if i == 23:
            has_23 = True
    result = has_12 and has_23
    print("\n17. Array contains both 12 and 23:", result)

contains_two_elements()

# 18. Write a program to remove the duplicate elements and return the new array
def remove_duplicates_return_new():
    arr = [1, 2, 2, 3, 4, 4, 5]
    result = []
    for i in arr:
        found = False
        for j in result:
            if i == j:
                found = True
                break
        if not found:
            result.append(i)
    print("\n18. New array after removing duplicates:", result)

remove_duplicates_return_new()

