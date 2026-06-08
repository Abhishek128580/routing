import pandas as pd

from classifier import classify_query

df = pd.read_csv("C:\\Users\\kotha\\OneDrive\\Desktop\\Intelligent-Query-Routing\\src\\data\\queries.csv")

for idx, row in df.iterrows():

    result = classify_query(
        row["query"]
    )

    print("-" * 50)

    print("Query:")
    print(result["query"])

    print("Domain:")
    print(result["domain"])

    print("Confidence:")
    print(result["domain_confidence"])

    print("Complexity:")
    print(result["complexity"])