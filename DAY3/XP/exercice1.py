class Cat:
    def __init__(self, name, age):
        self.name  = name
        self.age  = age
    
# create 3instance of class Cat
cat1 = Cat("Mimi",2)
cat2 = Cat("Loulou",5)
cat3 = Cat("Minou",3)
def oldest_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
            return cat1
    elif cat2.age >cat1.age and cat2.age > cat3.age:
            return cat2
    else:
            return cat3
        
        
old_cat = oldest_cat(cat1, cat2, cat3)
print("the oldest cat is",old_cat.name,"and is",old_cat.age,"years old")