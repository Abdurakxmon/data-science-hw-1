def typeBasedTransformer(**kwargs):
    data = {}
    for key, value in kwargs.items():
        data[key] = value
        if isinstance(value, (int, float)):
            data[key] = value**2
        elif isinstance(value, (str, list, tuple)):
            data[key] = value[::-1]
        elif isinstance(value, bool):
            data[key] = [True,False][value]
        elif isinstance(value, dict):
            s={}
            for i,j in value.items(): s[j] = i
            data[key] = s
    
    return data
