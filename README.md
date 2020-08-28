# Trump Tweet Analysis
This is part of a project to analyse Trump's tweets and their effects on the stock market. My role was to do text cleaning, exploration and analyasis

### Tools/Packages Used:
* sklearn
* nltk
* vaderSentiment
* wordcloud
* textblob
* pandas
* time
* matplotlib
* scipy.stats
* plotly

#### Datasets
This project is based on two main datasets spanning the time from Jan1 2016 - Austg 10 2020: One is a complete set of trujo tweets taken from the trump twitter archive (http://www.trumptwitterarchive.com/archive) The other is the  Dow Jones Industrial Average daily information taken from ()
I created a dataframe matching the tweets and Dow Jones information over time and cleaned the tweets for sentiment analysis.
#### Sentiment analysis
I ran a variety of sentiment analysis algorythms, including tweetbob,  Naive Bayes and Vader. Taking Vader as a the most effective I built a explratory interface where I could graph search terms over a space based on aspects of the data. For example. Dow daily volatilty against time or Tweet sentiment against Dow. This program is searchable_sentiment_dji_dataframe.py. In general the results were non linear and it was hard to find a clear pattern.
#### Topic categorization
Next I did topic categorization of the tweets, looking to find a connection between the terms that would produce a clearer result. The topic categorization required much more data cleaning (see trump_data_cleaning.py). In this step I also calyculated term frequency and created a dictionary of vocaulary used. For the topic categorization I used LDA and NMF to create clusters of words looking for underlying patterns of terms that would help in anlyzing the texts. See topic_categorizor_nmf.py for results.

