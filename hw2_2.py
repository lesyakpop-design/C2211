import random


class Student:
    def __init__(self, name, year, money):
        self.name = name
        self.year = year
        self.money = money
        self.skills = random.uniform(1, 5)
        self.happiness = 5

    def working(self):
        print("Working... 🛠️")
        self.money += 200
        self.happiness -= 1
        self.skills += 0.05

    def study(self):
        print("Studying... 📚")
        self.skills += 0.3
        self.happiness -= 0.5

    def chill(self):
        print("Chilling... 😎")
        self.happiness += 1
        self.skills -= 0.1
        self.money -= 50

    def eat(self):
        self.money -= 20
        self.happiness += 0.2

    def is_alive(self):
        if self.skills <= 0:
            print("Student failed studies...💀")
            return False
        if self.money <= -100:
            print("Student went bankrupt...💸")
            return False
        if self.happiness <= 0:
            print("Student is depressed...😭")
            return False
        return True

    def day_action(self):
        if self.money < 100:
            self.working()
        elif self.skills < 2:
            self.study()
        elif self.happiness < 3:
            self.chill()
        else:
            action = random.choice([self.working, self.study, self.chill])
            action()

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.year}")
        print(f"Skills: {self.skills:.2f}")
        print(f"Money: {self.money:.2f}$")
        print(f"Happiness: {self.happiness:.2f}")

    def grow_up(self):
        self.year += 1


john = Student("John", 17, 500)
john.introduce()

for day in range(1, 366):
    print(f"===== Day {day} =====")

    john.day_action()
    john.eat()

    if not john.is_alive():
        break

else:
    print("Student survived the year 🎉")

john.grow_up()
john.introduce()