#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)):    # loop through all indexes for "lines" list
    if '* ' not in lines[i]:
        lines[i] = '* ' + lines[i] # add star to each string in "lines" list if it does not have a star in front already
    else:
        continue
text = '\n'.join(lines)
pyperclip.copy(text)
print("Your text has been modified.")