# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os
from collections import Counter
import statistics



# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank/Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank/analysis", "budget_analysis.csv")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0


# Add more variables to track other necessary financial data
average_change = []
greatest_increase = 0
greatest_decrease = 0
previousrow = 0

date = []
profit = []




# Open and read the csv

with open(file_to_load, encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    


    # Track the total and net change

    
   
    # Process each row of data
    for row in reader:

        date.append(str(row[0]))
        profit.append(int(row[1]))




    value = None

    for i in profit:
     #   next_row = i+1
     #   value = int(next_row[0]) - int(i[0]) 

        if value != None:
            try:
                value = i - value
                average_change.append(value)
                value = i
            except StopIteration:
            #    # Break the loop if there are no more rows
                break    
        else: 
            average_change.append(0)
            value = i
    
    
 
    

    #cuenta la cantidad de meses
    months = sum(Counter(date).values())


    cleaned_csv = list(zip(date,profit,average_change))      
        
    
        

        # Track the total


        # Track the net change


        # Calculate the greatest increase in profits (month and amount)


        # Calculate the greatest decrease in losses (month and amount)

  
    months = sum(Counter(date).values()) 
    print(months)

  
    total_net = (sum(row[1] for row in cleaned_csv))
    print(total_net)

   # counts the elements' frequency -> it sums the values of repetitions

    #because of the data set can not be used
    #mean = int(statistics.mean(average_change))
    #print(mean)

    mean2 = sum(average_change)/(months-1)
    print(mean2)

    maxvalue = max(average_change)
    print(maxvalue)

    minvalue = min(average_change)
    print(minvalue)

    strminvalue = str(minvalue)

    

    #for (average_change) in cleaned_csv:
     #   if average_change == strminvalue:
     #       print(cleaned_csv)

    filtered_list_minvalue = [t[0] for t in cleaned_csv if t[2] == minvalue]
    mindate = (str(filtered_list_minvalue[0]))
    print(mindate)

    filtered_list_maxvalue = [t[0] for t in cleaned_csv if t[2] == maxvalue]
    maxdate = (str(filtered_list_maxvalue[0]))
    print(maxdate)

    print(cleaned_csv)

    
    #print(cleaned_csv)


with open(file_to_output, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["______________________________________"])
    csvwriter.writerow([])
    csvwriter.writerow(['Total Months: '+ str(months)])
    csvwriter.writerow(['Total: '+ str(total_net)])
    csvwriter.writerow(['Average change: '+ str(mean2)])
    csvwriter.writerow(['Greatest Increase in Profits: '+ maxdate + " ($"+str(maxvalue)+")"])
    csvwriter.writerow(['Greatest Decrease in Profits: '+ mindate + " ($"+str(minvalue)+")"])






    


    

 

# Calculate the average net change across the months


# Generate the output summary


# Print the output


# Write the results to a text file
#->with open(file_to_output, "w") as txt_file:
 #   txt_file.write(output)
