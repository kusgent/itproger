class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name = "Пупок", age = None, isHappy = None):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, " age: ", self.age, ".", " Happy: ", self.isHappy, "!", sep="")


cat1 = Cat("Сёмка", 2, True)
cat1.set_data(1)
cat1.get_data()

cat2 = Cat()
