
def five_num_summary(items):
    """
    This function takes in 1 list(item) of int or float as argument, It then returns the Five Number Summary of list.
    Five number summary = list maximum, minimum, median, 25th percentile and 75th percentile.
    """
    
    a=np.max(items)
    s=np.median(items)
    d=np.min(items)
    f=np.quantile(items, .25)
    g=np.quantile(items, .75)
    
    return dict(max=round(a,2), median=round(s,2),min =round(d,2), q1=round(f,2), q3=round(g,2))
