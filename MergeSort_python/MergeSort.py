def merge(l1, l2):
    if len(l1) == 0 and len(l2) == 0:
        return []
    elif len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    else:
        if l1[0] < l2[0]:
            merged = merge(l1[1:], l2)
            merged.insert(0, l1[0])
            return merged
        else:
            merged = merge(l1, l2[1:])
            merged.insert(0, l2[0])
            return merged

