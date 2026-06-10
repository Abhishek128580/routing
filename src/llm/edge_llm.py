from urllib import response

from transformers import pipeline

print("Loading Flan-T5...")

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

print("Edge LLM Ready")


def generate_response(query):

    result = generator(
        query,
        max_new_tokens=40,
        do_sample=True,
        temperature=0.7
    )

    response = result[0]["generated_text"]

    # temporary confidence estimate

    response_words = len(response.split())
    query_words = len(query.split())

    confidence = min(
        (response_words / max(query_words, 1)) / 5,
        1.0
    )

    return {
        "response": response,
        "confidence": round(
            confidence,
            2
        )
    }