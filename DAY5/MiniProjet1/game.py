# game.py

import random

class Game:
    def get_user_item(self):
        choices_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        while True:
            choice = input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
            if choice in choices_map:
                return choices_map[choice]
            else:
                print("Invalid input. Please enter r, p, or s.")

    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "paper" and computer_item == "rock") or \
             (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You chose: {user_item[0]}. The computer chose: {computer_item[0]}. Result: {result}")
        return result
