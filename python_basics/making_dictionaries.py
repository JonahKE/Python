# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings.
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    return dict(zip(arr1, arr2))

print make_dict(name, favorite_animal)
# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.
name2 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "dogs"]

def make_dict_unequal(arr1, arr2):
    if len(arr2) > len(arr1):
        return dict(zip(arr2, arr1))
    else:
        return dict(zip(arr1, arr2))

print make_dict_unequal(name2, favorite_animal2)