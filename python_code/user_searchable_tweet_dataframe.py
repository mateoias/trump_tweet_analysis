import plotly.express as px
import seaborn as sns
import re
import csv
import string
import sys
import matplotlib.pyplot as plt
import pandas as pd

# this program allows the user to search the database and create a scatterplot for a search term

# function to get user's search term
def get_user_input():
    print("this program allows you to search Trump's tweets and create a scatterplot for a search term")
    print("enter 'quit' to exit the program")
    search_term = input("Please enter a search term to get all tweets containing that word:\n")
    if search_term == "quit":
        sys.exit()
    search_term = search_term.lower()
    return (search_term)
# function import all tweets that contain the search term from the csv file
def import_data_from_database(search_term):
    search_term = search_term
    with open('../data/condensed_dow_and_sentiment.csv', 'r') as f:
        csvReader = csv.DictReader(f)
        dow_tweet_list = []
        tweets_with_user_text = []
        for row in csvReader:
            data = row["Time"], row["Vader_compound"],row["Volatility"], row["Open"],row["Close"],row["Tweet_text"], row["Volume"]
            dow_tweet_list.append(data)
        for tweet in dow_tweet_list:
            time = tweet[0]
            sentiment = tweet[1]
            dow_volatility = tweet[2]
            dow_open = tweet[3]
            dow_close = tweet[4]
            text = tweet[5]
            dow_volume = tweet[6]
            text = re.sub(r'https.*', ' ', text)
            lower_text = text.lower()            
            content_word_tweets = time, sentiment, dow_volatility, dow_open, dow_close, text, dow_volume	
            if search_term in lower_text:
                tweets_with_user_text.append(content_word_tweets)
        return tweets_with_user_text

   # function to check if user input has any results   


def check_user_input(tweets_with_user_text, search_term):
    if (len(tweets_with_user_text))>0:
        print(f"The database holds {len(tweets_with_user_text)} tweets with the search term {search_term}")
        df = pd.DataFrame(tweets_with_user_text, columns=[
                              "Time", "Vader_compound", "Volatility", "Open", "Close", "Text", "Volume"])           
        return(df)
    else:
        print(f"{user_text} does not appear in the database. Please enter a new term")
        get_user_input()

# function to create a scatter plot of all the tweets that contain the user's search term
def get_x_y_axes():
    x_axis = input("You can plot the data for dates, Dow Jones information and tweet sentiment. \n"
                   "The Dow Jones Data is on for 2016 - 08/23/202. \n"
                   "Please choose 'Time', 'Vader_compound' (sentiment), 'Volatility', 'Open', 'Close', 'Volume' (from the dow jones)\n"
                   "Please enter a value for the x axis:\n")
    y_axis = input("Please enter a value for the y axis: \n")
    if x_axis and y_axis in ["Time", "Volatility", "Open", "Close", "Volume", "Vader_compound"]:
        return(x_axis, y_axis)
    else: 
        get_x_y_axes()
    return x_axis, y_axis

def create_scatter_plot(df, search_term):
    x_axis, y_axis = get_x_y_axes()
# figure comparing two input variables from user
    fig = px.scatter(df, x=x_axis, y= y_axis, hover_data = ["Time", "Text"])
#https://plotly.com/python/hover-text-and-formatting/#customizing-hover-text-with-plotly-express
    fig.update_layout(
        title={
            'text': "Results for: " + search_term,
            'y': 0.99,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.show()
   
# if name ==__main_:
def main():
    search_term = get_user_input()
    tweets_with_user_text = import_data_from_database(search_term)
    df = check_user_input(tweets_with_user_text, search_term)
    create_scatter_plot(df, search_term)
    main()


if __name__ == ('__main__'):
    main()