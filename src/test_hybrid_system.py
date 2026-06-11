from classifier.classifier import (
    classify_query
)

from complexity.complexity_scorer import (
    calculate_complexity
)

from simulator.network_generator import (
    generate_network_state
)

from scheduler.heuristic_scheduler import (
    calculate_route_score,
    route_query
)

from router.hybrid_router import (
    execute_route
)

query = input(
    "Enter Query: "
)

classification = classify_query(
    query
)

complexity_info = (
    calculate_complexity(
        query,
        classification["domain"],
        classification[
            "domain_confidence"
        ]
    )
)

network = (
    generate_network_state()
)

route_score = (
    calculate_route_score(
        complexity_info["score"],
        network["latency"],
        network["load"],
        classification[
            "domain_confidence"
        ]
    )
)

route = route_query(
    route_score
)

result = execute_route(
    route,
    query
)

print("\nDomain:")
print(
    classification["domain"]
)

print("\nComplexity:")
print(
    "\nSemantic Label:"
)

print(
    complexity_info[
        "predicted_label"
    ]
)

print(
    "\nSemantic Confidence:"
)

print(
    complexity_info[
        "semantic_confidence"
    ]
)

print("\nRoute:")
print(route)

print("\nTier:")
print(
    result["tier"]
)

print("\nResponse:")
print(
    result["response"]
)

print("Confidence:",
      classification["domain_confidence"])

print("Complexity Score:",
      complexity_info["score"])

print("Latency:",
      network["latency"])

print("Load:",
      network["load"])

print("Route Score:",
      route_score)