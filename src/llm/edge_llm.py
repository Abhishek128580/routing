from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

print("Loading Flan-T5...")

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(
    model_name
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    model_name
)

print("Edge LLM Ready")


def generate_response(query):

    inputs = tokenizer(
        query,
        return_tensors="pt"
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=50
    )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return {
        "response": response
    }