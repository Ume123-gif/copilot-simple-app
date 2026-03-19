import random

def get_motivation():
    quotes = [
        "Believe you can and you're halfway there.",
        "Your code is a work of art in progress.",
        "Mistakes are proof that you are trying.",
        "Don't stop until you're proud.",
        "You are closer than you were yesterday."
    ]
    return random.choice(quotes)

print("--- AI Developer Cheerleader ---")
print(f"Today's Motivation: {get_motivation()}")
print("--------------------------------")
