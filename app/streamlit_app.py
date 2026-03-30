import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

import pandas as pd
import streamlit as st

from src.demo_data import get_demo_dataset
from src.auditor import audit_dataframe
from src.recommender import build_recommendations
from src.reporting import build_executive_report
from src.rules import VERTICAL_RULES
from src.ui_helpers import inject_css

st.set_page_config(page_title="GeoPilot AI", layout="wide")
st.markdown(inject_css(), unsafe_allow_html=True)

st.markdown(
    '''
    <div class="hero">
      <h1>GeoPilot AI</h1>
      <p>AI Copilot for Data Quality, Workflow Automation, and Operational Readiness. Upload a dataset or use demo mode to audit health, score readiness, identify operational blockers, and generate a remediation plan.</p>
    </div>
    ''',
    unsafe_allow_html=True
)

left, right = st.columns([1.05, 0.95])

with left:
    vertical = st.selectbox("Choose operating vertical", list(VERTICAL_RULES.keys()))
    input_mode = st.radio("Input mode", ["Use Demo Dataset", "Upload CSV"], horizontal=True)
    uploaded = None
    if input_mode == "Upload CSV":
        uploaded = st.file_uploader("Upload a CSV dataset", type=["csv"])

    run = st.button("Run GeoPilot Audit", use_container_width=True)

with right:
    st.markdown(
        '''
        <div class="glass">
          <div class="section-title">What GeoPilot evaluates</div>
          Schema health, missingness, duplicate risk, placeholder-value drift, outlier patterns, domain-specific operational blockers, and workflow readiness.
        </div>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        '''
        <div class="glass">
          <div class="section-title">Best-fit use cases</div>
          Managed GIS services, public-safety data validation, utility readiness audits, migration assessments, campus/indoor data reviews, and enterprise data-governance workflows.
        </div>
        ''',
        unsafe_allow_html=True
    )

if run:
    if input_mode == "Use Demo Dataset":
        df = get_demo_dataset(vertical)
    else:
        if uploaded is None:
            st.warning("Please upload a CSV file first.")
            st.stop()
        df = pd.read_csv(uploaded)

    audit_result = audit_dataframe(df, vertical)
    recs = build_recommendations(audit_result, vertical)
    report_text = build_executive_report(vertical, audit_result, recs)
    summary = audit_result["summary"]

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Readiness Score", summary["readiness_score"])
    m2.metric("Severity", summary["severity"])
    m3.metric("Missing Cells", summary["missing_cells"])
    m4.metric("Duplicate Rows", summary["duplicate_rows"])

    col1, col2 = st.columns([1.2, 0.8])

    with col2:
        st.markdown("### Executive Signal")
        st.markdown(
            f'''
            <div class="glass">
              <div class="score-pill">Operational Readiness: {summary["readiness_score"]}/100</div>
              <div class="section-title">Severity</div>
              {summary["severity"]}
            </div>
            ''',
            unsafe_allow_html=True
        )
        st.markdown("### Automation Candidates")
        for item in recs["automation_candidates"]:
            st.write(f"- {item}")

        st.markdown("### Risk Flags")
        for item in recs["risk_flags"]:
            st.write(f"- {item}")

    with col1:
        st.markdown("### Dataset Preview")
        st.dataframe(df.head(20), use_container_width=True, hide_index=True)

        st.markdown("### Recommended Actions")
        for item in recs["actions"]:
            st.write(f"- {item}")

    st.markdown("### Issue Breakdown")
    a, b = st.columns(2)

    with a:
        st.markdown("#### Missing / Schema Health")
        st.write(f"Critical missing fields: {', '.join(audit_result['critical_missing_fields']) if audit_result['critical_missing_fields'] else 'None'}")
        st.write(f"Recommended missing fields: {', '.join(audit_result['recommended_missing_fields']) if audit_result['recommended_missing_fields'] else 'None'}")
        if audit_result["high_missing_columns"]:
            st.dataframe(
                pd.DataFrame({
                    "column": list(audit_result["high_missing_columns"].keys()),
                    "missing_pct": list(audit_result["high_missing_columns"].values())
                }),
                use_container_width=True,
                hide_index=True
            )

    with b:
        st.markdown("#### Data Quality Signals")
        if audit_result["suspicious_terms"]:
            st.dataframe(pd.DataFrame(audit_result["suspicious_terms"]), use_container_width=True, hide_index=True)
        else:
            st.write("No suspicious placeholder terms detected.")
        if audit_result["coordinate_flags"]:
            st.write(audit_result["coordinate_flags"])
        if audit_result["numeric_outliers"]:
            st.dataframe(pd.DataFrame(audit_result["numeric_outliers"]), use_container_width=True, hide_index=True)

    st.markdown("### Workflow Roadmap")
    for step in recs["roadmap"]:
        st.write(f"- {step}")

    st.markdown("### Executive Report")
    st.code(report_text, language="text")

    st.download_button(
        "Download Executive Report",
        data=report_text,
        file_name="geopilot_executive_report.txt",
        mime="text/plain",
        use_container_width=True
    )
else:
    st.info("Choose a vertical, use demo data or upload a CSV, then run the GeoPilot audit.")
