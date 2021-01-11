import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
import pandas as pd
import matplotlib.pyplot as plt
import string
import csv
import numpy as np
import re
from wordcloud import WordCloud, STOPWORDS
#import standard stopwords from NLTK, may need to customize this list
stop_words = set(stopwords.words('english'))

# take the original tweets , remove stopwords and punctuation other than #,#, 
# remove some unneccessary tokens and make everything lowercase: create a datframe with sentiment and Time
def pos_tagger(word):
	"""Map POS tag to first character lemmatize() accepts"""
	tag = nltk.pos_tag([word])[0][1][0].upper()
	tag_dict = {"J": wordnet.ADJ,
				"N": wordnet.NOUN,
				"V": wordnet.VERB,
				"R": wordnet.ADV}

	return tag_dict.get(tag, wordnet.NOUN)

def clean_data():
	clean_tweet_list = []
	# import the csv file and extract the text entries
	with open("/Users/imacmattimacmatt/Desktop/bootcamp work/Github_Repositories/trump_tweet_analysis/data/condensed_dow_and_sentiment.csv", "r") as f:
		csvReader = csv.DictReader(f)
		tweet_list = []
		short_tweets = []
		clean_tweet_list = []
		time_list = []
		Vader_list = []
		for row in csvReader:
			data = row["Tweet_text"], row["Time"], row["Vader_compound"]
			tweet_list.append(data)

	for tweet in tweet_list:
		text = tweet[0]
		time = tweet[1]
		Vader_compound = tweet[2]
		#remove RT, &amp, hyperlinks: preserve U.S.
		text = re.sub(r'https.*', '', text)
		text = text.replace('&amp', '')
		text = text.replace('U.S.', 'usa')
		text = text.replace('RT', '')
		text = text.replace('dems', 'democrats')

		# split tweets into tokens by white space
		tokens = text.split()
		# make lower case
		tokens = [word.lower() for word in tokens]
	# Remove punctuation no roman alphabet words from each tweet, add  or c=="#" or c=="@" to keep # and @
		tokens = ["".join(c for c in word if c.isalpha()) for word in tokens ]
	# remove stop words
		content_word_tweet = [w for w in tokens if not w in stop_words]
	# lemmatize the nouns (men didn't work)
		lemmatizer = WordNetLemmatizer()
		lemmatized_output = ' '.join([lemmatizer.lemmatize(w)for w in content_word_tweet])
		lemmatized = [lemmatizer.lemmatize(w, pos_tagger(
			w)) for w in nltk.word_tokenize(lemmatized_output)]

#Spacy lemmatizer
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(lemmatized_output)
# mytokens = [word.lemma_ if word.lemma_ !="-PRON-" else word.lower_ for word in doc]
		# turn the leammatized string back into a list
		# lemmatized_tweet = list(lemmatized.split(" "))
		# print(lemmatized_output)
		# number_of_tokens = len(lemmatized_tweet)
		if (len(lemmatized)>1):
			clean_tweet_list.append(lemmatized)
			time_list.append(time)
			Vader_list.append(Vader_compound)
		else:
			short_tweets.append(lemmatized)

		# total_tokens = total_tokens+number_of_tokens
	# print(f"tweets with search term {clean_tweet_list}")
	# print(f"In the data set there are {len(clean_tweet_list)} tweets")
	# print(f"In the data set there are  {total_tokens} tokens/words")
	word_frequency_df = pd.DataFrame(clean_tweet_list)
	word_frequency_df["Time"] = time_list
	word_frequency_df["Vader_compound"] = Vader_list
	# print (word_frequency_df) 
	
	with open("/Users/imacmattimacmatt/Desktop/bootcamp work/Github_Repositories/trump_tweet_analysis/data/clean_tweet_list.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(clean_tweet_list)
	
		# return clean_tweet_list, word_frequency_df
	print(short_tweets)
	print(len(clean_tweet_list))
	print(len(short_tweets))

clean_data()
# def to count word frquency and make a vocab list of all words used
# def word_counter():
# 	# hashtags = []
# 	# references = []
# 	data = clean_data()
# 	# results is the cleaned tweets
# 	tweets_text = data[0]
# 	#dataframe includes vader score and time
# 	tweets_df = data[1]
# 	# print(results_df)
# 	# Create a dataframe with the vocabulary and their tweet ids
# 	DF = {}
# 	for i in range(len(tweets_text)):
# 		tokens = tweets_text[i]
# 		for w in tokens:
# 			try:
# 				DF[w].add(i)
# 			# .add is a set function (creates a set), so it will only add 1 time, set values have to be unique
# 			except:
# 				DF[w] = {i}
# 	# the except adds the word if the word doesn't exist in the dictionary (creates a key and stores the first index)
	
# 	# print(DF.items())
# 	for word in DF:
# 		#get the number of occurences of each word
# 		DF[word] = len(DF[word])
# 		#extract the words with # and @
# 		# if '#' in word:
# 		# 	hashtags.append(word)
# 		# if '@' in word:
# 		# 	references.append(word)
# 	# from collections import Counter
# 	# number = Counter(references)
# 	# print(f"sample references: {references[0:9]} sample hashtags {hashtags[0:9]}")
# 	# print(f"There are {len(hashtags)} hashtags \nThere are {len(references)} references")
# 	sorted_frequency = sorted(DF.items(), key = lambda x: x[1], reverse = True)
# #	remove the blank spaces at position 0
# 	print(f"The top 40 words are {sorted_frequency[1:40]}")
# 	# create a list of unique words
# 	total_vocab = [x for x in DF]
# 	print(f"There are {len(total_vocab)}  unique words after removing stop words")

# word_counter()
