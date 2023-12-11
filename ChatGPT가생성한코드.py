# List
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Dictionary:", my_dict)

# Accessing elements
print("Accessing elements:")
print("List[0]:", my_list[0])
print("Tuple[0]:", my_tuple[0])
# Sets do not support indexing, so we convert it to a list first
set_as_list = list(my_set)
print("Set[0]:", set_as_list[0])
print("Dictionary['a']:", my_dict['a'])

# Modifying elements
print("Modifying elements:")
my_list[0] = 10
# Tuples are immutable, so the following line would raise an error
# my_tuple[0] = 10
# Sets do not support indexing directly, so you would need to use methods like add() or remove()
my_set.add(10)
my_dict['a'] = 10

# Length of the data structures
print("Length:")
print("List length:", len(my_list))
print("Tuple length:", len(my_tuple))
print("Set length:", len(my_set))
print("Dictionary length:", len(my_dict))

# Check membership
print("Check membership:")
print("Is 10 in List?", 10 in my_list)
print("Is 10 in Tuple?", 10 in my_tuple)
print("Is 10 in Set?", 10 in my_set)
print("Is 'a' in Dictionary?", 'a' in my_dict)
