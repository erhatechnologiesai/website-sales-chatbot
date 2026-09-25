import os
class Settings:
    PROJECT_NAME: str = "AI Website Sales Chatbot"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEMO_MODE: bool = os.getenv("DEMO_MODE", "true").lower() == "true"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    SALES_ALERT_EMAIL: str = os.getenv("SALES_ALERT_EMAIL", "sales@erhatechnologies.com")
    MIN_QUALIFICATION_SCORE: int = int(os.getenv("MIN_QUALIFICATION_SCORE", "60"))
settings = Settings()
