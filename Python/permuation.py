def permutation (l):
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
            candidates.append(el);
    
    for candidate in candidates:
        current.append(candidate)
        backtrack(current, solutions, original)
        current.pop()

print (permutation ([1,2,3]))