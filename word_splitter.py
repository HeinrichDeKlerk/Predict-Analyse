### START FUNCTION
def word_splitter(df):
    # your code here
    spl_twt = {}
    i = 0
    while i < len(df['Tweets']):
        spl_twt[i] = df['Tweets'][i].lower().split()
        i+=1
    df['Split Tweets'] = pd.Series(spl_twt)
    return df

### END FUNCTION