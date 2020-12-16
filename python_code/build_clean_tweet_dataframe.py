import re
import csv
import pandas as pd
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# a function to load the topic clusters from the CSV
def load_topic_words():
	topic_word_list = []
	with open("../data/topic_groups.csv", "r") as f:
		csvReader = csv.reader(f)
		for row in csvReader:
			data = row
			topic_word_list.append(data)
	topic_words_df = pd.DataFrame(topic_word_list)

# a function to let the user choose which topic to look at
def get_user_search_words():
	# check validity of user input
	while True:
		user_search_topic = input("Which topic would you like to view? There are 28 topics to choose from: ")
		if 0<int(user_search_topic)<29:
			break 
		else:
			print("Please enter an integer between 1 and 28.")
			continue
			
	# call the load data function
	topic_words_df = load_topic_words()
	# return the top ten words from the topic cluster selected by the user
	topic_number = 2 * (int(user_search_topic)-1)
	user_search_words = topic_words_df.iloc[1:11, topic_number]
	search_word_weights = topic_words_df.iloc[1:11, topic_number+1]
	print(f"The words you are searching for are {user_search_words}. Their relative weighting in the topic is {search_word_weights}")
	return user_search_words.values.tolist()

# a function to load the topic clusters from the CSV and return a dataframe of the top 10 words for each cluster
def load_topic_words():
	topic_word_list = []
	# import the csv file with the topic clusters and extract the text entries
	with open("../data/topic_groups.csv", "r") as f:
		csvReader = csv.reader(f)
		for row in csvReader:
			data = row
			topic_word_list.append(data)
	# create a dataframe of the top 10 words for each topic cluster
	data_df = pd.DataFrame(topic_word_list)
	return data_df

def import_tweets_and_sentiment():
# import the csv file and extract the text entries if the tweet has more than 5 words

	with open('../data/condensed_dow_and_sentiment.csv', 'r') as f:
		csvReader = csv.DictReader(f)
		tweet_list = []
		for row in csvReader:
			data = row["Time"], row["Vader_compound"], row["Tweet_text"]
			num_words = data[2].split(" ")
			if len(num_words) >5:
				tweet_list.append(data)
			for tweet in tweet_list:
				time = tweet[0]
				sentiment = tweet[1]
				text = tweet[2]
		return tweet_list

def clean_text(tweet_list):
	clean_tweet_list = []
	for tweet in tweet_list:
		text = tweet[2]
		text = re.sub(r'https.*', ' ', text)
		text = text.replace('&amp', '')
		text = text.replace('U.S.', 'usa')
		text = text.replace('dems', 'democrats')
		text = text.replace('RT', '')
		text = text.replace('-', '')
		text = text.replace('?', '')
		text = text.replace('.', '')
		text = text.replace('#', '')
		text = text.replace('@', '')
		text = text.lower()
		tokens = text.split()
		tokens = [w for w in tokens if not w in stop_words]
		text = ' '.join(map(str, tokens))
		clean_tweet_list.append(text)
	return clean_tweet_list
	

if __name__ == "__main__":
	tweet_list = import_tweets_and_sentiment()
	clean_tweet_list = clean_text(tweet_list)
	tweet_data_frame = pd.DataFrame(tweet_list, columns=["Time", "Sentiment", "Original Text"])
	tweet_data_frame["Clean Tweet"] = clean_tweet_list
	tweet_data_frame.to_csv("../data/tweet_data_frame.csv",
	                        header=["Time", "Sentiment", "Original Text", "Clean Tweet"])
