# A python script for making inventory of the films that I own.

import os
import sys

# Setup three dicts to append to - based on type of copy

dvds = {}

blu_rays = {}

digital = {}

new_user = True

# Welcome user and show what they already have in their list of movies
print("Welcome! This is a script for keeping track of your movie collection.")
user = input("What is your name? ")

if os.path.exists("./MyMovies/collection.txt"):
    new_user = False
    view_choice = input(
        f'Hi, {user}. Do you want to see what you have cataloged so far? (Yes/No) '
    )
    if view_choice.lower() == "yes" or view_choice.lower == "y":
        # show movies that have already been written to file - by reading and outputting file
        view = open("/MyMovies/collections.txt", "r")
        content = view.read()
        print(content)
        done = input("Press Enter - when you are done viewing.")
        while done != "":
            done = input("Press Enter to move on.")
        os.system("clear")
        view.close()
else:
    os.mkdir("MyMovies")
    print(f'Hi, {user}. This program will create file for you called "collections".')
    print(
        "You can use this file to append to - everytime you want to add to catalog titles."
    )
    print('The "collections" file will be in a folder called "MyMovies".')
    with open('./MyMovies/collection.txt', 'w') as new_file:
        title_content = f'****************** {user}\'s Movie Collection *********************\n'
        new_file.write(title_content)


ready = input("Are you ready to enter some titles? (Yes/No)")
if ready.lower() == "yes" or ready.lower() == "y":
    add_to_collection = True
elif ready.lower() == "no" or ready.lower == "n":
    print("See you next time!")
    sys.exit()
else:
    print("I didn't get that. Relaunch the program.")
    sys.exit()

types = ['1', '2', '3']
while add_to_collection:
    # Ask user whether they want to enter a DVD, Blu-Ray or a digital version
    print("Do you want to enter a DVD(1), Blu-Ray(2) or Digital-Content(3)?")
    type = input("Please type the number: ")
    if type not in types:
        print('That is not a valid choice. Try again.')
        continue
    # Prompt user to input a title and save in a variable
    print('Type the name of the film you want to catalog below:')
    name = input()

# Prompt user to input the director of that film
    print('Now type the name of the director of this film:')
    director = input()

# Append the film title and director to the appropriate dict
    if type == '1':
        dvds[name] = director
    elif type == '2':
        blu_rays[name] = director
    else:
        digital[name] = director

    another = input('Type "Y" to continue adding titles or type "N" to finish up for now: ')
    if another.lower() == 'n':
        add_to_collection = False

# Append to a file - wwith fstrings - the information collected in the dicts
with open('MyMovies/collection.txt', 'a') as file:
# Format the output and save it to the file.
