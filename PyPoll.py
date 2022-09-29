# Add our dependencies
import os

import csv

#Assign a variable to load a file from path
file_to_load = os.path.join("election_results.csv")
file_to_save = os.path.join("Analysis" , "election_results.txt")

#initalize a total vote counter
total_votes = 0

#Candidate option and candidate votes
candidate_options =[]

#Delclare the empty dictionary
candidate_votes = {}

#winning candaidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the elction results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
  
    #Print each row
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidates votes count
            candidate_votes[candidate_name] = 0
            #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping the counts
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")

#Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)