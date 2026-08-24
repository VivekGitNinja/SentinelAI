#!/usr/bin/env python3
"""
Interactive Chat with SentinelAI Protection

A simple interactive chat using OpenAI, protected by SentinelAI SDK.

Prerequisites:
    # Clone the SentinelAI rules repository first
    git clone https://github.com/Nova-Hunting/sentinelai.rules

Usage:
    export OPENAI_API_KEY="your-key"
    python interactive_chat.py
"""

from openai import OpenAI
from sentinelai.sdk import Sentinel, SentinelBlockedError

# Initialize OpenAI
client = OpenAI()

# Initialize Sentinel with security policy
sentinelai.= Sentinel(
    rules_path="sentinelai.rules/",
    policy={
        "Jailbreak": {"action": "block"},
        "Injection": {"action": "block"},
        "DAN": {"action": "block"},
    }
)

# Protect the chat function with decorator
@sentinelai.protect(action="block")
def chat(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def main():
    print("SentinelAI Protected Chat (type 'quit' to exit)")
    print("-" * 40)

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            if not user_input:
                continue

            response = chat(user_input)
            print(f"\nAssistant: {response}")

        except SentinelBlockedError as e:
            print(f"\n[BLOCKED] {e.message}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
