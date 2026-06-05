import itertools

servers = ["Srv1", "Srv2", "Srv3", "Srv4"]
print(*list(itertools.combinations(servers, 2)))

