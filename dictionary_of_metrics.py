### START FUNCTION
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
