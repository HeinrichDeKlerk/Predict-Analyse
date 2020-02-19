def dictionary_of_metrics(items):
    """
    Calculate mean, median, maximum, minimum, variance and standard deviation
    with a ddof=1.
    Args:
        items(list) of ints or floats
    Returns:
        Dictionary of operations performed
    """

        q=np.mean(items)
        w=np.median(items)
        e=np.var(items, ddof=1)
        r=np.std(items,ddof=1)
        t=np.min(items)
        y=np.max(items)
        return dict(mean=round(q,2),median=round(w,2),var=round(e,2),std=round(r,2),min=round(t,2),max=round(y,2))


def five_num_summary(items):
    """
    Calculate the five number summary on a list of items
    Five number summary includes maximum, minimum, median,
    25th percentile and 75th percentile
    Args:
        items (list) of ints or floats

    Returns:
        Dictionary of calculated operations
    """

    for num in items:
        s_list = sorted(items)
        n_max = np.max(s_list)
        n_med = np.median(s_list)
        n_q1 = np.percentile(s_list, 25)
        n_min = np.min(s_list)
        n_q3 = np.percentile(s_list, 75)

        D = { "max":n_max, "median":n_med, "min":n_min, "q1":n_q1, "q3":n_q3}
    return D


def date_parser(dates):
    """
    This function takes as input a list of datetime
    in a form "yyyy-mm-dd hr-min-sec" strings and
    returns only the date in 'yyyy-mm-dd' format.
    """
    new_dates = []
    for date in dates:
        my_dates = date.split()
        new_dates.append(my_dates[0])
    return new_dates


def extract_municipality_hashtags(df):
    """
	Add 2 new columns to pandas dataframe containing information about
	the municipality and hashtag of the tweet.
	Args:
		df (pandas dataframe)
	Returns:
		Modified pandas dataframe containing 2 new columns 'municipality'
		and 'hashtags', entry of np.nan where no hashtags were detected.
	"""
    spl_twt = {}
    i = 0
    while i < len(df['Tweets']):
        spl_twt[i] = df['Tweets'][i].lower().split()
        i+=1
    df['Split Tweets'] = pd.Series(spl_twt)
    munic = {}
    hashtags = {}
    i = 0
    while i < len(df['Split Tweets']):
        hashtag_list = []
        for word in df['Split Tweets'][i]:
            for mun in mun_dict.keys():
                if word == mun:
                    munic[i] = mun_dict[word]
            if word[0] == '#':
                hashtag_list.append(word)
        if len(hashtag_list)==0:
            hashtags[i] = np.nan
        else:
            hashtags[i] = hashtag_list
        i+=1
    df['municipality'] = pd.Series(munic)
    df['hashtags'] = pd.Series(hashtags)
    df.drop('Split Tweets', axis=1, inplace=True)
    return df

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


def word_splitter(df):
    """
    Modifies dataframe directly to tokenize sentences in tweets. ie, split sentences in tweets into seperate words.
    Splits sentences and adds result to new column in dataframe.

    Args:
        df (pandas dataframe)

    Returns:
        Modiefied dataframe with added column 'Split Tweets'
    """
    spl_twt = {}
    i = 0
    while i < len(df['Tweets']):
        spl_twt[i] = df['Tweets'][i].lower().split()
        i+=1
    df['Split Tweets'] = pd.Series(spl_twt)
    return df

def stop_words_remover(df):
    """
    Modify pandas dataframe to remove stop words defined in dictionary.

    Args:
        df (pandas dataframe)
    Returns:
        Modified dataframe with new column 'Without Stop Words', that do not contain the stop words defined in the dict
        provided
    """
    spl_twt = {}
    i = 0
    while i < len(df['Tweets']):
        spl_twt[i] = df['Tweets'][i].lower().split()
        i+=1
    df['Split Tweets'] = pd.Series(spl_twt)
    new_list = []
    for r in df['Split Tweets']:
        new_new_list = []
        for word in r:
            if word not in stop_words_dict['stopwords']:
                new_new_list.append(word)
        new_list.append(new_new_list)
    df['Without Stop Words'] = pd.Series(new_list)
    df.drop('Split Tweets', axis = 1, inplace = True)
    return df
