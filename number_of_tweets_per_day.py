### START FUNCTION
def number_of_tweets_per_day(df):
    # your code here
    i=0
    while i < len(df):
        df['Date'][i] = df['Date'][i][:11]
        i+=1
    df['Date'] = pd.to_datetime(df['Date'])
    a = pd.DataFrame(df.groupby('Date').count().loc[:,'Tweets'])
    return a

### END FUNCTION