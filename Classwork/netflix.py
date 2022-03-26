# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file ##had to go back a directory
myPath = os.path.join("..", "Resources", "netflix_ratings.cscv")

if os.path.exists(myPath):
    print("That file path doesn't exist")
    #tells you what directory youre in when youre trying to open the path so you can edit your path if youre in the wrong one
    print(f"you are at: {os.getcwd()}")

# Open the CSV ##as f with file as f *file type)
with open(myPath, "r", newline='') as f
    #on f bc thats what we opened the file as in the with statement
    # delim is commas bc thats what breaking up the data in the csv file
        #for delim dont put space comma itll look for that explicitly make sure its just a comma
    my_netflix_data = csv.reader(f, delimiter=",")

    # Loop through looking for the video
        #doesnt have to be called row its just a variable
        #looking in the nexflix data and checking if movie is in position 0 bc its 1st thing in rows
    for row in my_netflix_data:

        #check if movie is in position 0
        if video == row[0]:
            # if it is then print the screen and write to a file
            #wanted video name the rating and user rating, get row # from the csv file
            print(f'{video} is rated {row[1]} with a user rating of {row[-2]}.')

            with open(os.path.join("..", "Resources", "my_output_file.txt"), "w") as out_f:
                out_f.write(f'{video} is rated {row[1]} with a user rating of {row[-2]}.\n')

###will not run bc I do not have the files in the same place as the instructor