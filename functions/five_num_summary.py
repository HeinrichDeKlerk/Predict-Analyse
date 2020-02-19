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
    
    for num in items:
        s_list = sorted(items)
        n_max = np.max(s_list)
        n_med = np.median(s_list)       
        n_q1 = np.percentile(s_list, 25)
        n_min = np.min(s_list)
        n_q3 = np.percentile(s_list, 75)
        
        D = { "max":n_max, "median":n_med, "min":n_min, "q1":n_q1, "q3":n_q3}
    return D

