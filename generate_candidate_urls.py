"""
Author: Ra
Purpose: generates a list of urls to check with enigmarch spider
"""

# initialize domain 
url_stem = "https://enigmarch.com/"

# initialize candidates
wordlist_file = "wordlist-en.txt"
n = 5

# initialize output destination
output_file = "url_candidates.txt"

# extracts raw words of n length from the dataset
def generate_candidate_words(input_file, n, output_file):
	new_urls = []
	with open(input_file) as f:
		for line in f.readlines():
			word = line.strip()[1:-1]
			if len(word) == n:
				new_url = url_stem + word + "/" + " \n"
				new_urls.append(new_url)
	with open(output_file, "w") as o:
		o.writelines(new_urls)

generate_candidate_words(wordlist_file, 5, output_file)