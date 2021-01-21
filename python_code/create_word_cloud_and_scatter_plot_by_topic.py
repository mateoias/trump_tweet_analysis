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

# return a flat list for the nested list of tweets
def flatten_clean_tweet_list(clean_tweet_list):
	flat_list = []
	for sublist in clean_tweet_list:
		for item in sublist:
			flat_list.append(item)
	return flat_list
	# a function to create a word cloud of all of Trump's tweets that contain the topic words searched for by the user
def create_word_cloud(clean_tweet_list):
	flat_list = flatten_clean_tweet_list(clean_tweet_list)
	text = " ".join(flat_list)
	word_cloud = WordCloud(width=800, height=800,
				   background_color='white',
				   min_font_size=10)
	word_cloud_image = word_cloud.generate_from_text(text)
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
	
	# return the top 10 words from the topic cluster selected by the user
def get_user_search_topic():
	while True:
		print("You may either choose a predefined topic or input your own search term. \n")
		user_search_topic = input("Choose a topic between 1 and 28 or input your search term now: ")
		return(user_search_topic)
		# if not user_search_topic.isdigit():
		# 	return(user_search_topic)
		# if 0<int(user_search_topic)<29:
		# 	#insert topic functionality here
		# 	break 
		# else:
		# 	print("Please enter an integer between 1 and 28 or a search word.")
		# 	continue		
	
def get_words_for_topic(user_search_topic):	
	topic_words_df = load_topic_data()
	topic_number = 2 * (int(user_search_topic)-1)
	user_search_words = topic_words_df.iloc[1:11, topic_number]
	search_word_weights = topic_words_df.iloc[1:11, topic_number+1]
	print(f"The words you are searching for are: \n {user_search_words}. Their relative weighting in the topic is: \n {search_word_weights}")
	return user_search_words.values.tolist()

# a function to load the topic clusters from the CSV 
def load_topic_data():
	topic_word_list = []
	with open("../data/topic_groups.csv", "r") as f:
		csvReader = csv.reader(f)
		for row in csvReader:
			data = row
			topic_word_list.append(data)
	topic_words_df = pd.DataFrame(topic_word_list)
	return topic_words_df

# a function to get all of the tweet data
def load_tweets():
	with open("../data/tweet_data_frame.csv", "r") as f:
		clean_tweet_list = []
		csvReader = csv.reader(f)
		for row in csvReader:
			data = row
			clean_tweet_list.append(data[4])
	return clean_tweet_list	
# A function to get all tweets with the users search terms
def find_relevant_tweets(user_topic_words, clean_tweet_list):
	relevant_tweet_list = set()
	for tweet in clean_tweet_list:
		for word in tweet.split(" "):
			if word in user_topic_words:
				relevant_tweet_list.add(tweet)
				break
	return relevant_tweet_list


def clean_text(relevant_tweet_list):
	clean_tweet_list = []
	for tweet in relevant_tweet_list:
		tokens = tweet.split()
		tokens = [word.lower() for word in tokens]
		content_words = [w for w in tokens if not w in stop_words]
		text_alphabetic = ["".join(c for c in word if c.isalpha())
                     for word in content_words]
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

# def clean_text(relevant_tweet_list):
# 	for text in relevant_tweet_list:
# 		tokens = text.split()
# 		tokens = [word.lower() for word in tokens]
# 		content_words = [w for w in tokens if not w in stop_words]
# 		text = ["".join(c for c in word if c.isalpha()) for word in content_words]
# 		text = text.replace('&amp', '')
# 		text = text.replace('realdonaldtrump', '')
# 		text = text.replace("thank", "thanks")
# 		text = text.replace('U.S.', 'usa')
# 		text = text.replace('RT', '')
# 		text = text.replace('dems', 'democrats')
# 		clean_tweet_list.append(text)
# 	return clean_tweet_list

if __name__ == "__main__":
	user_search_words = get_user_search_topic()
	print("search words", user_search_words)
	clean_tweet_list = load_tweets()
	user_topic_words = get_words_for_topic(user_search_words)
	print(user_topic_words)
	relevant_tweet_list = find_relevant_tweets(user_topic_words, clean_tweet_list)
	clean_tweet_list = clean_text(relevant_tweet_list)
	print(f"there are {len(relevant_tweet_list)} tweets containing the search term(s) {user_topic_words}")
	create_word_cloud(clean_tweet_list)
	# create_scatter_plot(user_search_words, relevant_tweet_list)


# add the original text to the hover?
