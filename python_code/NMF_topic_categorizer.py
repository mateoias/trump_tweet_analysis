from sklearn.decomposition import LatentDirichletAllocation
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import pickle
import plotly.express as px
import csv
import json
import pandas as pd

def load_data():
	clean_tweet_list = []
	# import the csv file and extract the text entries as strings
	with open('../data/tweet_data_frame.csv', 'r') as f:
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



# function to show an NMF model with results for diferent numbers of topic clusters
# num_topic_clusters is the number of topics, 
def create_topic_dictionary(model, feature_names, num_words):
	topic_dict = {}
	for topic_idx, topic in enumerate(model.components_):
		topic_dict["Topic %d words" % (topic_idx)] = ['{}'.format(feature_names[i])
											   for i in topic.argsort()[:-num_words - 1:-1]]
		topic_dict["Topic %d weights" % (topic_idx)] = ['{:.1f}'.format(topic[i])
												 for i in topic.argsort()[:-num_words - 1:-1]]
	return pd.DataFrame(topic_dict)
def NMF_topic_cluster_model():
	#num_words = number of words printed for each topic cluster
	num_words = 10
	tf, feature_names = vectorize_tweet_data()
	for num_topic_clusters in range(29,30):
		model = NMF(n_components=num_topic_clusters, random_state=0,
					max_iter=750, alpha=.1, l1_ratio=.5)
		tf, feature_names = vectorize_tweet_data()
		model.fit(tf)
		nmf_topics = create_topic_dictionary(model, feature_names, num_words)
		pd.set_option("display.max_rows", None, "display.max_columns", None)
		print(f"NMF results: for {num_topic_clusters} topics.")
		print(nmf_topics)
		print(type(nmf_topics))

	# create a csv and a JSON of the largest set of topic clusters
	nmf_topics.to_csv(r'../data/topic_groups.csv', index=False)
	transposed_nmf_topics = nmf_topics.T
	transposed_nmf_topics.to_csv(r'../data/transposed_topic_groups.csv', index=False)

	# with open('nmf_topics.txt', 'w') as outfile:
	# 	json.dump(nmf_topics, outfile)
NMF_topic_cluster_model()
