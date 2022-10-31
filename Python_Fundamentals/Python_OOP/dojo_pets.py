class Pet:
    # implement __init__( name , type , tricks ):
    # Create a Pet class with the pet attributes listed above.
    def __init__(self, name , type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.sound = sound

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5 and decrease energy by 15
    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print( f'While bathing {self.name}, {self.name} started {self.sound}.')
        return self

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    # Create a Ninja class with the ninja attributes listed above.
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    # implement the following methods:
    # Implement walk(), feed(), bathe() on the ninja class.
    
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        print(f"Pets health: {self.pet.health} | Pets energy: {self.pet.energy}")
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f"Feeding {self.pet.name} {self.treats}")
        self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self

pet_1 = Pet("Mercedes","Dog","sitting","howling")

ninja_1 = Ninja("James","Randall", pet_1,"chicken strips","Purina")

# Have the Ninja feed, walk , and bathe their pet.
ninja_1.feed();
ninja_1.walk();
ninja_1.bathe();
