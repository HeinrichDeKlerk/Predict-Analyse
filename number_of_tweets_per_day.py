def number_of_tweets_per_day(df):
    """
    This function takes in a pandas dataframe as input argument.
    It then returns a new dataframe, grouped by day, with the number of tweets for that day.
    New dataframe has index of Date(datetime object) and column of 'Tweets"
    """
    i=0
    while i < len(df):
        df['Date'][i] = df['Date'][i][:11]
        i+=1
    df['Date'] = pd.to_datetime(df['Date'])
    a = pd.DataFrame(df.groupby('Date').count().loc[:,'Tweets'])
    return a
