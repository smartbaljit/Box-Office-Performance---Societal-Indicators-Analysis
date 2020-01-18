# Create function to hold news API call
# function will take in 'q' to query
# return json and input in pandas dataframe
# clean columns and add sentiment analysis

# import dependencies
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from x_api import x_api_key

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

# Query contextual web search API
# Replace the following string value with your valid X-RapidAPI-Key.
Your_X_RapidAPI_Key = x_api_key;



# Define function to do sentiment analysis of news data
def sentiment_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score


# The query parameters: (update according to your search query)
q = "" #the search query
pageNumber = 1 #the number of requested page
pageSize = 50 #the size of a page
autoCorrect = True #autoCorrectspelling
safeSearch = False #filter results for adult content


def news_pull(q):
    # test response to query and get count of total items and pages
    response_test=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI?q={}&pageNumber={}&pageSize={}&autocorrect={}&safeSearch={}".format(q, pageNumber, pageSize, autoCorrect,safeSearch),
                               headers={"X-RapidAPI-Key": Your_X_RapidAPI_Key}).json()

    #Get the number of items returned
    totalCount = response_test["totalCount"];
    totalPages = round(totalCount/pageSize)
    print('Please wait...searching')
    print(f' There are {totalPages} pages, with {totalCount} total articles.')
    

    # create empty lists to hold variable results
    url_list = []
    title_list = []
    description_list = []
    keywords_list = []
    provider_list = []
    date_list = []

    # Begin for loop of json 
    for page in range(1,totalPages+1):
        response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI?q={}&pageNumber={}&pageSize={}&autocorrect={}&safeSearch={}".format(q, page, pageSize, autoCorrect,safeSearch),
    headers={"X-RapidAPI-Key": Your_X_RapidAPI_Key}).json()

        # query each row in result
        try:
            #Go over each resulting item
            for webPage in response["value"]:

            #Get the web page metadata
                url = webPage["url"]
                title = webPage["title"]
                description = webPage["description"]
                keywords = webPage["keywords"]
                provider = webPage["provider"]["name"]
                datePublished = webPage["datePublished"]


                url_list.append(url)
                title_list.append(title)
                description_list.append(description)
                keywords_list.append(keywords)
                provider_list.append(provider)
                date_list.append(datePublished)

        except (KeyError,IndexError):
                print('Not found, skipping')
                
    # assign list to dataframe
    newsFrame = pd.DataFrame({'datePublished':date_list,'description':description_list,'keywords':keywords_list,'provider':provider_list,'title':title_list,'url':url_list})

    # clean description and title columns
    newsFrame.description = newsFrame.description.str.replace('<b>','')
    newsFrame.description = newsFrame.description.str.replace('</b>','')
    newsFrame.title = newsFrame.title.str.replace('<b>','')
    newsFrame.title = newsFrame.title.str.replace('</b>','')

    # add column in newsFrame for sentiment score
    newsFrame['sentiment_score'] = ''
    newsFrame['sentiment'] = ''
        
        # add in sentiment analysis to data frame

    for i, row in newsFrame.iterrows():
        sentiment_score = float(sentiment_scores(row[1])['compound']) # take sentiment of description of each article
        if(sentiment_score >= 0.05):
            row['sentiment'] = 'positive'
        elif(sentiment_score <= 0.05):
            row['sentiment'] = 'negative'
        else:
            row['sentiment'] = 'neutral'
        row['sentiment_score'] = sentiment_score

    newsFrame.datePublished = pd.to_datetime(newsFrame.datePublished)
    newsFrame.datePublished = newsFrame.datePublished.dt.strftime('%m/%d/%Y') 
    
    # check dataframe to see if sentiment score was added in
    print(newsFrame.head())
    
    return newsFrame