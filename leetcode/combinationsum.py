def solve(candidates, target, results, prev=[]):
    for c in filter(lambda x: x <= target, candidates):
        curr = [*prev, c]
        s = sum(curr)
        if s == target:
            result = sorted(curr)
            if result not in results:
                results.append(result)
        if s < target:
            solve(candidates, target, results, curr)


results = []
solve([2, 3, 6, 7], 7, results)
print(results)

results = []
solve([2, 3, 5], 8, results)
print(results)

results = []
solve([2], 1, results)
print(results)
