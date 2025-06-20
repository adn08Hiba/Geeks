class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo.")
    def get_animals(self):
      if self.animals:
        print(f"the animals in {self.zoo_name}")
        for animal in self.animals:
           print(animal)
    def sell_animal( self, animal_sold):
      if animal_sold in self.animals:
        self.animals.remove(animal_sold)
        print(f"{animal_sold} has been sold.")
    def sort_animals(self):
       self.animals.sort()  # Trie la liste principale d'animaux
       grouped = {}
       for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = [animal]
            else:
                grouped[first_letter].append(animal)
       return grouped
    def get_groups(self):
       grouped_animals = self.sort_animals()
       for letter, group in grouped_animals.items():
            print(f"{letter}: {group}")
my_zoo = Zoo("My zoo")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Zebra")
my_zoo.add_animal("Giraffe")
my_zoo.add_animal("Bear")
my_zoo.add_animal("Baboon")
my_zoo.add_animal("Cougar")
my_zoo.add_animal("Cat")
my_zoo.get_animals()
my_zoo.sell_animal("Zebra")
my_zoo.sort_animals()
my_zoo.get_groups()
       
       
       

      
        
        

    
