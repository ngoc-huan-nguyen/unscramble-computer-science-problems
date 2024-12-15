"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

def get_receiver_code(x):
    if ' ' in x[1]:
        return x[1][0:4]
    elif '(' in x[1]:
        return x[1][0:x[1].index(')') + 1]
    elif x[1].startswith('140'):
        return '140'

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    bangalore_calls = filter(lambda x: x[0].startswith('(080)'), calls)

    receiver_codes = map(lambda x: get_receiver_code(x), list(bangalore_calls))

    sorted_data = sorted(list(set(list(receiver_codes))))

    print('The numbers called by people in Bangalore have codes: ', sorted_data)
    
    total_bangalore_caller = len(list(filter(lambda x: x[0].startswith('(080)'), calls)))
    total_bangalore_receiver = len(list(filter(lambda x: x[0].startswith('(080)') and x[1].startswith('(080)'), calls)))
    percent = total_bangalore_receiver / total_bangalore_caller * 100
    
    print(str(round(percent,2)) + ' percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
