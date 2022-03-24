counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#The data we need to retrieve
#assign a variable for the file to load and the path
#Indirect path file opening
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
#open the election results.csv using the with statement as the filename obk election_Data
with open(file_to_load) as election_data:
    print(election_data)

    ##file_to_load = 'Resources\election_results.csv'

#open the election results and read the file
    ##election_data = open(file_to_load, 'r')

#use with so you dont have to open/close
    ##with open(file_to_load) as election_data:
        ##print(election_data)
#to do: perform analysis then close the file

###Creating a file for results to be written
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#use open statement to open the file as a text file
    #use with statement so you dont have to open and vlose
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n--------\nAnapahoe\nDenver\nJefferson")


#write some data to the file, #write() funct is from the os module

#close the file


