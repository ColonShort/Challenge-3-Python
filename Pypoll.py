# For this challenge we need: 
# -total number of votes cast, 
# -complete list of candidates who receieved votes, 
# -percentage of votes each candidate won, 
# -total number of votes each candidate won
# -winner of the election based on popular vote
import os
import csv

file_path = os.path.join("Resources", "election_data.csv")

number_votes = 0
candidate_list = []
votes_per_candidate = {}

with open(file_path, 'r', newline="", encoding="utf-8") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvReader)

    for row in csvReader:
        number_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            votes_per_candidate[candidate_name] = 0

        votes_per_candidate[candidate_name] += 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {number_votes}")
print("-------------------------")

for candidate_name, votes in votes_per_candidate.items():
    percentage = (votes / number_votes) * 100
    percentage_formatted = "{:.3f}".format(percentage)
    print(f"{candidate_name}: {percentage_formatted}% ({votes})")

print("-------------------------")

winner = max(votes_per_candidate, key=votes_per_candidate.get)
print(f"Winner: {winner}")

print("-------------------------")



