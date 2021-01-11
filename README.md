# Trump Tweet Analysis
This is part of a project to analyse Trump's tweets and their effects on the stock market. My role was to do text cleaning, exploration and analysis

### Tools/Packages Used:
* sklearn.decomposition, sklearn.feature_extraction, sklearn.cluster
* nltk.stem, nltk.corpus, nltk.tokenize
* vaderSentiment
* wordcloud
* textblob
* pandas
* time
* matplotlib
* scipy.stats
* plotly

#### Datasets
This project is based on two main datasets spanning the time from Jan1 2016 - August 10 2020: One is a complete set of Trump's tweets taken from the trump twitter archive (http://www.trumptwitterarchive.com/archive) The other is the  Dow Jones Industrial Average daily information for that same time period.
I created a dataframe matching the tweets and Dow Jones information over time and cleaned the tweets for sentiment analysis.
#### Sentiment analysis
I ran a variety of sentiment analysis algorithms, including textblob, Naive Bayes and Vader. Vader was the most effective so I created a new dataset including Vader sentiment scores. Then I built an exploratory interface where I could graph different aspects of the data and look for patterns. For example, graphing the Dow daily volatility over time against Tweet sentiment for some search term(s). In general the sentiment vs Dow results were non linear and it was hard to find a clear pattern in them.
#### Topic categorization
Next I did topic categorization of the tweets, looking to find a connection between the words Trump used that would produce a clearer result. The topic categorization required much more data cleaning (see trump_data_cleaning.py). In this step I also calculated term frequency and created a dictionary of vocabulary used. For the topic categorization I used LDA and NMF to create clusters of words looking for underlying patterns of terms that would help in analyzing the texts. See NMF_topic_categorizer.py for results.
#### Topic categorization with BERT
In order to retain semantic information when doing topic categorization the best choice seems to be to combine LDA and BERT using BERT as service. This will be the next stage of the project.
