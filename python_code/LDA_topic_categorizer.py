from sklearn.decomposition import LatentDirichletAllocation
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import pickle
import plotly.express as px
import csv
import pandas as pd

def load_data():
	clean_tweet_list = []
	# import the csv file and extract the text entries as strings
	with open('../data/clean_tweet_list.csv', 'r') as f:
		csvReader = csv.reader(f)
		clean_tweet_list = []
		for row in csvReader:
			data = row
			listToStr = ' '.join(map(str, data))
			clean_tweet_list.append(listToStr)
	return clean_tweet_list

def vectorize_tweet_data():
# get the tweet data
	tweet_data = load_data()
	# transform text (string) to vector form
	vectorizer = CountVectorizer(max_df = 0.1, min_df=3)
	# apply transformation
	tf = vectorizer.fit_transform(tweet_data)
	# tf_feature_names tells us what word each column in the matric represents
	feature_names = vectorizer.get_feature_names()
	return tf, feature_names

def LDA_topic_cluster_model():
	tf, feature_names = vectorize_tweet_data()
	num_topic_clusters = 10
	num_words = 10
	model = LatentDirichletAllocation(n_components=num_topic_clusters, random_state=0)
	model.fit(tf)
	topic_dict = {}
	for topic_idx, topic in enumerate(model.components_):
		topic_dict["Topic %d words" % (topic_idx)] = ['{}'.format(feature_names[i])
                                                for i in topic.argsort()[:-num_words - 1:-1]]
		topic_dict["Topic %d weights" % (topic_idx)] = ['{:.1f}'.format(topic[i])
                                                  for i in topic.argsort()[:-num_words - 1:-1]]
	return pd.DataFrame(topic_dict)

def display_LDA_results():
	topics = LDA_topic_cluster_model()
	pd.set_option("display.max_rows", None, "display.max_columns", None)
	print("LDA results:\n")
	print(topics)

display_LDA_results()
