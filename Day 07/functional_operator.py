# map function :-

nums = [1,2,3,4,5,6,7,8,9,10]
squares = map(lambda x: x * 2, nums)
print(squares) 

# filter function :-

nums = [1,2,3,4,5,6,7,8,9,10]
even_nums = filter(lambda x: x % 2 == 0, nums)
print(even_nums)

# for odd numbers return 0 and for even numbers return it's square
nums = [1,2,3,4,5,6,7,8,9,10]
result = map(lambda x: 0 if x % 2 != 0 else x ** 2, nums)
print(result) 

# reduce function :-
from functools import reduce

nums = [2,5,7,2,6]

s = reduce(lambda x,y: x+y, nums)
p = reduce(lambda x,y: x*y, nums)
print(s,p)

# Given a list, Find max and min vale from the list using reduce 
nums = [2,5,7,9,11]
max=reduce(lambda x,y: x if x > y else y, nums)
min=reduce(lambda x,y: x if x < y else y, nums)
print(max, min)

# Is Sorted or not?
nums = [2,5,1,4,3]
isSorted = reduce(lambda x,y: (x<y,y) if type(x) is not tuple else (x[0] and x[1]<y,y), nums)[0]
print(isSorted)