def detect_intent(user_input: str) -> str:
    text = user_input.lower()

    greeting_words = ["hi", "hello", "hey"]
    high_intent_words = ["buy", "subscribe", "sign up", "start", "try", "interested", "want"]
    pricing_words = ["price", "cost", "plan", "pricing", "features"]

    # 🔥 PRIORITY: High intent FIRST
    if any(word in text for word in high_intent_words):
        return "high_intent"

    if any(word in text for word in pricing_words):
        return "pricing"

    if any(word in text for word in greeting_words):
        return "greeting"

    return "general"