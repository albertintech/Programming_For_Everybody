# pylint: disable=invalid-name, missing-docstring, unspecified-encoding

# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Problem break down:
# Question: Who sent the most emails?
# Input: mbox-short.txt
# Output: [email] [number of appearances] => cwen@iupui.edu 5

# Algo:
# Read text file
# Isolate "From " lines. Note: Not equal to "From:" lines
# Isolate second word in from line, ie the sender email address
# Count each occurence of sent email from each email address
# Use a dictionary to track emails to counts
# Use a loop to find the highest email count and corresponding address
# Print email and count number of highest sender => cwen@iupui.edu 5
