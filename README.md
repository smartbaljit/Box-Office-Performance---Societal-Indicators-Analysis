Final Project - Analyzing the impact of societal indicators on Movie Box office
=======

Group Members: Jess, Baljit, Rick, Tanvir

## Abstract

The goal was to gather a variety of indicators which could give insight into the "feeling" or "mood" of a society.    
Things like unemployment rate, median income, presidential approval ratings and news headlines. Then all these indicators  
could be tested against film Box Office in order to determine how they effect movie going habits.  

## Data Sources

* [OMDB - API](http://www.omdbapi.com/)
* [IMDB - csv](https://www.imdb.com/search/title/)
* [Box Office Mojo - csv](https://github.com/zacharyang/movies-project/tree/master/data/clean)
* [Netflix Stock Price - csv](https://finance.yahoo.com/quote/NFLX/)
* [Consumer Price Index](https://data.oecd.org/unemp/harmonised-unemployment-rate-hur.htm)
* [Median Income](https://fred.stlouisfed.org/series/MEHOINUSA672N)
* [Presidential Approval ratings - csv](https://www.presidency.ucsb.edu/statistics/data/presidential-job-approval)


## ETL

Pandas was used for cleaning of data sets. All data was eventually organized by year and then combined  
into a large table.

## Analysis

**Vader Sentiment Analysis Library** - Using the NY Times API, all news headlines/descriptions were pulled from 1995-2015  
These were then analyzed for sentiment in order to gauge average sentiment on an year by year basis 

**Machine Learning Scikit Learn**

Why Linear Regression?    
We decided to use Linear Regression because our dependent variable (Box Office Revenue)    
is a continuous field. It is not a yes/no field or limited to a set of categories. For continuous     
fields like this, Linear Regression is a good model for prediction.  

Our initial feature set was a large set of variables tied to year and/or month of movie release.      
This included economic conditions such as GDP change, unemployment, consumer confidence, and median     
income; political polling, with approval/disapproval of President; binary encoded genre     
features (e.g, a romantic comedy would be a "1" under "romance" and "comedy" and a "0" under other genres);     
and the current market price of the S&P 500 index and Netflix stock. The full model of everything showed     
a good match between train and test data but only a minor correlation, with R^2 scores in the 0.20 to 0.25 range.      
We split features into new train/test models, with only economic data or only political data, etc.  This revealed     
that the only feature model showing even a slight correlation was genre.  Others had correlations of practically zero.      
The correlation of genre was almost identical to entire feature set.  Even with an excess of features,     
Linear Regression was able to separate even a small signal from noise.    

## Visualizations

HTML/CSS with interactive embedded Tableau Dashboards  
Website Template from https://colorlib.com/wp/templates/




