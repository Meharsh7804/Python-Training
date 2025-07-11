def print_info(val1, val2, name, city):
    print(val1 + val2)
    print(name)
    print(city)

#Unnamed arguments / Positional arguments
print_info(10, 20, "John", "New York") 

# Named arguments / Keyword arguments
print_info(val1=10, val2=20, name="John", city="New York") 

# Caution :- Cannot pass positional arguments after keyword arguments

def print_info_2(*args, **kwargs):
    for k,v in kwargs.items():
        print(k,v)

print_info_2(10, 20, name="John", city="New York")