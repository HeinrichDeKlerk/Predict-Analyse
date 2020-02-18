def date_parser(dates):
    """
    Doc strings here
    """
    new_dates = []
    for date in dates:
        my_dates = date.split()
        new_dates.append(my_dates[0])
    return new_dates