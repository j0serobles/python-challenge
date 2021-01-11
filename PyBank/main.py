"""
===============================================================
.NAME
    PyBank/main.py
.WHAT
    PyBank main program, UCF Data Analysis and Visualization
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


#-------------------------------------------------------------------------------------------

def find_largest_profit_decrease(changes_dictionary):
    # Input : changes_dictionary        : The dictionary with the profit/loss changes per month  
    #                                     with format { 'Mon-YYYY': NNNNNNNN, 'Mon-YYYY: NNNNNN , ... }
    # Output: largest_changes_dictionary: A dictionary with keys = the largest profit decrease (loss) amount,
    #                                     and values = a list of months when it occurred, formatted like:
    #                                     { -NNNNNNN.NN : ['Mon-YYYY', 'Mon-YYYY', ...]}

    largest_changes_dictionary = dict() # The dictionary with results to return
    # find the largest value:
    largest_profit_decrease = min(changes_dictionary.values())

    # Reverse Lookup: For each amount that matches the greatest decrease in profit
    #  (loss) value, 
    # append the month to the associated list
    for month in changes_dictionary:
        change_amount = changes_dictionary[month]
        if change_amount == largest_profit_decrease:
            if str(largest_profit_decrease) not in largest_changes_dictionary:
                largest_changes_dictionary[str(largest_profit_decrease)]= [month]
            else:
                largest_changes_dictionary[str(largest_profit_decrease)].append(month)


    return largest_changes_dictionary
        
#-------------------------------------------------------------------------------------------

def find_largest_profit_increase(changes_dictionary):
    # Input : changes_dictionary        : The dictionary with the profit/loss changes per month  
    #                                     with format { 'Mon-YYYY': NNNNNNNN, 'Mon-YYYY: NNNNNN , ... }
    # Output: largest_changes_dictionary: A dictionary with keys = the largest profit increase amount,
    #                                     and values = a list of months when it occurred, formatted like:
    #                                     { NNNNNNN.NN : ['Mon-YYYY', 'Mon-YYYY', ...]}

    largest_changes_dictionary = dict() # The dictionary with results to return
    # find the largest value:
    largest_profit_increase = max(changes_dictionary.values())

    # Reverse Lookup: For each amount that matches the maximum value, append the month to the associated list
    for month in changes_dictionary:
        change_amount = changes_dictionary[month]
        if change_amount == largest_profit_increase:
            if str(largest_profit_increase) not in largest_changes_dictionary:
                largest_changes_dictionary[str(largest_profit_increase)]= [month]
            else:
                largest_changes_dictionary[str(largest_profit_increase)].append(month)


    return largest_changes_dictionary
        
#------------------------------------------------------------------------------------------

num_months = 0 # Number of months count
net_profit_or_loss = 0.0
profit_loss_changes = dict()
previous_month_profit_loss = 0.00

# Open csv file from Resources directory
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#Traverse each line in the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 
 
    # for each line
    for row in csvreader:
        
        current_month = row[0]
        current_profit_loss = float(row[1])
        # increment number of months counter
        num_months = num_months + 1
        # Accumulate net amount of profit or loss
        net_profit_or_loss = net_profit_or_loss + current_profit_loss
        profit_loss_changes[current_month] = (current_profit_loss - previous_month_profit_loss )
        previous_month_profit_loss = current_profit_loss

        # Average profit or loss amount
        average_profit_or_loss = net_profit_or_loss / num_months
    
    largest_increase = find_largest_profit_increase(profit_loss_changes)
    largest_decrease = find_largest_profit_decrease(profit_loss_changes)


         
print("Financial Analysis" + '\n' + "--------------------------------------" + '\n')
print("Number of Months: %d\n" % num_months)
print("Total profit/loss: %.2f\n" % net_profit_or_loss)
print("Average profit/loss: %.2f\n" % average_profit_or_loss)
# t = largest_increase.items()
print("Greatest Increase in Profits: %s " % list(largest_increase.keys())[0] )
for thevalue in largest_increase.values():
    print( "%s" % thevalue)


# print(find_largest_profit_increase(profit_loss_changes))   
# print(find_largest_profit_decrease(profit_loss_changes))       
# print(average_profit_or_loss)
        
# print(f"Total months : {num_months}" )
# print(f"Net Profit: { net_profit_or_loss }")
# print (profit_loss_changes)

#    Define a structure to store the change in Profit/Loss for each month, compared to the previous one
#    Save the greatest increase in profit in a variable
#    Save the greatest decrease in losses in a variable

# Print the results to the terminal and to a CSV file as:
# Financial Analysis
# ----------------------------
# Total Months: nn
# Total: $nnnnnnnnnn
# Average  Change: $nnnnnn.nn
# Greatest Increase in Profits: Mon-YYYY ($nnnnnnnn)
# Greatest Decrease in Profits: Mon-YYYY ($nnnnnnnn)
