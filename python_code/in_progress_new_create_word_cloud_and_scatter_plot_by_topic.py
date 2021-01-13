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


# def flatten_user_text(words_to_display):
# 	print (f"flatten{words_to_display}")
# 	return [item for sublist in words_to_display for item in sublist]  
	# a function to create a word cloud of Trump's tweets that contain the topic words searched for by the user
def create_word_cloud(words_to_display):
	word_cloud = WordCloud(width=800, height=800,
				   background_color='white',
				   min_font_size=10)
	word_cloud_image = word_cloud.generate_from_text(' '.join(words_to_display))
	plt.figure(figsize=(8, 8), facecolor=None)
	plt.imshow(word_cloud_image)
	plt.axis("off")
	plt.tight_layout(pad=0)
	plt.show()

def create_scatter_plot(user_search_words, tweet_data_frame):
	search_terms = ' '.join(map(str, user_search_words))
	# fig = px.scatter(tweet_data_frame, x=1, y=2,
    #               hover_data=[3, 2])
	# fig.update_layout(
    #         title={
    #             'text': "Results for: " + search_terms,
    #             'y': 0.99,
    #        					'x': 0.5,
    #        					'xanchor': 'center',
    #        					'yanchor': 'top'})
	# fig.show()
	
	# return the top five words from the topic cluster selected by the user
def get_user_search_words():
	while True:
		user_search_topic = input("You may choose either a predefined topic or to input your own terms. Choose a topic between 1 and 28 or input your search term now: ")
		if not user_search_topic.isdigit():
			print(user_search_topic)
			return(user_search_topic)
		if 0<int(user_search_topic)<29:
			break 
		else:
			print("Please enter an integer between 1 and 28 or a search word.")
			continue		
	topic_words_df = load_topic_words()
	topic_number = 2 * (int(user_search_topic)-1)
	user_search_words = topic_words_df.iloc[1:6, topic_number]
	search_word_weights = topic_words_df.iloc[1:6, topic_number+1]
	print(f"The words you are searching for are {user_search_words}. Their relative weighting in the topic is {search_word_weights}")
	return user_search_words.values.tolist()

# a function to load the topic clusters from the CSV and return a dataframe of the top 10 words for each cluster
def load_topic_words():
	topic_word_list = []
	with open("../data/topic_groups.csv", "r") as f:
		csvReader = csv.reader(f)
		for row in csvReader:
			data = row
			topic_word_list.append(data)
	data_df = pd.DataFrame(topic_word_list)
	return data_df

# a function to get the tweet data
def load_tweets():
	with open("../data/tweet_data_frame.csv", "r") as f:
		clean_tweet_list = []
		csvReader = csv.reader(f)
		for row in csvReader:
			data = row
			clean_tweet_list.append(data[4])
			print(clean_tweet_list[0:10])
	# tweet_list_df = pd.DataFrame(tweet_list)
	return clean_tweet_list	
# A function to get all tweets with the users search terms
def find_relevant_tweets(user_search_words, tweet_list):
	relevant_tweet_list = []
	# relevant_tweet_sentiment = []
	# relevant_tweet_time = []
	#df 4 is the cleaned tweets with only content words
	# tweet_list = tweet_list_df[4].values
	# .tolist()
	print(tweet_list[0:20])
	for tweet in tweet_list:
		for word in tweet.split(" "):
			if word in user_search_words and tweet not in relevant_tweet_list:
				relevant_tweet_list.append(tweet)
			# print(relevant_tweet_list)
	return relevant_tweet_list

if __name__ == "__main__":
	user_search_words = get_user_search_words()
	print(user_search_words)
	tweet_list = load_tweets()
	print(f"tweet_list is {tweet_list[0:10]}")
	tweets_to_display = find_relevant_tweets(user_search_words, tweet_list)
	print(tweets_to_display)
	# print(f"there are {len(tweets_to_display)} tweets containing the search term(s) {user_search_words}")
	# create_word_cloud(tweets_to_display)
	# create_scatter_plot(user_search_words, tweets_to_display)


# add the original text to the hover?
