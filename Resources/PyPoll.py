#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the elevtion based on popular vote

file_to_load = 'Resources/election_results.csv'

# Direct opening: Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    print(headers)


