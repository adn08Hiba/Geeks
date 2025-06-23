class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Siamese(Cat):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

class Bengal(Cat):
    pass

class Chartreux(Cat):
    pass

# Création des objets
bengal_obj = Bengal("Leo", 2)
chartreux_obj = Chartreux("Grisou", 4)
siamese_obj = Siamese("Luna", 3, "white")

# Liste de tous les chats
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Affichage des informations
print(f"{bengal_obj.name} is {bengal_obj.age} years old.")
print(f"{chartreux_obj.name} is {chartreux_obj.age} years old.")
print(f"{siamese_obj.name} is {siamese_obj.age} years old and is {siamese_obj.color}")

# Création de l'objet Pets et appel de walk()
sara_pets = Pets(all_cats)
sara_pets.walk()
