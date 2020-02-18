
def five_num_summary(items):
    
    a=np.max(items)
    s=np.median(items)
    d=np.min(items)
    f=np.quantile(items, .25)
    g=np.quantile(items, .75)
    
    return dict(max=round(a,2), median=round(s,2),min =round(d,2), q1=round(f,2), q3=round(g,2))
