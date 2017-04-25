def flatten(nested, flat=None):
    if flat == None:
        flat = []
    for i in nested:
        if isinstance(i, list):
            flatten(i, flat)
        else:
            flat.append(i)
    return flat


nested = ["a", ["b", "c", ["d"], "e"]]
print(flatten(nested))
print(flatten(nested))
