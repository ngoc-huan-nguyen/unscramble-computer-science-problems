"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

def get_period_time(x):
    return int(x[3])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    periods = list(map(get_period_time, calls))
    max_period = max(periods)
    max_period_index = periods.index(max_period)
    record = calls[max_period_index]
    print(record[0] + ' spent the longest time, ' + str(max_period) + ' seconds, on the phone during September 2016.')
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

