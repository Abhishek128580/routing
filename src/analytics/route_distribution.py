import pandas as pd

df = pd.read_csv(
    r"C:\Users\kotha\OneDrive\Desktop\Intelligent-Query-Routing\src\logs\routing_logs.csv"
)

counts = (
    df["route"]
    .value_counts()
)

total = len(df)

print("\nRoute Distribution\n")

for route, count in counts.items():

    percent = (
        count / total
    ) * 100

    print(
        f"{route}: "
        f"{count} "
        f"({percent:.2f}%)"
    )