CATALOG = [
    {"name": "AI Starter Node", "tier": "Starter", "price_monthly": 499, "features": ["1 Autonomous Agent", "Up to 5k requests/mo", "Community Support"]},
    {"name": "Enterprise Multi-Agent Mesh", "tier": "Enterprise", "price_monthly": 2499, "features": ["Unlimited Agents", "Custom RAG Pipelines", "24/7 Dedicated Support", "SLA Guarantees"]},
    {"name": "Custom Workflow Automation", "tier": "Custom", "price_monthly": 1499, "features": ["Full Stack Integration", "CRM & Webhook Sync", "Weekly Optimization"]}
]

def search_products(query: str):
    q = query.lower()
    return [p for p in CATALOG if any(w in p["name"].lower() or w in p["tier"].lower() for w in q.split())] or CATALOG
