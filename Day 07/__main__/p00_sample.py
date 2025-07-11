def get_sum(a,b):
  return a+b

def get_product(a,b):
  return a*b

def print_name():
  print("__name__ in p00_sample is:", __name__)

print(get_product(10,2))

if __name__ == "__main__":
  print(get_sum(10,2))