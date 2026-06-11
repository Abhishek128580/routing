# # import pandas as pd

# # from classifier.classifier import classify_query

# # from scheduler.heuristic_scheduler import route_query

# # from simulator.simulator import LOW

# # from logs.logger import log_routing


# # df = pd.read_csv(
# #     "C:\\Users\\kotha\\OneDrive\\Desktop\\Intelligent-Query-Routing\\src\\data\\queries.csv"
# # )

# # for _, row in df.iterrows():

# #     query = row["query"]

# #     result = classify_query(query)

# #     route = route_query(
# #         result["complexity"],
# #         LOW.load
# #     )

# #     log_routing(
# #         query,
# #         result["domain"],
# #         result["complexity"],
# #         LOW.name,
# #         route
# #     )

# # print(
# #     f"Processed {len(df)} queries"
# # )

# import pandas as pd

# from classifier.classifier import classify_query

# from complexity.complexity_scorer import calculate_complexity

# from simulator.network_generator import generate_network_state

# from scheduler.heuristic_scheduler import route_query

# from analytics.metrics import estimate_processing_time

# from logs.logger import log_routing


# df = pd.read_csv(
#    "C:\\Users\\kotha\\OneDrive\\Desktop\\Intelligent-Query-Routing\\src\\data\\queries.csv"
# )

# for _, row in df.iterrows():

#     query = row["query"]

#     classification = classify_query(query)

#     complexity_info = calculate_complexity(
#         query
#     )

#     network = generate_network_state()

#     route = route_query(
#         complexity_info["complexity"],
#         network["latency"],
#         network["load"]
#     )

#     processing_time = estimate_processing_time(
#         route,
#         network["latency"]
#     )

#     log_routing(
#         query,
#         classification["domain"],
#         complexity_info["complexity"],
#         complexity_info["score"],
#         network["latency"],
#         network["load"],
#         route,
#         processing_time
#     )

# print(
#     f"Processed {len(df)} queries"
# )

import pandas as pd

from classifier.classifier import classify_query

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

from logs.logger import log_routing


df = pd.read_csv(
    "C:\\Users\\kotha\\OneDrive\\Desktop\\Intelligent-Query-Routing\\src\\data\\queries.csv"
)

for _, row in df.iterrows():

    query = row["query"]

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

    log_routing(
        query,
        classification["domain"],
        classification[
            "domain_confidence"
        ],
        complexity_info[
            "complexity"
        ],
        complexity_info[
             "predicted_label"
             "semantic_confidence"
        ],
        network["latency"],
        network["load"],
        route_score,
        route
    )

print(
    f"Processed {len(df)} queries"
)