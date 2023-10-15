import time


def timer(f):
    def i(*args):
        s = time.time()
        r = f(*args)
        print('t: ', time.time() - s)
        return r

    return i


def solve(candidates, target):
    def add_to_solutions(solutions, solution):
        if solution not in solutions:
            solutions.append(solution)

    def add_to_results(results, solution):
        if solution not in results:
            results.append(solution)

    solutions, results = [], []
    while candidates:
        candidate = candidates.pop()
        for i in range(len(solutions)):
            solution = [*solutions[i], candidate]
            s = sum(solution)
            if s <= target:
                add_to_solutions(solutions, solution)
                if s == target:
                    add_to_results(results, sorted(solution))
        if candidate <= target:
            solution = [candidate]
            add_to_solutions(solutions, solution)
            if sum(solution) == target:
                add_to_results(results, solution)
    print(results)
    return results


@timer
def solve_(candidates, target):
    solutions = []
    results = []
    while candidates:
        candidate = candidates.pop()
        for i in range(len(solutions)):
            solution = solutions[i]
            s = sum(solution) + candidate
            if s <= target:
                solution = [*solution, candidate]
                if solution not in solutions:
                    solutions.append(solution)
                    if s == target:
                        _solution = sorted(solution)
                        if _solution not in results:
                            results.append(_solution)
        if candidate <= target:
            solution = [candidate]
            if solution not in solutions:
                solutions.append(solution)
                if sum(solution) == target and solution not in results:
                    results.append(solution)
    print(results)
    return results


solve([8, 7, 4, 3], 11)

solve([10, 1, 2, 7, 6, 1, 5], 8)

solve([2, 5, 2, 1, 2], 5)

solve([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27)

solve(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 30)
