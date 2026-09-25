import uuid
from app.models import LeadCaptureRequest, LeadQualificationResult
from app.config import settings

def evaluate_lead(lead: LeadCaptureRequest) -> LeadQualificationResult:
    score = 0
    if lead.monthly_budget >= 2000:
        score += 40
    elif lead.monthly_budget >= 500:
        score += 25
    else:
        score += 10
        
    if lead.timeline_weeks <= 2:
        score += 30
    elif lead.timeline_weeks <= 6:
        score += 20
    else:
        score += 10
        
    if len(lead.needs_description.strip()) > 30:
        score += 30
    else:
        score += 15

    if score >= settings.MIN_QUALIFICATION_SCORE:
        status = "QUALIFIED"
        recommended_tier = "Enterprise Multi-Agent Mesh" if lead.monthly_budget >= 2000 else "Custom Workflow Automation"
        cta = "Schedule VIP Architecture Call with Erha AI Specialists"
    elif score >= 40:
        status = "NURTURE"
        recommended_tier = "AI Starter Node"
        cta = "Download Erha Whitepaper & Explore Demo Sandbox"
    else:
        status = "DISQUALIFIED"
        recommended_tier = "Self-Service Tier"
        cta = "Join Community Forum"

    lead_id = f"LEAD-{uuid.uuid4().hex[:6].upper()}"
    return LeadQualificationResult(
        lead_id=lead_id,
        qualification_score=score,
        status=status,
        recommended_tier=recommended_tier,
        call_to_action=cta
    )
