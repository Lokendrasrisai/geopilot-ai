VERTICAL_RULES = {
    "GIS / Local Government": {
        "critical_fields": ["asset_id", "latitude", "longitude", "status"],
        "recommended_fields": ["inspection_date", "asset_type", "priority", "jurisdiction"],
        "high_risk_terms": ["deprecated", "unknown", "tbd", "na"],
        "workflow_focus": [
            "schema validation",
            "coordinate integrity checks",
            "asset lifecycle normalization",
            "inspection readiness review",
            "handoff report generation"
        ]
    },
    "Public Safety": {
        "critical_fields": ["address_id", "latitude", "longitude", "status"],
        "recommended_fields": ["zone", "response_area", "street_name", "updated_at"],
        "high_risk_terms": ["unknown", "invalid", "pending", "missing"],
        "workflow_focus": [
            "location accuracy review",
            "address completeness checks",
            "response boundary reconciliation",
            "stale-record escalation",
            "executive risk summary"
        ]
    },
    "Utilities": {
        "critical_fields": ["asset_id", "status", "asset_type"],
        "recommended_fields": ["inspection_date", "installation_year", "condition_score", "feeder"],
        "high_risk_terms": ["unknown", "inactive", "tbd", "null"],
        "workflow_focus": [
            "network asset validation",
            "condition-score auditing",
            "missing lifecycle metadata repair",
            "migration readiness scoring",
            "automation candidate generation"
        ]
    },
    "Campus / Indoors": {
        "critical_fields": ["space_id", "building", "floor", "status"],
        "recommended_fields": ["category", "capacity", "updated_at", "accessible"],
        "high_risk_terms": ["unknown", "temp", "none"],
        "workflow_focus": [
            "space inventory validation",
            "floor-level consistency checks",
            "indoor routing readiness review",
            "stale-record cleanup",
            "stakeholder summary"
        ]
    },
    "General Enterprise Data": {
        "critical_fields": ["record_id", "status"],
        "recommended_fields": ["created_at", "updated_at", "owner", "category"],
        "high_risk_terms": ["unknown", "tbd", "na", "null"],
        "workflow_focus": [
            "schema health review",
            "missing value remediation",
            "duplicate resolution",
            "owner-field normalization",
            "report packaging"
        ]
    }
}
