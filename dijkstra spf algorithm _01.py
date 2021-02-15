graph = {}
cost = {}
parents = {}

visited = []

# graph
graph["start"] = {}
graph["start"]["A"] = 10
graph["start"]["B"] = 20
graph["start"]["C"] = 15

graph["a"] = {}
graph["a"]["c"] = 10
graph["a"]["d"] = 25

graph["b"] = {}
graph["b"]["e"] = 30

graph["c"] = {}
graph["c"]["b"] = 5
graph["c"]["e"] = 30

graph["d"] = {}
graph["d"]["finish"] = 20

graph["e"] = {}
graph["e"]["d"] = 10
graph["e"]["finish"] = 15

graph["finish"] = {}

print ("Graph", graph)

#costs
infinity = float("inf")

cost["a"] = 10
cost["b"] = 20
cost["c"] = 15
cost["d"] = infinity
cost["e"] = infinity
cost["finish"] = infinity

print ("Cost", cost)


# parents
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = "start"
# parents["d"] = "a"
# parents["d"] = "e"
# parents["e"] = "b"
# parents["e"] = "c"
parents["in"] = None


# function to find lowest cost node
def find_lowest_cost_node(cost):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in cost:
        if lowest_cost < cost[node] and cost[node] not in visited:
            lowest_cost = cost[node]
            lowest_cost_node = node
    return lowest_cost_node

