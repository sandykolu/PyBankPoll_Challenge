import os
import csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
output = os.path.join('.', 'analysis', 'budget_analysis.txt')
change_list = []
month_list = []

# Create list for max increase with the current max value for profits/losses as zero and null month
max_increase = ["",0]

# Create list for max decrease with the current min value for profits/losses as99999999999 (some very high value compared to the dataset) and null month
max_decrease = ["",99999999999]

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#   print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#   print(f"CSV Header: {csv_header}")
    rowcount = 0
    total = 0
    
#   Extract the value of the first row in the file. This needs to be done outside of the for loop
    first_row = next(csvreader)
#   print(first_row)
    total += int(first_row[1])
    
#   Initialize the last total to the first row proft/loss
    prev_total = int(first_row[1])

    # Read each row of data after the header
    for row in csvreader:
        
#       Get the number of rows in the file to get the count of months
        rowcount += 1
    
#       Get the net total amount of “Profit/Losses” over the entire period
        total += int(row[1])
        
#       Get the change by subtracting the current row in the for loop of the dataset with the previous row
        change = int(row[1]) - prev_total
    
#       Set the current row profit loss value as the previous row value
        prev_total = int(row[1])
    
#       print(change)

#       Create the change list by appending the changes
        change_list.append(change)
    
#       Create the corresponding month list by appending the months
        month_list.append(row[0])
    
#       Find the greatest increase in profits (date and amount) over the entire period
        
        if change > max_increase[1]:
            max_increase[1] = change
            max_increase[0] = row[0]
        
#       Find the greatest decrease in profits (date and amount) over the entire period
        if change < max_decrease[1]:
            max_decrease[1] = change
            max_decrease[0] = row[0]
        
#       Calculate the changes in “Profit/Losses” over the entire period, then find the average of those changes
        average_change = round(sum(change_list)/len(change_list),2)
               
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {rowcount+1}") # Adding 1 for the first row
    print(f"Total: ${total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})")
    print(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")
    
    Analysis=(
        f"\nFinancial Analysis\n"
        f"-----------------------------\n"
        f"Total: ${total}\n"
        f"Average Change: ${average_change}\n"
        f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n"
        f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n"
            )
    
    with open (output, "w") as txt_file:
        txt_file.write(Analysis)
