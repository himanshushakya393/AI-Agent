import json

def load_knowledge():
    with open("data/knowledge.json", "r") as f:
        return json.load(f)

def get_answer(query: str) -> str:
    kb = load_knowledge()
    q = query.lower()

    if "price" in q or "plan" in q:
        return f"""
📊 AutoStream Pricing:

🔹 Basic Plan - {kb['pricing']['basic']['price']}
   - {kb['pricing']['basic']['videos']}
   - {kb['pricing']['basic']['resolution']}

🔹 Pro Plan - {kb['pricing']['pro']['price']}
   - {kb['pricing']['pro']['videos']}
   - {kb['pricing']['pro']['resolution']}
   - AI captions included
   - 24/7 support

"""

    if "refund" in q:
        return f"📌 Policy: {kb['policies']['refund']}"

    if "support" in q:
        return f"📌 Support: {kb['policies']['support']}"

    return "Ask me about pricing, features, or getting started!"