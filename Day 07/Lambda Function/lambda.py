# LAMBDA FUNCTION IS USED WHEN ONE LINER FUNCTION IS NEEDED

def get_sum(a,b):
    return a + b

sum = lambda a, b: a+b

print("Sum using get_sum Function: ",get_sum(5, 3))
print("Sum using Lambda Function 1: ",sum(5, 3))
print("Sum using Lambda Function 2: ", (lambda a, b: a+b)(5, 3))
