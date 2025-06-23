class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False
class Family:
    def __init__(self, last_name, members=[]):
        self.last_name = last_name
        self.members = members
    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                return member.is_18()
                if member.is_18():
                    return "You are over 18, your parents Jane and John accept that you will go out with your friends"
                else :
                    return "Sorry, you are not allowed to go out with your friends."
        return "Member not found in the family."
    def family_presentation(self):
        print(f"Family {self.last_name} members:")
        for member in self.members:
            print(f"{member.first_name}  have {member.age} years old.")
my_family = Family("Smith")
my_family.born("Alice", 17)
my_family.born("Bob", 20)

print(my_family.check_majority("Bob"))
print(my_family.check_majority("Alice"))

my_family.family_presentation()
