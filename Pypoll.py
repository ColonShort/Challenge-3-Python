# For this challenge we need: 
# -total number of votes cast, 
# -complete list of candidates who receieved votes, 
# -percentage of votes each candidate won, 
# -total number of votes each candidate won
# -winner of the election based on popular vote
import os #import the operating system

import csv #

#file path to the election data
file_path = os.path.join("Resources", "election_data.csv")

#lists created to hold data
number_votes = []
candidate_list = []
votes = []
percentages = []

#set all variables to 0/blank
vote_count = 0
votes_per_candidate = 0
vote_percentage = 0
winner = ""

with open(file_path, 'r', newline="", encoding="utf-8") as csvFile:  # with open function lets you use the variable file_path as an object, r is for read mode
    # this uses the csvFile that we just made in the step above this one to name the reader in the open with function and also tells the file what to seperate a list with, hence the comma
    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvReader)

    #create the for loop
    for row in csvReader:
        #after we got the header out of the way, we can count the rows to add up total votes
        vote_count = vote_count + 1

        #list of candidates
        candidate_name = row[2]

        #lets create an if statement to add candidates to our candidate list if they havent alreadyu been added
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            
            #lets also track the count of votes per candidate with
            votes_per_candidate[candidate_name] = 0
        
            #everytime a canidate gets named on the data sheet, this will add another count to the respective candidates votes
            votes_per_candidate[candidate_name] += 1
    for
print("Election Results")
print("--------------------------")
print(f"Total Votes: {number_votes}")
for count in range(len(candidate_list)):
    print(f"{candidate_name[count]}: {percentages[count]}% ({vote_count[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

