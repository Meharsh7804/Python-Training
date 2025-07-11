nums = [[10,100],[20,300],[15,400],[25,250]]
print("Original list: ")
print(nums)

# Sort in ascending order based on the first element of each sublist
print("\nAscending order based on first element: ")
nums.sort()
print(nums)

# Sort in ascending order based on the second element of each sublist
print("\nAscending order based on second element: ")
nums.sort(key=lambda x: x[1])
print(nums)

# Sort in descending order based on the first element of each sublist
print("\nDescending order based on first element: ")
nums.sort(reverse=True)
print(nums)

# Sort in descending order based on the second element of each sublist
print("\nDescending order based on second element: ")
nums.sort(key=lambda x: x[1], reverse=True)
print(nums)