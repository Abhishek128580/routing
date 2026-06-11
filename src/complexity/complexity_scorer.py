from transformers import pipeline

print("Loading Complexity Classifier...")

complexity_classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

print("Complexity Classifier Ready")

COMPLEXITY_LABELS = [
    "simple factual query",
    "technical explanation",
    "system design problem",
    "research level problem"
]


def calculate_complexity(
    query,
    domain,
    confidence
):

    query_lower = query.lower()
    word_count = len(query.split())

    # --------------------
    # Rule Override Layer
    # --------------------

    factual_starters = (
        "what",
        "who",
        "when",
        "where"
    )

    if (
        word_count <= 4 and
        query_lower.startswith(factual_starters)
    ):

        return {
            "complexity": "low",
            "score": 20,
            "predicted_label":
            "simple factual query",
            "semantic_confidence": 1.0
        }

    # --------------------
    # Semantic Layer
    # --------------------

    result = complexity_classifier(
        query,
        COMPLEXITY_LABELS
    )

    predicted = result["labels"][0]

    semantic_score = result["scores"][0]

    if predicted == "simple factual query":

        complexity = "low"

        complexity_score = (
            25 +
            semantic_score * 10
        )

    elif predicted == "technical explanation":

        complexity = "medium"

        complexity_score = (
            50 +
            semantic_score * 15
        )

    elif predicted == "system design problem":

        complexity = "high"

        complexity_score = (
            85 +
            semantic_score * 15
        )

    else:

        complexity = "high"

        complexity_score = (
            95 +
            semantic_score * 20
        )

    return {

        "complexity":
        complexity,

        "score":
        round(
            complexity_score,
            2
        ),

        "predicted_label":
        predicted,

        "semantic_confidence":
        round(
            semantic_score,
            4
        )
    }