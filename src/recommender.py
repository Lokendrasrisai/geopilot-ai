from src.rules import VERTICAL_RULES

def build_recommendations(audit_result: dict, vertical: str):
    summary = audit_result["summary"]
    actions = []
    risk_flags = []
    rules = VERTICAL_RULES[vertical]

    if audit_result["critical_missing_fields"]:
        actions.append("Restore or map all critical fields before downstream automation or migration.")
        risk_flags.append("Missing critical fields could block operational workflows and reduce trust in outputs.")

    if audit_result["recommended_missing_fields"]:
        actions.append("Backfill recommended fields to improve workflow richness and reporting quality.")

    if summary["duplicate_rows"] > 0:
        actions.append("Run duplicate-resolution workflow with survivorship rules and unique ID checks.")
        risk_flags.append("Duplicate records may inflate counts and create operational confusion.")

    if summary["missing_ratio_pct"] >= 10:
        actions.append("Prioritize missing-value remediation with field-level ownership and validation rules.")

    if audit_result["suspicious_terms"]:
        actions.append("Normalize placeholder terms such as unknown, tbd, na, and null using controlled vocabularies.")
        risk_flags.append("Placeholder values suggest inconsistent field-entry practices or legacy migration artifacts.")

    if audit_result["numeric_outliers"]:
        actions.append("Review numeric outliers for unit mismatch, sensor error, or malformed imports.")

    if audit_result["coordinate_flags"]:
        actions.append("Validate coordinate integrity and coordinate system assumptions before any mapping workflows.")
        risk_flags.append("Invalid coordinates can break GIS, routing, and location-critical decisions.")

    if summary["staleness_signal"] > 0:
        actions.append("Audit record freshness and trigger stale-data review for operationally sensitive records.")

    if not actions:
        actions.append("Dataset appears structurally healthy. Start with light validation, baseline reporting, and monitoring.")

    roadmap = [
        f"Run {rules['workflow_focus'][0]} first.",
        f"Then execute {rules['workflow_focus'][1]}.",
        f"Prioritize {rules['workflow_focus'][2]} for the highest-risk fields.",
        f"Package findings into {rules['workflow_focus'][3]}.",
        f"Finish with {rules['workflow_focus'][4]}."
    ]

    automation_candidates = []
    if audit_result["critical_missing_fields"] or audit_result["recommended_missing_fields"]:
        automation_candidates.append("schema-mapping and field normalization script")
    if summary["duplicate_rows"] > 0:
        automation_candidates.append("duplicate-detection and survivorship pipeline")
    if audit_result["coordinate_flags"]:
        automation_candidates.append("coordinate validation and repair script")
    if audit_result["suspicious_terms"]:
        automation_candidates.append("controlled-vocabulary standardization job")
    if not automation_candidates:
        automation_candidates.append("scheduled health-check reporting workflow")

    return {
        "actions": actions[:6],
        "risk_flags": risk_flags[:5] if risk_flags else ["No major structural blockers detected. Continue with controlled validation."],
        "roadmap": roadmap,
        "automation_candidates": automation_candidates,
    }
