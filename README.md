# GeoPilot AI
### AI Copilot for Data Quality, Workflow Automation, and Operational Readiness

GeoPilot AI is a portfolio-grade enterprise AI copilot that audits incoming datasets, scores operational readiness, identifies quality risks, recommends remediation actions, and generates workflow plans.

## What it does
- audits uploaded CSV datasets
- computes a readiness score
- detects missingness, duplicates, outliers, schema drift, and domain-specific risks
- supports multiple vertical modes:
  - GIS / Local Government
  - Public Safety
  - Utilities
  - Campus / Indoors
  - General Enterprise Data
- generates issue summaries, remediation actions, executive report text, and workflow roadmap
- includes a polished Streamlit dashboard

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Demo mode
The app includes built-in demo datasets so you can test it instantly without uploading files.
