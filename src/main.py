# from classifier.classifier import classify_query

# from scheduler.heuristic_scheduler import route_query

# from simulator.simulator import LOW

# from logs.logger import log_routing


# query = input("Enter Query: ")

# result = classify_query(query)

# route = route_query(
#     result["complexity"],
#     LOW.load
# )

# print("\n------------------")
# print("Classification")
# print("------------------")

# print("Domain:",
#       result["domain"])

# print("Complexity:",
#       result["complexity"])

# print("Confidence:",
#       result["domain_confidence"])

# print("\n------------------")
# print("Routing")
# print("------------------")

# print("Network:", LOW.name)

# print("Selected Tier:",
#       route)

# log_routing(
#     query,
#     result["domain"],
#     result["complexity"],
#     LOW.name,
#     route
# )

from classifier.classifier import classify_query

from complexity.complexity_scorer import calculate_complexity

from simulator.network_generator import generate_network_state

from scheduler.heuristic_scheduler import route_query

from analytics.metrics import estimate_processing_time

from logs.logger import log_routing


query = input("Enter Query: ")

classification = classify_query(query)

complexity_info = calculate_complexity(query)

network = generate_network_state()

route = route_query(
    complexity_info["complexity"],
    network["latency"],
    network["load"]
)

processing_time = estimate_processing_time(
    route,
    network["latency"]
)

print("\nDomain:",
      classification["domain"])

print("Confidence:",
      classification["domain_confidence"])

print("\nComplexity:",
      complexity_info["complexity"])

print("Complexity Score:",
      complexity_info["score"])

print("\nNetwork")

print(network)

print("\nRoute:",
      route)

print("Processing Time:",
      processing_time)

log_routing(
    query,
    classification["domain"],
    complexity_info["complexity"],
    complexity_info["score"],
    network["latency"],
    network["load"],
    route,
    processing_time
)