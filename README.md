# Trump Tweet Analysis
This project began as an analysis of Donald Trump's tweets and their effects on the stock market. I am continuing to parse and organize the tweets to make them accessible and searchable for the user. 

### Tools/Packages Used:
* sklearn.decomposition, sklearn.feature_extraction, sklearn.cluster
* nltk.stem, nltk.corpus, nltk.tokenize
* vaderSentiment
* LatentDirichletAllocation
* NMF
* KMeans
* wordcloud
* textblob
* pandas
* time
* matplotlib
* scipy.stats
* plotly

#### Datasets
This project is based on two datasets. One is the complete set of Trump's tweets taken from the trump twitter archive (http://www.trumptwitterarchive.com/archive) and extending to the point at which he was banned by twitter. The other is the  Dow Jones Industrial Average daily information for the time period in which he was president. I created a dataframe matching the tweets and Dow Jones information over time and looked for significant effects of tweet sentiment on the Dow Jones.  In general the sentiment vs Dow results were non linear and it was hard to find a clear pattern in them.
#### Sentiment analysis
I ran a variety of sentiment analysis algorithms, including textblob, Naive Bayes and Vader. Vader was the most effective so I created a new dataset including Vader sentiment scores. Then I built an exploratory interface where a user can graph different aspects of the data and look for patterns. For example, plotting the tweet sentiment for some set of search terms over time (see user_searchable_tweet_dataframe.py).
#### Topic categorization
Finally, I did topic categorization of the tweets, looking to find a connection between the words Trump used that would help in understanding the data. The topic categorization required much more data cleaning (see build_clean_tweet_dataframe.py). In this step I also calculated term frequency and created a dictionary of vocabulary used (tweet_dictionary_maker.py). For the topic categorization I used LDA and NMF to create clusters of words looking for underlying patterns of terms that would help in analyzing the texts. See NMF_topic_categorizer.py for results. I also wrote a word cloud creating function that allows the user to see what words are most strongly assosciated with each topic (create_word_cloud_by_topic.py).
