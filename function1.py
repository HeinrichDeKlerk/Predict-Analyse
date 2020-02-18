def dictionary_of_metrics(items):
    """
    This function make use of Numpay labraries to calculate the 
    mean, median, variance(Var), standard deviation (std), 
    minimum(min) and maximum(max) of a list of items.

    """
    D = {'mean': round(np.mean(np.array(items)),2),
         'median':round(np.median(np.array(items)),2),
         'var' : round(np.var(np.array(items)),2),
         'std': round(np.std(np.array(items)),2),
         'min': round(min(np.array(items)),2),
         'max': round(max(np.array(items)),2)}
    return D