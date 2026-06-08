from classifier.classifier import classify_query

from scheduler.heuristic_scheduler import route_query

from simulator.simulator import LOW

from logs.logger import log_routing


query = input("Enter Query: ")

result = classify_query(query)

route = route_query(
    result["complexity"],
    LOW.load
)

print("\n------------------")
print("Classification")
print("------------------")

print("Domain:",
      result["domain"])

print("Complexity:",
      result["complexity"])

print("Confidence:",
      result["domain_confidence"])

print("\n------------------")
print("Routing")
print("------------------")

print("Network:", LOW.name)

print("Selected Tier:",
      route)

log_routing(
    query,
    result["domain"],
    result["complexity"],
    LOW.name,
    route
)