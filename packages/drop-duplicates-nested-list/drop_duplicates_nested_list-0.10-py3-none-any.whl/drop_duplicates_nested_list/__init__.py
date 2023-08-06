def drop_duplicates(l):
    istup = isinstance(l, tuple)
    tempdict = {}
    for ll in l:
        try:
            tempdict[ll] = ll
        except Exception:
            tempdict[str(ll) + repr(ll)] = ll
    fin = [x[1] for x in tempdict.items()]
    if istup:
        return tuple(fin)
    return fin

