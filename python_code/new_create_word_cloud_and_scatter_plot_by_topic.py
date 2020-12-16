import plotly.express as px
import seaborn as sns
import re
import csv
import matplotlib.pyplot as plt
import pandas as pd
import nltk
# nltk.download('stopwords')
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


def flatten_user_text(user_search_words):
	print (f"flatten{user_search_words}")
	return [item for sublist in user_search_words for item in sublist]  
	# a function to create a word cloud of Trump's tweets that contain the topic words searched for by the user
def create_word_cloud(user_search_words):
	print (f"creatre {user_search_words}")
	word_cloud_text = flatten_user_text(user_search_words)
	print(word_cloud_text)
	print(' '.join(word_cloud_text))
	# word_cloud = WordCloud(width=800, height=800,
	# 			   background_color='white',
	# 			   min_font_size=10)
	# word_cloud_image = word_cloud.generate_from_text(' '.join(word_cloud_text))
	# plt.figure(figsize=(8, 8), facecolor=None)
	# plt.imshow(word_cloud_image)
	# plt.axis("off")
	# plt.tight_layout(pad=0)
	# plt.show()


def create_scatter_plot(user_search_words, tweet_data_frame):
	search_terms = ' '.join(map(str, user_search_words))
	tweet_data_frame = tweet_data_frame
	fig = px.scatter(tweet_data_frame, x="Time", y="Sentiment",
                  hover_data=["Text", "Sentiment"])
	fig.update_layout(
            title={
                'text': "Results for: " + search_terms,
                'y': 0.99,
           					'x': 0.5,
           					'xanchor': 'center',
           					'yanchor': 'top'})
	fig.show()

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
# import the csv file and extract the text entries if the tweet has moe than 5 words
	# search_term_list = get_user_search_words()
	# print(search_term_list)
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
			# tweets_and_sentiment_df = pd.DataFrame(tweet_list, columns=["Time", "Sentiment", "Text"])
			# # create_word_cloud(user_text)
			# return tweets_and_sentiment_df  # search_term_list

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
	# content_word_tweets = time, sentiment, dow_volatility, dow_open, dow_close, listToStr, dow_volume
			#searching for user input term (lower case)
			# for word in search_term_list:
			# 		if word in tokens:
			# 			clean_tweet_list.append(content_word_tweets)
			# 			original_tweet_list.append(tweet)
			# 	user_text = clean_tweet_list
	

def find_relevant_tweets(user_search_words, tweet_list):
	relevant_tweet_list = []

	for tweet in tweet_list:
		# print("tweet found")
		tweet_text = tweet[2]
		print(tweet_text)
		for word in tweet_text:
			print(user_search_words)
			if word in user_search_words:
				print("word found")
				relevant_tweet_list.append(tweet_text)
	print("relevant tweet found")
	print(user_search_words)
	return relevant_tweet_list



if __name__ == "__main__":
	tweet_list = import_tweets_and_sentiment()
	print(len(tweet_list))
	clean_tweet_list = clean_text(tweet_list)
	tweet_data_frame = pd.DataFrame(tweet_list, columns=["Time", "Sentiment", "Text"])
	print (len(clean_tweet_list))
	user_search_words = get_user_search_words()
	print(user_search_words)
	tweets_to_display = find_relevant_tweets(user_search_words, tweet_list)
	print(tweets_to_display)
	# create_word_cloud(user_search_words)
	# create_scatter_plot(user_search_words, tweet_data_frame)


# add the original text to the hover?
