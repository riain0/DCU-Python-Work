def swap_keys_values(d):
    new_d = {}
    for k in d:
        v = d.get(k)
        new_d[v] = k
    return new_d
