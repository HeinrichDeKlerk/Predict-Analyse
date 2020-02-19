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
    #####################################
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