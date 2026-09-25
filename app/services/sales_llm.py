from app.services.catalog_service import CATALOG

def answer_sales_query(query: str) -> str:
    q = query.lower()
    if "price" in q or "cost" in q:
        tiers = ", ".join([f"{p['name']} (${p['price_monthly']}/mo)" for p in CATALOG])
        return f"We offer flexible packages designed for scale: {tiers}. Which one fits your workflow goals?"
    elif "enterprise" in q or "custom" in q:
        return "Our Enterprise tier provides bespoke multi-agent workflows with guaranteed uptime and custom LLM tuning. Would you like to qualify your budget and book a demo?"
    else:
        return "Erha Technologies provides high-performance AI automation solutions. Tell us about your current operational bottlenecks so we can recommend the optimal agent architecture!"
