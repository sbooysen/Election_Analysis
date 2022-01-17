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

# Close the file.
election_data.close()

#indirect file opening
import csv
import os
file_to_load = os.path.join("Resources","election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file: 
    txt_file.write("Arapahoe\nDenver\nJefferson")

