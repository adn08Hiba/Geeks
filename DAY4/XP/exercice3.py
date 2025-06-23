from exercice2 import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        print(f"{self.name} is barking!")
        self.trained = True
    def play(self, *args):
        print("All dogs play together:")
        for dog in args:
            print(f"{self.name} is playing with {dog.name}")
    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
my_dog = PetDog("Fido", 2, 10)
buddy = PetDog("Buddy", 3, 12)
max = PetDog("Max", 4, 15)
my_dog.train()
my_dog.play(buddy, max)
my_dog.do_a_trick()
