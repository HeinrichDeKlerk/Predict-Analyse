def dictionary_of_metrics(items):
    """
    Docstring here
    """
    D= {'mean': round(np.mean(np.array(items)),2),
         'median':round(np.median(np.array(items)),2),
         'variance' : round(np.var(np.array(items)),2),
         'standard deviation': round(np.std(np.array(items)),2),
         'min': round(min(np.array(items)),2),
         'max': round(max(np.array(items)),2)}
    return D