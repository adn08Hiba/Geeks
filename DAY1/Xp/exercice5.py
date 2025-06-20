my_fav_number = {42} 
my_fav_number.add(7)
my_fav_number.add(23)
my_fav_number.remove(23)
friend_fav_numbers = {2,5,8,9,10}
our_fav_numbers = my_fav_number.union(friend_fav_numbers)
print("Mu favorite numbers are:", my_fav_number)
print("Mu friends favorite numbers are:", friend_fav_numbers)
print("Our favorite numbers are:", our_fav_numbers)