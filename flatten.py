def flatten(nested, flat=None):
    if not flat:
        flat = []
    for i in nested:
        if isinstance(i, list):
            flatten(i, flat)
        else:
            flat.append(i)
    return flat

def flat_list(array):
    res = []
    for i in array:
        if isinstance(i, list):
            res += flat_list(i)
        else:
            res.append(i)
    return res

nested = ["a", ["b", "c", ["d"], "e"]]
print(flat_list(nested))
