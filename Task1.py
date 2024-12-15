"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    all_numbers = set()
    for l in texts:
        all_numbers.add(l[0])
        all_numbers.add(l[1])
    print('There are ' + str(len(all_numbers)) + ' different telephone numbers in the records')


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    all_numbers = set()
    for l in calls:
        all_numbers.add(l[0])
        all_numbers.add(l[1])
    print('There are ' + str(len(all_numbers)) + ' different telephone numbers in the records')

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
