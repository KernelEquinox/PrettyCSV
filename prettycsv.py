#!/usr/bin/env python

import sys

# Print help text.
if len(sys.argv) < 2:
	# Properly format script name for both Windows and Linux.
	if "/" in sys.argv[0]:
		script = sys.argv[0].split("/")[-1]
	else:
		script = sys.argv[0].split("\\")[-1]
	print "\nPrettyCSV\n"
	print "Description:"
	print "    Analyzes a CSV file (or any delimited text file)"
	print "    and prints the data in MySQL format.\n"
	print "Usage:"
	print "    %s [delimiter] [col name] [col name] ... [file]\n" % script
	print "Examples:"
	print "    %s * User \"Password Hash\" mysql.txt" % script
	print "    %s : ID Username Password Email phpbb.txt" % script
	print "    %s , \"Full Name\" SSN City State Zip experian.csv\n" % script
	exit()

# Cleanly handle nonexistent files and mistyped columns.
try:
	file = open(sys.argv[-1], "r")
except:
	print "\nERROR: File '%s' does not exist!\n" % sys.argv[-1]
	exit()

# Set up variables and placeholders.
delim = sys.argv[1]
fields = sys.argv[2:-1]
fieldnum = len(fields)
entries = []
maxlen = []
linenum = 0

# Check if delimiter is of wrong length.
if len(delim) != 1:
	print "\nERROR: Delimiter must only be one character.\n"
	exit()

# Count number of expected input fields.
for i in range(0, fieldnum):
	maxlen.append(len(fields[i]))

# Load data into memory and strip newlines.
for line in file:
	entries.append(line.replace("\n",""))
file.close()

# Calculate the width of each column.
for entry in entries:
	linenum += 1
	entry = entry.split(delim)
	# Check if the number of headers don't match the parsed data.
	if len(entry) != len(maxlen):
		print "\nERROR: Incorrect number of delimiters on line %d!\n" % linenum
		exit()
	for i in range(0, len(maxlen)):
		if len(entry[i]) > maxlen[i]:
			maxlen[i] = len(entry[i])

# Create a border of the proper length.
border = ""
for fieldlen in maxlen:
	border += "+-" + "-" * fieldlen + "-"
border += "+"

# Print the top border.
print border

# Print the headings.
for i in range(0, len(fields)):
	space = maxlen[i] - len(fields[i])
	print "| %s%s" % (fields[i], "\x20"*space),
print "|"

# Print the separator between the headers and the data.
print border

# Print each line of formatted data with proper borders and spacing.
for entry in entries:
	entry = entry.split(delim)
	for i in range(0, len(maxlen)):
		space = maxlen[i] - len(entry[i])
		print "| %s%s" % (entry[i], "\x20"*space),
	print "|"

# Print the bottom border.
print border