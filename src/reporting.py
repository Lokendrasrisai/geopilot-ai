def build_executive_report(vertical: str, audit_result: dict, recs: dict) -> str:
    summary = audit_result["summary"]
    return f'''
GeoPilot AI Executive Summary

Vertical:
{vertical}

Operational Readiness Score:
{summary["readiness_score"]}/100

Risk Severity:
{summary["severity"]}

What this means:
The uploaded dataset was audited for structure, completeness, duplicates, suspicious placeholders, outlier signals, and domain-specific readiness indicators. The current readiness level suggests that this dataset {"can move forward with light governance" if summary["readiness_score"] >= 80 else "requires targeted remediation before reliable downstream use"}.

Priority actions:
1. {recs["actions"][0] if len(recs["actions"]) > 0 else "Proceed with standard validation."}
2. {recs["actions"][1] if len(recs["actions"]) > 1 else "Document issues and assign ownership."}
3. {recs["actions"][2] if len(recs["actions"]) > 2 else "Package findings into a stakeholder report."}

Operational risk:
{recs["risk_flags"][0]}

Recommended next workflow:
- {recs["roadmap"][0]}
- {recs["roadmap"][1]}
- {recs["roadmap"][2]}

Automation opportunity:
{", ".join(recs["automation_candidates"])}
'''.strip()
