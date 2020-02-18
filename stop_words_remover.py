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
