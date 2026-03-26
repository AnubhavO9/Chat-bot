import os
from openai import OpenAI
from dotenv import load_dotenv

# Load env
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat():
    print("🤖 AI Chatbot (type 'exit' to quit)\n")

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        # Add user message
        messages.append({"role": "user", "content": user_input})

        # Call OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content

        print("Bot:", reply, "\n")

        # Save response
        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat()