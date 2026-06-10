from llm.edge_llm import (
    generate_response
)

from router.cascade_router import (
    cascade_decision
)

query = input(
    "Enter Query: "
)

result = generate_response(
    query
)

decision = cascade_decision(
    result["confidence"]
)

print("\nResponse")
print(result["response"])

print("\nConfidence")
print(result["confidence"])

print("\nDecision")
print(decision)