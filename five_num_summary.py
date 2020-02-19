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
    
    a=np.max(items)
    s=np.median(items)
    d=np.min(items)
    f=np.quantile(items, .25)
    g=np.quantile(items, .75)
    
    return dict(max=round(a,2), median=round(s,2),min =round(d,2), q1=round(f,2), q3=round(g,2))

