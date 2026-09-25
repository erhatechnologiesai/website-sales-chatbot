import unittest
from fastapi.testclient import TestClient
from app.api import app
from app.services.qualifier_service import evaluate_lead
from app.models import LeadCaptureRequest

class TestSalesChatbot(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_catalog_endpoint(self):
        res = self.client.get("/catalog")
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(len(res.json()["catalog"]), 1)

    def test_sales_chat(self):
        res = self.client.post("/chat", json={"session_id": "s1", "user_query": "How much does enterprise cost?"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("Enterprise", res.json()["reply"])

    def test_lead_qualification_high_score(self):
        lead = LeadCaptureRequest(
            name="John Doe",
            email="john@example.com",
            company="Tech Corp",
            monthly_budget=3000,
            timeline_weeks=2,
            needs_description="We require an automated customer support multi-agent pipeline."
        )
        res = evaluate_lead(lead)
        self.assertEqual(res.status, "QUALIFIED")
        self.assertGreaterEqual(res.qualification_score, 70)
        self.assertIn("VIP", res.call_to_action)

if __name__ == "__main__":
    unittest.main()
