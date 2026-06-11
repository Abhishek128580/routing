from cloud.gemini_client import (
    generate_cloud_response
)

query = input(
    "Enter Query: "
)

response = generate_cloud_response(
    query
)

print("\nResponse:\n")

print(response)