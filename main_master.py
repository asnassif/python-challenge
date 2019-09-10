import os
import csv

csvpath= os.path.join('..', 'PyBank', 'budget_data.csv')
with open('budget_data.csv', newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header= next(csvreader)
    print(f"CSV Header : {csv_header}")


    for line in csvreader:
        print((line))

    total_months= csvreader.line_num
    print("Total_Months:", total_months-1)

    
    