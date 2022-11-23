def derangement(l):
    solutions = []
    backtrack([], solutions, l)
    return solutions

def backtrack(current, solutions, original):
    if (len(current) == len(original)):
        solutions.append(current.copy())
        return

    candidates = []
    for el in original:
        if not el in current:
            if not el == len(current) + 1:
                candidates.append(el)
    
    for candidate in candidates:
        current.append(candidate)
        backtrack(current, solutions, original)
        current.pop()

print (derangement([1,2,3,4]))