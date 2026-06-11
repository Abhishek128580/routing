import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import pandas as pd

from classifier.classifier import classify_query
from complexity.complexity_scorer import calculate_complexity
from simulator.network_generator import generate_network_state
from scheduler.heuristic_scheduler import (
    calculate_route_score,
    route_query
)

df = pd.read_csv(
    "src/data/final_evaluation.csv"
)

correct = 0

for _, row in df.iterrows():

    query = row["query"]

    expected = row["expected_route"]

    classification = classify_query(
        query
    )

    complexity = calculate_complexity(
        query,
        classification["domain"],
        classification["domain_confidence"]
    )

    network = generate_network_state()

    score = calculate_route_score(
        complexity["score"],
        network["latency"],
        network["load"],
        classification["domain_confidence"]
    )

    predicted = route_query(
        score
    )

    print(
        f"\nQuery: {query}"
    )

    print(
        f"Expected: {expected}"
    )

    print(
        f"Predicted: {predicted}"
    )

    if predicted == expected:
        correct += 1

accuracy = (
    correct / len(df)
) * 100

print("\n================")
print("ROUTING ACCURACY")
print("================")

print(
    f"{accuracy:.2f}%"
)
print(
    complexity["predicted_label"]
)