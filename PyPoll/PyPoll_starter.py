# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os
import operator



# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll/Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll/analysis", "election_analysis.txt")  # Output file path



# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts


Candidate = []
Candidate_count = []
Winner_list = []

# Winning Candidate and Winning Count Tracker

Winner = []
Winn_count = 0


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)


    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row

        total_votes = total_votes + 1


        # Get the candidate's name from the row

        
        candidate_value = row[2]

        # If the candidate is not already in the candidate list, add them

        Candidate.append(candidate_value) if candidate_value not in Candidate else ""

        # Add a vote to the candidate's count

        Candidate_count.append(candidate_value)



     # Loop through the candidates to determine vote percentages and identify the winner
     # Get the vote count and calculate the percentage
    for i in Candidate:
     coutcandidates = Candidate_count.count(i)
     percent = round((coutcandidates/total_votes),5)*100
     Winner_list.append([i,percent,coutcandidates])




# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    
    print(Winner_list)

  
    # sorts in place
    Winner_list.sort(reverse=True,key=lambda x: x[2])



    print (Winner_list)

    # Write the total vote count to the text file
    # Print and save each candidate's vote count and percentage
    # Generate and print the winning candidate summary

    csvwriter = csv.writer(txt_file, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(["Total Votes: " + str(total_votes) ])
    csvwriter.writerow(["-------------------------"])
    for i in Winner_list:
        csvwriter.writerow([ str(i[0]) + ":" + str(i[1]) + "% (" + str(i[2]) + ")"])
    csvwriter.writerow(["-------------------------"])

    # Update the winning candidate if this one has more votes
    csvwriter.writerow(["Winner: " + str((Winner_list[0])[0])])
    csvwriter.writerow(["-------------------------"])