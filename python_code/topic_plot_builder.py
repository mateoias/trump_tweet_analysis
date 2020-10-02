import csv
import pandas as pd


def load_topic_data(i):
	topic_word_list = []
	# import the csv file and extract the text entries
	with open("../data/topic_groups.csv", "r") as f:
		csvReader = csv.reader(f)
		for row in csvReader:
			data = row
			topic_word_list.append(data)
	data_df = pd.DataFrame(topic_word_list)
	search_words = data_df.iloc[1:11, i]
	print(search_words)
	return search_words.values.tolist()

data = load_topic_data(2)
print(data)