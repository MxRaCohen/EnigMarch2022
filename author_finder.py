"""
Author: Ra
Purpose: Famous quote author finder
"""

raw_names = list()
input_file = "person_2020_update.csv" # https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/28201

# extracts raw names from the dataset
with open(input_file) as f:
	print(f.readline())
	for line in f.readlines():
		raw_names.append(line.split(",")[4])

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

def find_right_name_shape():
	length_candidates = list()
	for name in raw_names:
		# make a person and add them to our big list
		candidate = Person(name)

		# find people of type 4,5 and add them as potential answers
		if len(candidate.first_name) == 4 and len(candidate.last_name) == 5:
			length_candidates.append(candidate)
	return length_candidates



big_file = "big_quotes_dataset.csv" # https://github.com/ShivaliGoel/Quotes-500K      (~500,000)
reduced_file = "reduced_quotes_dataset.csv" # https://github.com/ShivaliGoel/Quotes-500K  (piped the first 10,000)

# find lines that contain a name candidate
def find_candidate_quotes(author_candidates, input_file=reduced_file):
	candidate_quotes = dict()
	with open(input_file) as f:
		for line in f.readlines():
			for author in author_candidates:
				if line.find(str(author)) >= 0:
					candidate_quotes[line[0:line.index(str(author))].strip('",')] = author
				elif line.find(f'{author.first_name} {author.last_name}') >= 0:
					candidate_quotes[line[0:line.index(f'{author.first_name} {author.last_name}')].strip('",')] = author
	return candidate_quotes


candidate_quotes = find_candidate_quotes(find_right_name_shape(), big_file)
print(len(candidate_quotes.keys()))

# remove all punctuation to find our ideal quote form
def remove_punc(input_string):
	punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	output_string = input_string
	for letter in output_string:
		if letter in punctuation:
			output_string = output_string.replace(letter, "")
	return output_string

refinement_1 = dict()
for quote in candidate_quotes.keys():
	new_quote = remove_punc(quote)
	if len(new_quote) < 55:
		continue
	new_quote_array = new_quote.split()
	# desired quote shape: "3 2, 3 4 9 4 2 3 6, 3 7 2 7, 3 3 8 6." - 4 5
	if len(new_quote_array[0]) == 3 and len(new_quote_array[1]) == 2 and len(new_quote_array[2]) == 3 and len(new_quote_array[3]) == 4:
		refinement_1[new_quote] = candidate_quotes[quote]
print(len(refinement_1.keys()))


for quote in refinement_1.keys():
	print(f'"{quote}" -{refinement_1[quote]}')
	print()

"""
print("length candidates")
for candidate in length_candidates:
	print(candidate)

print("letter candidates")
for candidate in letter_candidates:
	print(candidate)
"""

