import os
import csv

csvpath= os.path.join('..', 'PyPoll', 'election_data.csv')

with open('election_data.csv', newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header= next(csvreader)
    print(f"CSV Header : {csv_header}")

    for line in csvreader:
        print((line))