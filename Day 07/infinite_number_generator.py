def infinite_generator():
    i = 0;
    while True:
        i += 1
        yield(i)

fun = infinite_generator()
for _ in range(100):
    print(next(fun), end=" ")