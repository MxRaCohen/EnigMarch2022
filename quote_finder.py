"""
Author: Ra
Purpose: Famous quote finder to match the form: https://enigmarch.com/codeword/

10 2 25    26 17 ,   14 12 17    26 2 18 14    17 4 21 2 7 3 1 8 17 

5 3 25 14    11 18   14 12 17    5 6 24 24 8 17 ,    14 12 17 

5 25 2 23 17 18 18    2 10    18 2 8 16 11 4 9 ,    4 2 14 

14 12 17    18 2 8 6 14 11 2 4    11 14 18 17 8 10 . 

– 17 25 4 2   25 6 1 11 20 

Find your next puzzle at enigmarch.com/ 4 3 26 17 18

"""
import csv

all_quotes = dict()
webminer_file = "webminer_quotes.csv" # https://thewebminer.com/buy-famous-quotes-database    (~35,000)

"""
desired quote shape: "3 2, 3 4 9 4 2 3 6, 3 7 2 7, 3 3 8 6." - 4 5
"""

# extracts raw names from the webminer dataset and adds them to provided dictionary 
def open_webminer_quotes(quotes_dict, input_file=webminer_file):
	with open(input_file) as f:
		print(f.readline())
		for line in f.readlines():
			new_line = line.split(';')
			quotes_dict[new_line[0]] = new_line[1]

# extracts raw names from the big quotes dataset and adds them to provided dictionary 
def open_big_quotes(quotes_dict, input_file=reduced_file):
	with open(input_file) as f:
		for line in f.readlines():
			new_line = line.split('"')
			quotes_dict[new_line[0]] = new_line[1]

# create class for each name
class Person:
	def __init__(self, name):
		self.original = name
		self.name = name[1:-1]
		split_names = self.name.split()
		self.first_name = str(split_names[0])
		self.last_name = str(split_names[-1])

		# cover middle names
		if len(split_names) > 1 and self.last_name != split_names[1]:
			self.middle_name = split_names[1:-1]

	def __str__(self):
		return f'{self.name}'

all_people = list()
length_candidates = list()
letter_candidates = list()
ideal_candidate = list()
for name in raw_names:
	# make a person and add them to our big list
	candidate = Person(name)
	all_people.append(candidate)

	# Initialiize candidacy
	len_can = False
	let_can = False

	# find people of type 4,5 and add them as potential answers
	if len(candidate.first_name) == 4 and len(candidate.last_name) == 5:
		len_can = True

	# if this candidate fulfills second letter of the first matching first letter of second
	if len(candidate.first_name) > 1 and candidate.first_name[1] == candidate.last_name[0]:
		let_can = True

	if len_can:
		length_candidates.append(candidate)
	if let_can:
		letter_candidates.append(candidate)
	if len_can and let_can:
		ideal_candidate.append(candidate)
		print(candidate)

"""
print("length candidates")
for candidate in length_candidates:
	print(candidate)

print("letter candidates")
for candidate in letter_candidates:
	print(candidate)
"""

