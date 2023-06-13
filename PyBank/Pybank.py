# Pybank Challenge
# from within the data set find: how many months are in the data set, total profits or losses, average change, greatest increase and decrease
import os
import csv

file_path = os.path.join("Resources", "budget_data.csv")

profits_losses = []
average_change = []
date = []

count = 0
total_profits_and_losses = 0
previous_profit_losses = 0

with open(file_path, 'r', encoding="utf-8") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvReader)

    for row in csvReader:
        count += 1
        date.append(row[0])

        profit_losses = int(row[1])
        profits_losses.append(profit_losses)
        total_profits_and_losses += profit_losses

        change = profit_losses - previous_profit_losses
        average_change.append(change)

        previous_profit_losses = profit_losses

    average_profits = sum(average_change[1:]) / (count - 1)
    greatest_inc = max(average_change)
    greatest_dec = min(average_change)
    
    increase_date = date[average_change.index(greatest_inc) + 1]
    decrease_date = date[average_change.index(greatest_dec) + 1]

    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: $" + str(total_profits_and_losses))
    print("Average Change: $" + "{:.2f}".format(average_profits))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_inc) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_dec) + ")")     

with open("finances.txt", "w") as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------------------------------------\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Total Profits: $" + str(total_profits_and_losses) + "\n")
    text.write("Average Change: $" + "{:.2f}".format(average_profits) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_inc) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_dec) + ")\n")
