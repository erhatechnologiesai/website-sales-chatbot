from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ProductInfo(BaseModel):
    name: str
    tier: str
    price_monthly: int
    features: List[str]

class LeadCaptureRequest(BaseModel):
    name: str
    email: str
    company: Optional[str] = "Independent"
    monthly_budget: int
    timeline_weeks: int
    needs_description: str

class LeadQualificationResult(BaseModel):
    lead_id: str
    qualification_score: int
    status: str  # QUALIFIED, NURTURE, DISQUALIFIED
    recommended_tier: str
    call_to_action: str
    timestamp: datetime = datetime.utcnow()

class SalesChatRequest(BaseModel):
    session_id: str
    user_query: str
    lead_email: Optional[str] = None
