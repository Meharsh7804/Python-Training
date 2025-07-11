num = range(1,10000)
print(num)  # range object


def generate_nums(n):
    yield("abc")
    yield(100)
    yield(True)

gun = generate_nums(10)
print(next(gun))
print(next(gun))
print(next(gun))

for i in range(0, 11, 2):
    print(i, end=" ")

def myRange(start, end, step=0.2):
    while start < end:
        yield start
        start += step

for i in myRange(0, 10, 0.5):
    print(i, end=" ")