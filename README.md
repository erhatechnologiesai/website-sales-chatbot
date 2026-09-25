# AI Website Sales Chatbot

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An autonomous website sales agent designed to qualify inbound leads in real time, recommend appropriate solution tiers, handle objections, and maximize conversion through dynamic Call-to-Action (CTA) generation.

---

## Key Features

- **BANT**: lead qualification scoring prospects on Budget, Authority, Need, and Timeline
- **Dynamic**: product catalog recommendations matching customer requirements to tiers
- **Autonomous**: objection handling addressing pricing, implementation time, and compliance concerns
- **Dynamic**: Call-to-Action (CTA) routing high-intent leads to VIP calendars or nurture cadences
- **FastAPI**: microservice architecture with complete input validation

---

## Architecture

```mermaid
flowchart LR
    Visitor([Website Visitor]) -->|Chat / Inquire| API[FastAPI Sales Endpoint]
    API --> Catalog[Product Knowledge Base]
    API --> Qualifier[BANT Lead Qualifier]
    Qualifier --> Scoring[Heuristic Matrix]
    Scoring -->|High Intent| VIP[VIP Calendar Booking]
    Scoring -->|Nurture| LeadGen[CRM Lead Ingestion]
    API --> Visitor
```

---

## Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| **Runtime** | Python 3.12 | Core execution environment |
| **API Framework** | FastAPI & Uvicorn | High-performance asynchronous REST endpoints |
| **Data Validation** | Pydantic v2 | Strict schema validation and serialization |
| **Domain Engine** | Dual-Mode (Local + LLM) | Production-ready AI logic with offline test capability |
| **Testing** | Unittest & Pytest | Deterministic automated verification suite |

---

## Project Structure

```text
ai-website-sales-chatbot/
├── app/
│   ├── __init__.py
│   ├── api.py           # FastAPI routes and server definitions
│   ├── config.py        # Environment variables and application settings
│   ├── models.py        # Pydantic data schemas
│   └── services/        # Core business and AI automation logic
├── tests/
│   ├── __init__.py
│   └── test_sales_bot.py   # Automated test suite
├── .env.example         # Template for environment configuration
├── .gitignore           # Python and runtime exclusions
├── LICENSE              # MIT License
├── README.md            # Comprehensive project documentation
└── requirements.txt     # Python package dependencies
```

---

## Getting Started

### Prerequisites

- Python 3.10+ (Python 3.12 recommended)
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/erhatechnologiesai/ai-website-sales-chatbot.git
   cd ai-website-sales-chatbot
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration if running in live mode
   ```

---

## Running the Application

Start the local development server with auto-reload:

```bash
python -m uvicorn app.api:app --reload --host 0.0.0.0 --port 8000
```

Once running, interactive documentation is accessible at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check and catalog status |
| `GET` | `/catalog` | List available product tiers and pricing models |
| `POST` | `/chat` | Interactive sales consultation dialogue turn |
| `POST` | `/qualify-lead` | Score and classify prospect under BANT framework |

### Example Request

```bash
curl -X POST http://127.0.0.1:8000/qualify-lead -H "Content-Type: application/json" -d '{"budget": 15000, "authority": "Decision Maker", "need": "Enterprise AI", "timeline": "Immediate"}'
```

---

## Running Tests

Execute the automated test suite:

```bash
python -m unittest tests/test_sales_bot.py
```

Or using pytest:

```bash
pytest tests/
```

All test cases are self-contained and run offline without requiring third-party API credentials.

---

## Security & Best Practices

- **Zero Credential Leakage**: API tokens and secrets are loaded exclusively via environment variables and excluded by `.gitignore`.
- **Strict Validation**: All incoming request payloads are strictly validated using Pydantic schemas.
- **Fail-Safe Fallbacks**: Deterministic offline engines guarantee application continuity even during external provider outages.

---

## License

This project is licensed under the terms of the [MIT License](LICENSE).
