"""
Author: Ra
Purpose: dictionary wordlist attack for bruteforce enigmarch
https://enigmarch.com/codeword/
"""
import requests

# initialize domain to attempt and our headers
url_stem = "https://enigmarch.com/"
headers = {'user-agent': 'queuetie/0.0.1'}

# initialize candidates
wordlist_file = "wordlist-en.txt"
n = 5

# extracts raw words of n length from the dataset
def generate_candidate_words(input_file, n):
	len_n_words = list()
	with open(input_file) as f:
		for line in f.readlines():
			if len(line.strip()[1:-1]) == n:
				len_n_words.append(line)
	return len_n_words

# tests if given url returns an ok (2**) status and returns the current (potentially redirected) url
def test_url(url, headers=headers):
	request_response = requests.get(url, headers=headers)
	if request_response.status_code == requests.codes.ok:
		return request_response.url

# given a list of tails, appends each to given url stem, then returns a list of all valid urls
def find_valid_urls(tails, seen_urls, url_stem=url_stem, headers=headers):
	valid_urls = list()
	for word in tails:
		candidate_url = url_stem + word + "/"
		response_url = test_url(candidate_url, headers)
		seen_urls.add(response_url)
		if response_url == candidate_url:
			valid_urls.append(candidate_url)
	return valid_urls

# finds candidate urls, prints all valid ones
def print_valid_candidate_urls(input_file, n, seen_urls, url_stem, headers=headers):
	candidates = generate_candidate_words(input_file, 5)
	valid_urls = find_valid_urls(candidates, seen_urls, url_stem, headers)
	for valid_guess in valid_urls:
		print(valid_guess)
	return valid_urls


# run the code
# print_valid_candidate_urls(wordlist_file, 5, url_stem)

test_url_list = ["https://enigmarch.com/codeword/", "https://enigmarch.com/", "https://enigmarch.com/prompts/", "https://enigmarch.com/faq/", "https://enigmarch.com/resources/", "https://enigmarch.com/resources/inspiration-playlist/"]
# try a url thoroughly
def test_thoroughly(test_url_list, headers=headers):
	received_urls = set()
	for url in test_url_list:
		request_response = requests.get(url, headers=headers)
		if url != request_response.url:
			print(f'tried: {url} got: {request_response.url}')
		received_urls.add(request_response.url)
	print_valid_candidate_urls(wordlist_file, n, received_urls, url_stem)

	print("-----")
	for seen in received_urls:
		print(seen)

# test_thoroughly(test_url_list)



