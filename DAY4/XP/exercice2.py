class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight  # ajout manquant

    def bark(self):
        print(f"{self.name} is barking!")

    def run_speed(self):
        return self.weight / self.age * 10  # correction : return au lieu de print

    def fight(self, autre_dog):
        if self.run_speed() * self.weight > autre_dog.run_speed() * autre_dog.weight:
            print(f"{self.name} has won against {autre_dog.name}!")
        else:
            print(f"{autre_dog.name} has won against {self.name}!")

# Création des objets
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)

# Appels
dog1.bark()
print(dog1.run_speed())   # affiche la vitesse
dog2.bark()
print(dog2.run_speed())
dog1.fight(dog2)
