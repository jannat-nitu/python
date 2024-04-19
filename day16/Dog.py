class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Bark")
        for n in range(0, 10):
            print(n)

ozzy = Dog("Ozzy", 20)
print(ozzy.bark())
