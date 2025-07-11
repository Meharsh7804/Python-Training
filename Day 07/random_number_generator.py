class MyRandom:
    def __init__(self, low, high, count):
        self.low = low
        self.high = high
        self.count = count
        self.current = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.count:
            import random
            self.current += 1
            return random() * (self.high - self.low) + self.low
        else:
            raise StopIteration
        
for r in MyRandom(1, 10, 5):
    print(r, end=" ")