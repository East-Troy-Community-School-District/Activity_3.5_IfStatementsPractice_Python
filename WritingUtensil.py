'''
Writing Utensil
Pawelski
10/15/2023
Introduction to Computer Science
'''

utensil = input("Enter an office supply item >> ")
if utensil == "marker":
    color == input("What color is the marker? >> ")
    if color == "red":
        print("You can write with that, but it will be hard to see!")
    else:
        print("You can write with that and see it easily.")
elif utensil == "pencil" or utensil == "pen" or utensil == "mechanical pencil": # Add your code here!
    print("You can write with that!")
# Add your code here!
else:
    print("You can't write with that!")