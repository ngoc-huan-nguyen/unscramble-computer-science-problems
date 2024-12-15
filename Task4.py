"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

number_made_call = list(set(list(map(lambda x: x[0], calls))))
number_received_call = list(set(list(map(lambda x: x[1], calls))))

number_send_text = list(set(list(map(lambda x: x[0], texts))))
number_received_text = list(set(list(map(lambda x: x[1], texts))))

ignored_phones = list(set(number_send_text + number_received_text + number_received_call))

telemarketers = list(set(filter(lambda x: x not in ignored_phones, number_made_call)))
print('These numbers could be telemarketers: ', sorted(telemarketers))
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

