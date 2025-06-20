class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name}does woof!")
    def jump(self):
        print(f"{self.name}jumpscm high!{self.height*2}")
davids_dog = Dog("Rex",50)
sarahs_dog = Dog("Teacup",20)
print(davids_dog.name,"is",davids_dog.height,"cm")
davids_dog.bark()
davids_dog.jump()
print(sarahs_dog.name,"is",sarahs_dog.height,"cm")
sarahs_dog.bark()
sarahs_dog.jump()
