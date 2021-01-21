import pandas as pd
import numpy as np
import json
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# a program to create a dictionary for the vocabulary in trump's tweets

# import the tweets and extract the text entries
def load_data():
	clean_tweet_list = []
	with open('../data/tweets_until_01_08_2021.json', 'r') as f:
		trump_dict = json.load(f)
		tweet_list = []
		for tweet in trump_dict:
			data = tweet["text"]
			tweet_list.append(data)
	return tweet_list

#def to replace some abreviations,delete unecessary symbols, remove punctuation and stop words
def clean_text():
	clean_tweet_list = []
	tweet_list = load_data()
	for tweet in tweet_list:
		tokens = tweet.split()
		tokens = [word.lower() for word in tokens]
		content_words = [w for w in tokens if not w in stop_words]
		text_alphabetic = ["".join(c for c in word if c.isalpha()) for word in content_words]
		text = " ".join(text_alphabetic)
		text = text.replace('amp', '')
		text = text.replace('realdonaldtrump', '')
		# text = text.replace('rt', '')
		text = text.replace("thanks", "thank")
		text = text.replace('u.s.', 'usa')
		# text = text.replace('rt', '')
		text = text.replace('dems', 'democrats')
		text_list = text.split()
		clean_tweet_list.append(text_list)
	return clean_tweet_list

# def to count word frequency and make a vocab list of all words used
def dictionary_maker():
	clean_tweets = clean_text()
	DF = {}
	for i in range(len(clean_tweets)):
		tweet_string = clean_tweets[i]
		# tweet_list = list(tweet_string.split(" "))
		content_word_tweet = [w for w in tweet_string if not w in stop_words]
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

dictionary_maker()
