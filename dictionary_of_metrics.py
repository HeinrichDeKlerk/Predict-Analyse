def dictionary_of_metrics(items):
    for num in items:
    """
    This function takes in one argument, a list of numbers and computes the mean, median, variance,
    max and min numbers rounded to 2 decimal spaces, then outputs the operations into a dictionary.

    """
        sort_list = sorted(items)# list needs to be sorted for median
    
        num_mean = sum(items) / len(items)
        num_mean = round(num_mean, 2)
    
        if len(items) % 2 != 0: #median calculation to get index number/numbers of list middle
            ind = len(items)//2
            num_median = (sort_list[ind])
        else:
            ind = len(items)//2
            num_median = ((sort_list[ind] + sort_list[ind-1])/2)
        num_median = round(num_median,2)
        
        num_var = sum((num - num_mean) ** 2 for num in items) / (len(items) -1)
        num_var = round(num_var, 2)
    
        num_stddev = num_var ** (1/2)
        num_stddev = round(num_stddev, 2)
    
        num_min = min(items)
        num_min = round(num_min, 2)
    
        num_max = max(items)
        num_max = round(num_max,2)
    
        D = {"mean":num_mean, "median":num_median, "variance":num_var, "standard deviation":num_stddev, "min":num_min, "max":num_max}
    
    return D
