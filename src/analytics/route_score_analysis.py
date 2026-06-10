import pandas as pd

df = pd.read_csv(
    "src/experiments/experiment_results.csv"
)

print(
    df["route_score"].describe()
)