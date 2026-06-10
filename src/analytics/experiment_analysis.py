# import pandas as pd

# df = pd.read_csv(
#     "src/experiments/experiment_results.csv"
# )

# print("\nTotal Samples:")
# print(len(df))

# print("\nRoute Distribution:")

# counts = df["route"].value_counts()

# for route, count in counts.items():

#     percentage = (
#         count / len(df)
#     ) * 100

#     print(
#         f"{route}: "
#         f"{count} "
#         f"({percentage:.2f}%)"
#     )

# print("\nAverage Route Score:")
# print(
#     round(
#         df["route_score"].mean(),
#         2
#     )
# )

# print("\nAverage Latency:")
# print(
#     round(
#         df["latency"].mean(),
#         2
#     )
# )

# print("\nAverage Load:")
# print(
#     round(
#         df["load"].mean(),
#         2
#     )
# )

import pandas as pd

df = pd.read_csv(
    "src/experiments/experiment_results.csv"
)

print("\n====================")
print("EXPERIMENT SUMMARY")
print("====================")

print(
    f"\nTotal Samples: {len(df)}"
)

print("\nRoute Distribution")

counts = (
    df["route"]
    .value_counts()
)

for route, count in counts.items():

    percent = (
        count / len(df)
    ) * 100

    print(
        f"{route}: "
        f"{count} "
        f"({percent:.2f}%)"
    )

print("\nAverage Route Score")

print(
    round(
        df["route_score"].mean(),
        2
    )
)

print("\nAverage Latency")

print(
    round(
        df["latency"].mean(),
        2
    )
)

print("\nAverage Load")

print(
    round(
        df["load"].mean(),
        2
    )
)

print("\nAverage Complexity Score")

print(
    round(
        df["complexity_score"].mean(),
        2
    )
)