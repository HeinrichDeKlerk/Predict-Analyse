def number_of_tweets_per_day(df):
    """
    Create new dataframe with index of Date(datetime object) and column of 'Tweets' with number of tweets per day
    
    Args:
        df (pandas dataframe)
    Returns:
        a new dataframe, grouped by day, with the number of tweets for that day.
    """
    i=0
    while i < len(df):
        df['Date'][i] = df['Date'][i][:11]
        i+=1
    df['Date'] = pd.to_datetime(df['Date'])
    a = pd.DataFrame(df.groupby('Date').count().loc[:,'Tweets'])
    return a
