def subsets(l):
    solutions = []
    backtrack(0, [], solutions, l)
    return solutions

def backtrack (ptr, current, solutions, original):
    if (ptr == len(original)):
        solutions.append(current.copy())
        return

    current.append(original[ptr])
    backtrack(ptr + 1, current, solutions, original)

    current.pop()
    backtrack(ptr + 1, current, solutions, original)

print (subsets([1,2,3]))