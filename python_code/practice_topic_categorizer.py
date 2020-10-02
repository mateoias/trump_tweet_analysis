import pandas as pd from sklearn.feature_extraction.text
import TfidfTransformer from sklearn.feature_extraction.text
import CountVectorizer
docs = ["the house had a tiny little mouse",
        "the cat saw the mouse",
        "the mouse ran away from the house",
        "the cat finally ate the mouse",
        "the end of the mouse story"
        ]
# the vectorizer object will be used to transform text to vector form

vectorizer = CountVectorizer()
# apply transformation
tf = vectorizer.fit_transform(docs)
# tf_feature_names tells us what word each column in the matric represents
tf_feature_names = vectorizer.get_feature_names()
number_of_topics = 10
model = LatentDirichletAllocation(n_components=number_of_topics, random_state=0)
model.fit(tf)
def display_topics(model, feature_names, no_top_words):
	topic_dict = {}
	for topic_idx, topic in enumerate(model.components_):
		topic_dict["Topic %d words" % (topic_idx)] = ['{}'.format(feature_names[i])
													  for i in topic.argsort()[:-no_top_words - 1:-1]]
		topic_dict["Topic %d weights" % (topic_idx)] = ['{:.1f}'.format(topic[i])
														for i in topic.argsort()[:-no_top_words - 1:-1]]
	return pd.DataFrame(topic_dict)

# display LDA results
# no_top_words = 10
# topics = display_topics(model, tf_feature_names, no_top_words)
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print("LDA results:\n")
# print(topics)


# # Do a NMF model
# i is the number of topics, no_top_words = number of words in the topic list
for i in range(9,12,2):
	no_top_words = 8
	model = NMF(n_components=i, random_state=0, max_iter=500, alpha=.1, l1_ratio=.5)
	model.fit(tf)
	nmf_topics = display_topics(model, tf_feature_names, no_top_words)
	pd.set_option("display.max_rows", None, "display.max_columns", None)
	print(f"NMF results: for {i} topics.")
	print(nmf_topics)


 
# # how does kmeans work
# model = KMeans (n_clusters = 10)
# model.fit(tf)
# clusters=model.labels_.tolist()

# if opts.n_components:
#     original_space_centroids = svd.inverse_transform(km.cluster_centers_)
#     order_centroids = original_space_centroids.argsort()[:, ::-1]
# else:
#     order_centroids = km.cluster_centers_.argsort()[:, ::-1]
# terms = vectorizer.get_feature_names()
# for i in range(true_k):
#     print("Cluster %d:" % i, end='')
#     for ind in order_centroids[i, :10]:
#         print(' %s' % terms[ind], end='')
#     print()





# #kmeans clustering optimal group size, the elbow method, optimal is wher the curve starts to flatten out

# # kmeans_topics = display_topics(model, tf_feature_names, no_top_words)
# # pd.set_option("display.max_rows", None, "display.max_columns", None)
# # print("KMEANS results:\n ")
# # print(kmeans_topics)

# #try to add BERT to LDA model
