# Only keys are unpacked, values are not
info = {5:25, "salary":50000, "name":"John", "city":"New York"}

# Unpacking
age, salary, name, city = info
print(age)    # 5
print(salary) # 25
print(name)   # salary
print(city)  # name

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

# method 1
nums = nums1 + nums2 
print(nums)

# method 2 [merging two lists]
nums = [*nums1, *nums2]  # Unpacking lists
print(nums)  

# method 3
nums = nums1.copy()  # Copying first list
nums.extend(nums2)  # Extending with second list
print(nums)


d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d = {**d1, **d2}  # Unpacking dictionaries
print(d)  
