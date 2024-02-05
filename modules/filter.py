def __listToDictionary(list):
    newDict = {}
    for value in list:
        newDict.update(value)
    return newDict

def filterData(data: dict, keysToFilter: (tuple, list, str), keysToSubFilter: dict = None):
    filtered: dict = {}

    if isinstance(keysToFilter, (tuple, list)):
        filtered: dict = data.fromkeys(keysToFilter)
        for key, val in filtered.items():
            filtered[key] = data.get(key)
    elif isinstance(keysToFilter, str):
        filtered.update({keysToFilter: None})
        filtered[keysToFilter] = data.get(keysToFilter)
    elif isinstance(keysToFilter, type(None)):
        raise TypeError("keysToFilter cannot be NONE!")
    else:
        raise TypeError("keysToFilter is not list, tuple or string!")

    if not keysToSubFilter:
        return filtered

    for key, val in keysToSubFilter.items():
        if isinstance(filtered.get(key), (list, tuple)):
            filtered[key] = filterData(__listToDictionary(filtered[key]), val)
        elif isinstance(filtered.get(key), str):
            filtered[key] = filterData(filtered[key], key)
        elif isinstance(filtered.get(key), type(None)):
            raise KeyError("key {key_name} doesn't exit or its value is NONE!".format(key_name=key))
        else:
            raise TypeError("key {key_name} is not a list, tuple, or string!".format(key_name=key))
    return filtered
