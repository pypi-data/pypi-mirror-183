from flatten_everything import flatten_everything


def group_lists_with_intersections(list_, keep_duplicates=False):
    results = tuple((frozenset(x) for x in list_))
    results2 = results
    for r in results:
        newresults2 = []
        for r2 in results2:
            if not isinstance(r2, (frozenset,set)):
                sr=frozenset(r2)
            else:
                sr=r2
            inter = (r.intersection(sr))
            if inter:
                appe = r.union(r2)
                newresults2.append(((appe)))
            else:
                newresults2.append(sr)
        results2 = set(((frozenset(x) for x in newresults2 if x)))
    results2 = tuple(tuple(x) for x in results2)
    if keep_duplicates:
        flattened = tuple(flatten_everything(list_))
        results2 = [
            tuple(flatten_everything([(y,) * flattened.count(y) for y in x]))
            for x in results2
        ]
    return results2

