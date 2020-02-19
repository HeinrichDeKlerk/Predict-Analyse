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

