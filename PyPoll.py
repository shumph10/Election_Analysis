# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. init a total vote counter
total_votes = 0
#declare a list for candiate name option, 2 bc its in row 3 so index 2
candidate_options = []
#declare an empty dictionary for the candidates votes
candidate_votes = {}
#declare variables for winning candidate, winning count and percent
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. - uses csv module with the reader funct
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
            #add to the total vote count
            total_votes += 1

            #print the candidate name from each row
            candidate_name = row[2]

            #add the candidate name to the candidate list
            if candidate_name not in candidate_options:
                #add it to the list of candidates
                candidate_options.append(candidate_name)

                #2. Begin tracking that candidate's vote count using format to get the key from a dictionary
                candidate_votes[candidate_name] = 0
            #add a vote to that candidate's count
            candidate_votes[candidate_name] +=1

    #opens the election analysis text file
    with open(file_to_save,"w") as txt_file:
        #Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"-----------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-----------------------\n")
        print(election_results, end="")
        txt_file.write(election_results)
        #save the final vote count to the text file
        #det the % votes for each candidate by looping through the counts
        #iterate through the candidate list
        for candidate_name in candidate_votes:
            #2. retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #3 calc the % of votes - float bc want to change from int data type to float to get decimals
            vote_percentage = float(votes) / float(total_votes) * 100
            #4. print the candidate name and % of votes w/ 2 decimal places
            #changed from print to candidate_results variables for output to text file
            #print(f'{candidate_name}: received {vote_percentage:.1f}% of the vote.\n')

        #print each candidates name, vote count, and % of votes
            candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
            print(candidate_results)
            txt_file.write(candidate_results)

            #det winning vote count and candidate
            #determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #if true set winning count = votes(bc votes assigned to candidate b4) and winning % = vote %
                winning_count = votes
                winning_percentage = vote_percentage
                #set the winning candidate = to candidates name
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
        print(winning_candidate_summary)
        #save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)

    print(total_votes)
    print(candidate_options)
    print(candidate_votes)
    print(winning_candidate)