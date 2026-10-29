class Cat:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, amount):
        self.weight += amount

    def getDetails(self):
        return f"Name: {self.name}\nWeight: {self.weight}\n"

    def walk(self):
        if self.weight <= 1:
            print(f"Couldn't walk {self.name} because that cat would starve if walked")
        else:
            self.weight -= 1