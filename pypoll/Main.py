# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidateNames = []
candidateVotes = {}

# Winning Candidate and Winning Count Tracker
winner = ""
winningVotes = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="\n")

        # Increment the total vote count for each row
        total_votes +=1

        # Get the candidate's name from the row
        candidateName = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidateName not in candidateNames:
            #add candidate name to list
            candidateNames.append(candidateName)
            #count vote for candidate
            candidateVotes[candidateName] = 1
        else:
            #if candidate exists
            candidateVotes[candidateName] += 1      
        

for candidate, votes in candidateVotes.items():
    if votes > winningVotes:
        winningVotes = votes
        winner = candidate

with open(file_to_output, "w") as txt_file:

    # Generate the output summer and print it
    output = (
    f"Election Results\n"
    f"\n"
    f"------------------------------------------------------------------\n"
    f"\n"
    f"Total Votes: {total_votes}\n"
    f"\n"
    f"------------------------------------------------------------------\n"
    )
    print(output)
    txt_file.write(output)   
    
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidateVotes.items():
        vote_percentage = (votes/total_votes) * 100
        candidate_result = f"\n{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_result)
        txt_file.write(candidate_result)
        
    # Generate Winning Candidate Summary    
    winning_summary = (
    f"---------------------------------------------------------------\n"
    f"\n"
    f"Winner: {winner}\n"
    f"\n"
    f"---------------------------------------------------------------\n"
    )
        
    print(winning_summary)

    #Save the output as a text file
    txt_file.write(winning_summary)
