def five_num_summary(items):
    """
    doc strings here
    """
    Fun_2= {'max': round(max(items),2),
          'median': round(np.median(items),2),
          'min': round(min(items),2),
          'q1': round(np.quantile(items, q= 0.25),2),
          'q3': round(np.quantile(items, q= 0.75),2)}
    return Fun_2
    