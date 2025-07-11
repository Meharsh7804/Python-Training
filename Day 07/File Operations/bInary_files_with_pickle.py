import pickle
# class DummyClass:
#     def __init__(self, val1, val2):
#         self.val1 = val1
#         self.val2 = val2
#     def get_val1(self):
#         return self.val1

# dc = DummyClass(10, 20)
# name = "Meharsh"
# age = 21

# with open("data.pkl", "wb") as f:
#     pickle.dump((dc,name, age), f)

# with open("data.pkl", "rb") as f:
#     dc1,name1,age1 = pickle.load(f)

# print(dc1,name1,age1)
# print(dc1.val1, dc1.val2)

class ManageFiles:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        
with ManageFiles("./hello.txt", "w") as f:
    f.write("Hello, World!")