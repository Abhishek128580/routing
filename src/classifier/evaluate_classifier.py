import pandas as pd
from classifier import classify_query

df = pd.read_csv("C:\\Users\\kotha\\OneDrive\\Desktop\\Intelligent-Query-Routing\\src\\data\\queries.csv")

correct = 0
total = len(df)

for _, row in df.iterrows():

    result = classify_query(row["query"])

    predicted = result["domain"]
    actual = row["expected_domain"]

    print("\n--------------------------------")
    print("Query:", row["query"])
    print("Expected:", actual)
    print("Predicted:", predicted)
    print("Confidence:", result["domain_confidence"])

    if predicted == actual:
        correct += 1

accuracy = correct / total

print("\n==========================")
print(f"Correct: {correct}")
print(f"Total: {total}")
print(f"Accuracy: {accuracy:.2%}")