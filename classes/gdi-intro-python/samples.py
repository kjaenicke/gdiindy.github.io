# You can just run this file but the examples below
# are mostly meant to be copied into your own files
# and adjusted as needed for you own project

###############
# CSV PARSING #
###############

import csv

# Let's take a csv file name from the user
csvFilePath = raw_input('Please enter csv file name or path: ')
csvFilePath = csvFilePath or 'sample.csv'
# Now let's open this file with python and assign the file to a variable
# using the built in open() function
csvFile = open(csvFilePath)
# Now let's use the csv library we imported to parse the csv file we opened
csvData = [a for a in csv.reader(csvFile)]
# csvData is now a list [line1, line2, line3, ...] where each line is also a list of values
# for instance [['First Name', 'Last Name', 'Age'], ['Jane', 'Doe', '54'], ['John', 'Doe', '49'], ['Foo', 'Bar', '5']]
# So after parsing a csv file, we have a list of lists of values. Let's go though them
# We don't actually want to print the first line because it's a header. Let's remove it
csvData.pop(0)
for line in csvData:
    # inside this block, line is just a list of items, representing a line in the csv file
    print line[0] + ' ' + line[1] + ' is ' + line[2] + ' years old.'


#########################
# FILE WRITING AND TIME #
#########################

# there is a datetime module from which we import datetime
from datetime import datetime

now = datetime.now()
nowString = now.isoformat()

# Let's open a file to write to (using a second argument 'w' for write). If it doesn't exist yet it will be created
myFile = open('timeprint.txt', 'w')
myFile.write(nowString)
# now that the file is written, we need to close it
myFile.close()
# the file now holds the time at which this file was executed by python


######################
# LIST COMPREHENSION #
######################

from math import sqrt # square root
# list of all int numbers from 0 to 99
range(100)
# or could also be
[a for a in range(100)]

# list of all int numbers from 1 to 100
[a + 1 for a in range(100)]

# list of all int numbers from 0 to 99 except for 55
[a for a in range(100) if a != 55]

# challenge: list of all prime numbers between 0 and 9999 (not optimized for performance)
print [a for a in range(2, 10000) if len([b for b in range(int(sqrt(a))) if a % (b + 1) == 0]) == 1]


##########################
# COMMAND LINE ARGUMENTS #
##########################

import sys

# if you called the program using an additonal argument, like "python samples.py foobar" then we'll print foobar
# but if you have not we'll just no do anything and pass
if len(sys.argv) > 1:
    print sys.argv[1] # this line prints the second argument, the first being samples.py
else:
    pass # this line does nothing
