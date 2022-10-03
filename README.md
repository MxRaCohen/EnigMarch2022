# EnigMarch2022
Creative attempts to brute-force a particularly elusive meta-puzzle on the EnigMarch website in 2022, [codeword](https://enigmarch.com/codeword/).

> Firstly, I’m glad you found this part of the puzzle hunt. I’m starting you off with an appropriate quote.

> 10 2 25    26 17 ,   14 12 17    26 2 18 14    17 4 21 2 7 3 1 8 17 

> 5 3 25 14    11 18   14 12 17    5 6 24 24 8 17 ,    14 12 17 

> 5 25 2 23 17 18 18    2 10    18 2 8 16 11 4 9 ,    4 2 14 

> 14 12 17    18 2 8 6 14 11 2 4    11 14 18 17 8 10 . 

> – 17 25 4 2   25 6 1 11 20 

> Find your next puzzle at enigmarch.com/ 4 3 26 17 18


# Forwards-Backwords on the quote/author
The quote has both an author and a body. 

Hypothesis
> If either author or quote body are known, enough letters would be discovered to deduce the rest and solve.

Method
* Scrape quotes websites to generate a pool of candidate quotes.
* Match quotes shape to the shape of the solution quote.
* Download existing repository of famous people. 
* Match name shape of quote author to famous people registry. 


# Dictionary Attack
The answer is 5 letters long.

Hypothesis
> If the answer is a word, simply try every 5-letter word in a dictionary appended to the base url to find the next puzzle. 

Method
* Find comprehensive shortform wordlist.
* Prune to only 5 letter words and generate candidate urls.
* Hit every candidate url and record all that were returning non-404 error pages. 

