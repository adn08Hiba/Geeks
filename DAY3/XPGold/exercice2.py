import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reverse_list(self):
        """Retourne la liste inversée."""
        return self.letters[::-1]

    def sort_list(self):
        """Retourne la liste triée par ordre alphabétique."""
        return sorted(self.letters)

    def generate_random_list(self):
        """Génère une liste de nombres aléatoires de même longueur que `letters`."""
        return [random.randint(0, 100) for _ in range(len(self.letters))]
# Création de l'objet avec une liste de lettres
my_list = MyList(['d', 'b', 'a', 'c', 'e'])

print("Original list: ", my_list.letters)
print("Reversed list:", my_list.reverse_list())
print("Sorted list:  ", my_list.sort_list())
print("Random list:  ", my_list.generate_random_list())
[random.randint(0, 100) for _ in range(len(self.letters))]
