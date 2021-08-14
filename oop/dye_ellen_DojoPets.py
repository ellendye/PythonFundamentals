class Ninja:
    def __init__ (self, first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(name='', type=pet, tricks ='')
    def walk(self):
        # walks the ninja's pet invoking the pet play() method
        self.pet.play()
        return self
    def feed(self):
        # feeds the ninja's pet invoking the pet eat() moethod
        self.pet.eat()
        return self
    def bathe(self):
        # cleans the ninj'as pet invoking the pet noise() method
        self.pet.noise()
        return self
    def pet_info(self,name,tricks):

        return self


class Pet: 
    def __init__(self, name, type, tricks):
        self.name=name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
    def sleep(self):
        #Increases the pets energy by 25
        self.energy += 25
        print(f"energy is {self.energy}")
        return self
    def eat(self):
        # increases the pet's health by 5
        self.health += 5
        print(f"health is {self.health}")
        return self
    def play(self):
        # increases the pet's energy by 5 and health by 10
        self.energy += 5
        self.health += 10
        print(f"energy is {self.energy} health is {self.health}")
        return self
    def noise(self):
        # prints out the pet's sound
        if self.type == "dog":
            print("bark")
        elif self.type == "cat":
            print("meow")
        elif self.type == "pig":
            print("oink")
        elif self.type == "cow":
            print("moo")
        else:
            print("cough")
        return self


brad = Ninja('brad','thompson','dentastick','blue buffalo','dog')
brad.pet = Pet("emma","dog",["sit","stay","heel"])
brad.walk().feed().bathe()
brad.pet.sleep()