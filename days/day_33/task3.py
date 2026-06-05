import itertools
methods = ["GET", "POST", "PUT"]
statuses = [200, 404, 500]
formats = ["JSON", "XML"]

comb = list(itertools.product(methods, "-", statuses, "-", formats))
print(comb)
res = [" ".join(map(str, tup)) for tup in comb]
print(res)