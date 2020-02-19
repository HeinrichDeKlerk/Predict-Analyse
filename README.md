A Python package with functions that are useful in extracting insightful information from Eskom data. 

dictionary_of_metrics : Calculate mean, median, maximum, minimum, variance and standard deviation with a ddof=1 (degrees of freedom).
    	   	              Args:  items(list) of ints or floats
   	  	                Returns:  Dictionary of operations performed

five_num_summary : Calculate the five number summary on a list of items, Five number summary includes maximum, minimum, median, 25th                        percentile and 75th percentile.
    	             Args: items (list) of ints or floats.
    	             Returns: Dictionary of calculated operations.

date_parser : This function takes as input a list of datetime in a form "yyyy-mm-dd hr-min-sec" strings and returns only the date in                   'yyyy-mm-dd' format.

extract_municipality_hashtags : Add 2 new columns to pandas dataframe containing information about the municipality and hashtag of the                                   tweet.
	  		                        Args: df (pandas dataframe)
	 		                          Returns:Modified pandas dataframe containing 2 new columns 'municipality' and 'hashtags', entry of                                       np.nan where no hashtags were detected.

number_of_tweets_per_day : Create new dataframe with index of Date(datetime object) and column of 'Tweets' with number of tweets per                                day.    
    	   		               Args: df (pandas dataframe).
    	 	  	               Returns: a new dataframe, grouped by day, with the number of tweets for that day.

word_splitter : Modifies dataframe directly to tokenize sentences in tweets. ie, split sentences in tweets into seperate words. Splits                   sentences and adds result to new column in dataframe.
    	          Args: df (pandas dataframe)
        	      Returns: Modiefied dataframe with added column 'Split Tweets'

stop_words_remover : Modify pandas dataframe to remove stop words defined in dictionary.    
    	      	       Args: df (pandas dataframe)
        	           Returns: Modified dataframe with new column 'Without Stop Words', that do not contain the stop words defined in the                               dictionary provided.
