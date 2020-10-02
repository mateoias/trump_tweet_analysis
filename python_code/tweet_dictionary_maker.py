import pandas as pd
import numpy as np
import csv

# take the original tweets , remove stopwords and punctuation other than #,#, 
# remove some unneccessary tokens and make everything lowercase: create a datframe with sentiment and Time
# def pos_tagger(word):
# 	"""Map POS tag to first character lemmatize() accepts"""
# 	tag = nltk.pos_tag([word])[0][1][0].upper()
# 	tag_dict = {"J": wordnet.ADJ,
# 				"N": wordnet.NOUN,
# 				"V": wordnet.VERB,
# 				"R": wordnet.ADV}

# 	return tag_dict.get(tag, wordnet.NOUN)

def load_data():
	clean_tweet_list = []
	# import the csv file and extract the text entries
	with open('../data/clean_tweet_list.csv', 'r') as f:
		csvReader = csv.reader(f)
		clean_tweet_list = []
		for row in csvReader:
			data = row
			clean_tweet_list.append(data)
	return clean_tweet_list



# def to count word frquency and make a vocab list of all words used
def word_counter():

	tweets_text = load_data()
	print(tweets_text)
	# Create a dictionary with the vocabulary and their tweet ids
	DF = {}
	for i in range(len(tweets_text)):
		tokens = tweets_text[i]
		for w in tokens:
			try:
				DF[w].add(i)
			# .add is a set function (creates a set), so it will only add 1 time, set values have to be unique
			except:
				DF[w] = {i}
	# the except adds the word if the word doesn't exist in the dictionary (creates a key and stores the first index)
	for word in DF:
		#get the number of occurences of each word
		DF[word] = len(DF[word])
		#extract the words with # and @

# 	# from collections import Counter
# 	# number = Counter(references)

	sorted_frequency = sorted(DF.items(), key = lambda x: x[1], reverse = True)
# #	remove the blank spaces at position 0
	print(f"The top 40 words are {sorted_frequency[1:40]}")
# 	# create a list of unique words
	total_vocab = [x for x in DF]
	print(f"There are {len(total_vocab)}  unique words after cleaning")
word_counter()
