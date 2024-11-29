# #  Slicing in Python..
# Reverse the list nums = [5, 10, 15, 20, 25, 30].
# Expected Output: [30, 25, 20, 15, 10, 5]

# Extract every third element starting from the second element in nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Expected Output: [2, 5, 8]

# Extract the sublist [3, 4, 5, 6] from nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
# Expected Output: [3, 4, 5, 6]

# Extract the last three elements from nums = [100, 200, 300, 400, 500, 600, 700].
# Expected Output: [500, 600, 700]

# Replace [30, 40] in nums = [10, 20, 30, 40, 50] with [300, 400].
# Expected Output: [10, 20, 300, 400, 50]

# Extract all elements at odd indices from nums = [0, 1, 2, 3, 4, 5].
# Expected Output: [1, 3, 5]

# Extract every second element in reverse order from nums = [10, 20, 30, 40, 50, 60].
# Expected Output: [60, 40, 20]

# Extract the first four elements from nums = [5, 10, 15, 20, 25].
# Expected Output: [5, 10, 15, 20]

# Replace the middle two elements in nums = [1, 2, 3, 4, 5] with [99, 100].
# Expected Output: [1, 2, 99, 100, 5]

# Extract elements from index 2 to 6 with a step of 2 from nums = [1, 2, 3, 4, 5, 6, 7, 8].
# Expected Output: [3, 5, 7]

# Reverse the string s = "hello world" using slicing.
# Expected Output: "dlrow olleh"

# Extract only vowels from the string s = "programming is fun" using slicing.
# Expected Output: "oaiiu"

# Extract the last 5 characters of the string s = "Python slicing is powerful".
# Expected Output: "rful"

# Replace the first 3 elements in nums = [1, 2, 3, 4, 5] with [10, 20, 30].
# Expected Output: [10, 20, 30, 4, 5]

# Extract all even numbers from nums = [0, 1, 2, 3, 4, 5, 6] using slicing.
# Expected Output: [0, 2, 4, 6]

# Extract elements in reverse order starting from index 4 to 1 in nums = [10, 20, 30, 40, 50].
# Expected Output: [50, 40, 30]

# Extract every fourth character from the string s = "abcdefghijklmnopqrstuvwxyz".
# Expected Output: "aeimquy"

# Extract the middle element from a 2D list matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# Expected Output: 5

# Extract a slice [5, 6, 7] from the 2D list matrix = [[1, 2, 3], [4, 5, 6, 7], [8, 9]].
# Expected Output: [5, 6, 7]

# Extract the diagonal [1, 5, 9] from the 2D list matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# Expected Output: [1, 5, 9]

# nums = [5, 10, 15, 20, 25, 30]
# print(nums[::-1])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::3])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[3:6])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums)

s = '12345'
print(s)
# '1234512345123451234512345'
print(s[::5])
# '11111'
print(s[4::5])
# '55555'
print(s[::-5])
# '55555'
print(s[::-2])
# '5432154321543215432154321'
