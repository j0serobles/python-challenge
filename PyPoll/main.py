"""
===============================================================
.NAME
    PyPool/main.py
.WHAT
    PyPool main program, UCF Data Analysis and Visualization
    Bootcamp homework #3
.DATE
    09-JAN-2020
.AUTHOR
    engjoserobles@gmail.com
===============================================================
"""
# Required imports
import csv
import os

# Open csv file from Resources directory
csvpath = os.path.join('.', 'Resources', 'election_data.csv')


# Define a variable for the number of votes cast
total_votes = 0
# Define a dictionary structure, 
# key will be candidate name, value will be number of votes won.
poll_results_dict = dict()

#Traverse each line in the file, skipping the header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 

    # for each line
    for row in csvreader:
        total_votes += 1
        candidate = row[2] 
        # If the candidate does not exist, add it and set vote count to 1
        if candidate not in poll_results_dict:
            poll_results_dict[candidate] = 1
        else:
            # If the candidate already exists in the dictionary, increment vote count.
            poll_results_dict[candidate] += 1

# Create output string with the election results:

output_string = "\nElection Results\n"
output_string += "-------------------------\n"
output_string += "Total Votes: %d\n" % total_votes
output_string += "-------------------------\n"

winner_votes = poll_results_dict[max(poll_results_dict, key=poll_results_dict.get)]
winner_name = ""

for candidate, votes in poll_results_dict.items():
    output_string += "%s : %.3f (%d)\n" % ( candidate, ( (votes/total_votes) * 100), votes )
    if votes == winner_votes:
        winner_name += candidate
        winner_name += " "
        
output_string += "-------------------------\n"
output_string += "Winner: %s\n" % winner_name
output_string += "-------------------------\n"

# Print to standard output
print (output_string)

# Write to output file
fout = open("./Resources/election_results.txt", "w")
fout.write (output_string)
fout.close()