# import sys
# import os

# sys.path.append(
#     os.path.abspath(
#         os.path.join(
#             os.path.dirname(__file__),
#             ".."
#         )
#     )
# )

# import pandas as pd

# from classifier.classifier import classify_query
# from complexity.complexity_scorer import calculate_complexity
# from simulator.network_generator import generate_network_state
# from scheduler.heuristic_scheduler import (
#     calculate_route_score,
#     route_query
# )

# NUM_RUNS = 100

# df = pd.read_csv(r"C:\Users\kotha\OneDrive\Desktop\Intelligent-Query-Routing\src\data\queries.csv")

# results = []

# for run in range(NUM_RUNS):

#     for _, row in df.iterrows():

#         query = row["query"]

#         classification = classify_query(query)

#         complexity_info = calculate_complexity(
#             query,
#             classification["domain"],
#             classification["domain_confidence"]
#         )

#         network = generate_network_state()

#         route_score = calculate_route_score(
#             complexity_info["score"],
#             network["latency"],
#             network["load"],
#             classification["domain_confidence"]
#         )

#         route = route_query(route_score)

#         results.append({
#             "route": route,
#             "latency": network["latency"],
#             "load": network["load"],
#             "route_score": route_score
#         })

# experiment_df = pd.DataFrame(results)

# experiment_df.to_csv(
#     r"C:\Users\kotha\OneDrive\Desktop\Intelligent-Query-Routing\src\experiments\experiment_results.csv",
#     index=False
# )

# print(
#     f"Generated {len(results)} routing decisions"
# )

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

NUM_RUNS = 100

print("Loading Dataset...")

df = pd.read_csv(r"C:\Users\kotha\OneDrive\Desktop\Intelligent-Query-Routing\src\data\queries.csv")

print(f"Loaded {len(df)} queries")

# --------------------------------------------------
# STEP 1 : CLASSIFY ONCE
# --------------------------------------------------

print("Precomputing BART Classifications...")

precomputed = []

for _, row in df.iterrows():

    query = row["query"]

    classification = classify_query(
        query
    )

    complexity_info = calculate_complexity(
        query,
        classification["domain"],
        classification["domain_confidence"]
    )

    precomputed.append(
        {
            "query": query,
            "domain": classification["domain"],
            "confidence": classification[
                "domain_confidence"
            ],
            "complexity": complexity_info[
                "complexity"
            ],
            "complexity_score": complexity_info[
                "score"
            ]
        }
    )

print(
    f"Cached {len(precomputed)} classifications"
)

# --------------------------------------------------
# STEP 2 : SIMULATIONS
# --------------------------------------------------

print(
    f"Running {NUM_RUNS} simulations..."
)

results = []

for run in range(NUM_RUNS):

    if run % 10 == 0:
        print(
            f"Simulation {run}/{NUM_RUNS}"
        )

    for item in precomputed:

        network = generate_network_state()

        route_score = calculate_route_score(
            item["complexity_score"],
            network["latency"],
            network["load"],
            item["confidence"]
        )

        route = route_query(
            route_score
        )

        results.append(
            {
                "query": item["query"],
                "domain": item["domain"],
                "confidence": item[
                    "confidence"
                ],
                "complexity": item[
                    "complexity"
                ],
                "complexity_score": item[
                    "complexity_score"
                ],
                "latency": network[
                    "latency"
                ],
                "load": network[
                    "load"
                ],
                "bandwidth": network[
                    "bandwidth"
                ],
                "route_score": route_score,
                "route": route
            }
        )

# --------------------------------------------------
# STEP 3 : SAVE RESULTS
# --------------------------------------------------

experiment_df = pd.DataFrame(
    results
)

experiment_df.to_csv(
    "src/experiments/experiment_results.csv",
    index=False
)

print("\nExperiment Complete")

print(
    f"Generated {len(results)} routing decisions"
)

print(
    "Saved to:"
)

print(
    "src/experiments/experiment_results.csv"
)