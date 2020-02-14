def date_parser(dates):

    """
    This funcyion returns a list of strings from an input of strings
    and formats as ''yyyy-mm-dd

    """

    i=0
    while i < len(dates):
        dates[i] = dates[i][:10]
        i+=1
    
    return dates
