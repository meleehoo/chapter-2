from itertools import combinations

def all_subsets(lst):
    subsets = []
    for i in range(len(lst) + 1):
        subsets.extend(combinations(lst, i))
    return [list(subset) for subset in subsets]

lst = [1, 2, 3]
print(all_subsets(lst))