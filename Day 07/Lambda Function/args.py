def get_sum(*nums):
    sum = 0
    for num in nums:
            sum += num
    return sum

print("Sum of numbers:", get_sum(1, 2, 3, 4, 5)) 
print("Sum of numbers:", get_sum(10, 20, 30))      
print("Sum of numbers:", get_sum(100, 200, 300, 400, 500, 600))  