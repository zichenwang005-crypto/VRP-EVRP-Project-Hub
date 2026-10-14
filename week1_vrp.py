
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import time

# 0代表仓库，1~5代表客户
distance_matrix = [
    [0, 10, 15, 20, 12, 18],
    [10, 0, 8, 14, 9, 16],
    [15, 8, 0, 7, 11, 13],
    [20, 14, 7, 0, 6, 10],
    [12, 9, 11, 6, 0, 5],
    [18, 16, 13, 10, 5, 0],
]

start_time = time.perf_counter()

manager = pywrapcp.RoutingIndexManager(6, 1, 0)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(
    distance_callback
)

routing.SetArcCostEvaluatorOfAllVehicles(
    transit_callback_index
)

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
)
search_parameters.local_search_metaheuristic = (
    routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
)
search_parameters.time_limit.FromSeconds(1)

solution = routing.SolveWithParameters(search_parameters)

if solution:
    index = routing.Start(0)
    route = []
    route_distance = 0

    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        next_index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(
            index, next_index, 0
        )
        index = next_index

    route.append(manager.IndexToNode(index))

    print("=== Week 1 VRP Baseline ===")
    print("Route:", " -> ".join(map(str, route)))
    print("Total distance:", route_distance)
    print("Feasible:", True)
    print("Runtime:", round(time.perf_counter() - start_time, 3), "seconds")
else:
    print("No solution found")
