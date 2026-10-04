import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=api_key)

print("=" * 45)
print("🤖  MY AI ASSISTANT")
print("=" * 45)
print("Type your message below.")
print("Commands: 'clear' = reset chat | 'exit' = quit")
print("-" * 45)

conversation = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if user_input.lower() == "clear":
        conversation.clear()
        print("🧹 Conversation cleared!\n")
        continue

    conversation.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.responses.create(
            model="gpt-6-luna",
            instructions="""
            You are a helpful and friendly AI assistant.

            Rules:
            1. Explain things in simple language.
            2. For technical questions, give a beginner-friendly explanation.
            3. Use examples when they make the answer clearer.
            4. If the user seems confused, explain the concept step by step.
            5. Do not make up information. If you are unsure, say so.
            """,
            input=conversation
        )

        print("AI:", response.output_text)

        conversation.append({
            "role": "assistant",
            "content": response.output_text
        })

    except Exception as e:
        print("⚠️ Something went wrong. Please try again.")

    print("AI:", response.output_text)

    conversation.append({
        "role": "assistant",
        "content": response.output_text
    })