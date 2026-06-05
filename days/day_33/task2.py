import itertools

switches = ["Red", "Blue", "Brown", "Black", "Silver"]
print(*list(itertools.combinations(switches, 3)))