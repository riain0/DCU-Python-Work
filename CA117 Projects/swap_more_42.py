def swap_unique_keys_values(d):
    new_d = {}
    for k in d:
        v = d.get(k)
        if v in new_d:
            del new_d[v]
        else:
            new_d[v] = k
    return new_d
