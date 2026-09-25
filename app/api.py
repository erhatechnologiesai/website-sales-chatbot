from fastapi import FastAPI, HTTPException
from app.config import settings
from app.models import SalesChatRequest, LeadCaptureRequest, LeadQualificationResult
from app.services.catalog_service import CATALOG
from app.services.qualifier_service import evaluate_lead
from app.services.sales_llm import answer_sales_query

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.get("/")
def home():
    return {"service": settings.PROJECT_NAME, "status": "active", "version": settings.VERSION}

@app.get("/catalog")
def get_catalog():
    return {"catalog": CATALOG}

@app.post("/chat")
def sales_chat(request: SalesChatRequest):
    if not request.user_query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    reply = answer_sales_query(request.user_query)
    return {"session_id": request.session_id, "reply": reply, "cta": "Submit your requirements for instant qualification!"}

@app.post("/qualify-lead", response_model=LeadQualificationResult)
def qualify_lead(lead: LeadCaptureRequest):
    return evaluate_lead(lead)
