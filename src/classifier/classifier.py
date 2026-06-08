from transformers import pipeline

LABELS = [
    "software engineering and programming",
    "medicine and healthcare",
    "law and legal matters",
    "mathematics and statistics",
    "natural science and physics",
    "business finance and economics",
    "general trivia and history"
]

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)


def classify_query(query):

    result = classifier(
        query,
        LABELS
    )

    domain = result["labels"][0]
    confidence = float(result["scores"][0])

    words = len(query.split())

    if words < 10:
        complexity = "low"
    elif words < 25:
        complexity = "medium"
    else:
        complexity = "high"

    return {
        "query": query,
        "domain": domain,
        "domain_confidence": round(confidence, 4),
        "complexity": complexity
    }


if __name__ == "__main__":

    query = "Explain recursion in Python"

    print(classify_query(query))