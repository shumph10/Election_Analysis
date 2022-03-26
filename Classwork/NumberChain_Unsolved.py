# Initial variable to track game play
from shutil import unregister_unpack_format


user_play = "y"

start_value = 0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    #if just want to count from 0 at all times just declare the inputted string with int(input) and get rid of try and except
    numbers = (input("How many numbers? "))

    # Loop through the numbers. (Be sure to cast the string into an integer.)
#have to have the try for it to work this way
    try:
        numbers = int(numbers) + start_value
        for num in range(start_value, numbers):
        
        #print each number in the range
            print(num)

        #set the start value equal to the number chosen so if they continue they sff on fo iy
            start_value = numbers
    except Exception as e:
                print(f"You input {numbers} which is not a number... ")

        # Print each number in the range


    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")
