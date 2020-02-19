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
