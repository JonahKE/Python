# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
arr = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(arr):
    for i in arr:
        for j in range(0,i):
            print "*",
        print " "
draw_stars(arr)
# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
arr2 = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_all_stars(arr):
    for i in arr:
        if type(i) == str:
            for j in range(0,len(i)):
                print i[0].lower(),
            print " "
        elif type(i) == int:
            for j in range(0,i):
                print "*",
            print " "
draw_all_stars(arr2)