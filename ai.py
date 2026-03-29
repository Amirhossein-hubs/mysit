from openai import OpenAI

# This client can be used for other model providers
# as well, like google, anthropic, etc..
client = OpenAI(
    api_key="sk-8OoW9fIBwZw65zr8JgfzdStNwT1lHj4NHagdollt4nC3hioC",
    base_url="https://api.gapgpt.app/v1"
)

response = client.responses.create(
    model="gapgpt-qwen-3.5",
    input="سلام درباره خودت بگو"
)

print(response.output_text)