import pandas as pd
from textblob import TextBlob
import json

#Calculate percentage
def percentage(part, whole):
    return 100 * float(part)/float(whole)

def get_Sentiments():
	df = pd.read_excel(r"C:\Users\mibrahim\Desktop\Prediction.xlsx")
	tweet_contents = df['Tweet content']

	#Sentiment Analysis
	positive = 0
	negative = 0
	nuetral = 0
	polarity = 0

	for tweet in tweet_contents:
	    #print(tweet)
	    #print(tweet.user.location)
	    analysis = TextBlob(tweet)
	    #print(analysis.sentiment)
	    polarity+= analysis.sentiment.polarity

	if (analysis.sentiment.polarity == 0.00):
		nuetral+=1

	elif (analysis.sentiment.polarity > 0.00):
		positive+=1

	elif (analysis.sentiment.polarity < 0.00):
		negative+=1
	noOfItems = 204820

	positive = percentage(positive,noOfItems)
	negative = percentage(negative,noOfItems)
	nuetral = percentage(nuetral,noOfItems)
	polarity =percentage(polarity,noOfItems)

	data = {}

	if (polarity == 0):
		data['type'] = 'Neutral'
		data['value'] = nuetral
	elif (polarity < 0):
		data['type'] = 'Negative'
		data['value'] = negative
	elif(polarity > 0):
		data['type'] = 'positive'
		data['value'] = positive

	json_data = json.dumps(data)
	print(json_data)
	return json_data


if __name__== "__main__":
   get_Sentiments()