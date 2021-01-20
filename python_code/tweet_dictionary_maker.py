import pandas as pd
import numpy as np
import json
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# create a dictionary for the vocabulary in trump's tweets


# def clean_text():
#     all_tweets = []
#     with open('../data/tweets_until_01_08_2021.json', 'r') as f:
#         trump_dict = json.load(f)
#         trump_tweet_list = []
#         for tweet in trump_dict:
#             data = tweet["text"], tweet["date"]
#             trump_tweet_list.append(data)


def load_data():
	clean_tweet_list = []
	# import the csv file and extract the text entries
	with open('../data/tweets_until_01_08_2021.json', 'r') as f:
		trump_dict = json.load(f)
		tweet_list = []
		for tweet in trump_dict:
			data = tweet["text"]
			tweet_list.append(data)
	return tweet_list

def clean_text(tweet_list):
	for text in tweet_list:
		text = text.replace('&amp', '')
		text = text.replace('U.S.', 'usa')
		text = text.replace('RT', '')
		text = text.replace('dems', 'democrats')
		tokens = text.split()
		tokens = [word.lower() for word in tokens]
		content_words = [w for w in tokens if not w in stop_words]
# Remove punctuation no roman alphabet words from each tweet, add  or c=="#" or c=="@" to keep # and @
		tokens = ["".join(c for c in word if c.isalpha()) for word in tokens]
		# tweet_string = tweets_text[i]
		# tweet_list = list(tweet_string.split(" "))
	return tokens
# def to count word frequency and make a vocab list of all words used
def word_counter():
	tweets_text = load_data()
	clean_tweets = clean_text(tweets_text)
	# Create a dictionary with the vocabulary and their tweet ids
	DF = {}
	for i in range(len(clean_tweets)):
		tweet_string = clean_tweets[i]
		tweet_list = list(tweet_string.split(" "))
		content_word_tweet = [w for w in tweet_list if not w in stop_words]

		for w in content_word_tweet:
			try:
				DF[w].add(i)
			except:
				DF[w] = {i}
	for word in DF:
		DF[word] = len(DF[word])

	sorted_frequency = sorted(DF.items(), key = lambda x: x[1], reverse = True)
	total_vocab = [x for x in DF]
	print(f"There are {len(total_vocab)}  unique words after cleaning")
	print(f"The top 40 words are {sorted_frequency[1:40]}")

word_counter()
