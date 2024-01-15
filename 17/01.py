class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, " age: ", self.age, ".", " Happy: ", self.isHappy, "!", sep="")


cat1 = Cat()
cat1.name = "Barsik"
cat1.age = 3
cat1.isHappy = True

cat2 = Cat()
cat2.name = "Pushok"
cat2.age = 2
cat2.isHappy = False

cat3 = Cat()
cat3.set_data("Murka", 5, True)

print(cat1.name)
print(cat2.age)
cat3.get_data()
