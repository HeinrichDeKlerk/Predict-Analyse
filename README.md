# predictModuleT27  
A Python package with functions that are useful in extracting insightful information from data and dataframes, particularly pertaining to Eskom. 

## Installing this package locally  
'python setyp.py sdist'

## Installing this package from GitHub  
pip install git+https://github.com/HeinrichDeKlerk/predictModuleT27.git

## Updating this file from GitHub  
pip install --upgrade git+https://github.com/HeinrichDeKlerk/predictModuleT27.git

## following is a list of the functions in this module with a brief overview. Click on the link to view function and comprehensive docstring.


[dictionary_of_metrics](functions/dictionary_of_metrics.py) :   Calculate mean, median, maximum, minimum, variance and standard deviation with a ddof=1 (degrees of freedom).
    	   	             

[five_num_summary](functions/five_num_summary.py) :   Calculate the five number summary on a list of items, Five number summary includes maximum, minimum, median, 25th                        percentile and 75th percentile.
    	             

[date_parser](functions/date_parser.py) :   This function takes as input a list of datetime in a form "yyyy-mm-dd hr-min-sec" strings and returns only the date in                   'yyyy-mm-dd' format.

[extract_municipality_hashtags](functions/extract_municipality_hashtags.py) :   Add 2 new columns to pandas dataframe containing information about the municipality and hashtag of the                                   tweet.
	  		                        

[number_of_tweets_per_day](functions/number_of_tweets_per_day.py) :   Create new dataframe with index of Date(datetime object) and column of 'Tweets' with number of tweets per                                day.    
    	   		               

[word_splitter](functions/word_splitter.py) :   Modifies dataframe directly to tokenize sentences in tweets. ie, split sentences in tweets into seperate words. Splits                   sentences and adds result to new column in dataframe.
    	          

[stop_words_remover](functions/stop_words_remover.py) :   Modify pandas dataframe to remove stop words defined in dictionary.    
    	      	       
