# Pybank Challenge
# from within the data set find: how many months are in the data set, total profits or losses, average change, greatest increase and decrease
import os  # this allows the file to have file handling functions

import csv  # this is so we can read csv files

# file_path is the variable we use to navigate to the data set in another folder
file_path = os.path.join("Resources", "budget_data_new.csv")

#print (file_path) this is so we can see that our file path is working within git

#these are empty lists to store our data in
profits_losses = []
average_change = []
date = []

#this is us telling python that all our variables start at 0
count = 0
total_profits_and_losses= 0
total_change = 0
initial_profits = 0

with open(file_path, 'r', encoding="utf-8") as csvFile:  # with open function lets you use the variable file_path as an object, r is for read mode
    # this uses the csvFile that we just made in the step above this one to name the reader in the open with function and also tells the file what to seperate a list with, hence the comma
    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvReader)

    # insert for loop
    for row in csvReader:
        #after we got the header out of the way, we can count the rows to add up all the months using count, and for every count add 1
        count = count + 1

        #append this data so that we can get our greatest increase and decrease in profits
        date.append(row[0])

        profits_losses.append(row[1])
        total_profits_and_losses = total_profits_and_losses + int(row[1])

        total_profits = int(row[1])
        monthly_profit = total_profits - initial_profits

        average_change.append(monthly_profit)

        total_profits_and_losses = total_profits_and_losses + monthly_profit
        initial_profits = total_profits

        average_profits = (total_profits_and_losses/count)

        greatest_inc = max(average_change)
        greatest_dec = min(average_change)
        
        increase_date = date[average_change.index(greatest_inc)]
        decrease_date = date[average_change.index(greatest_dec)]

    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profits_and_losses))
    print("Average Change: " + "$" + str(int(average_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_inc) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_dec)+ ")")     

with open("finances.txt", "w") as text:
    text.write ("Financial Analysis")
    text.write ("----------------------------------------------------------")
    text.write ("Total Months: " + str(count))
    text.write ("Total Profits: " + "$" + str(total_profits_and_losses))
    text.write ("Average Change: " + "$" + str(int(average_profits)))
    text.write ("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_inc) + ")")
    text.write ("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_dec)+ ")")   

#total_profitsandlosses =
#average_change =
#greatest_Inc = 
#greatest_Dec = 