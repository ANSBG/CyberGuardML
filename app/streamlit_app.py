import pandas as pd
import streamlit as st
from pathlib import Path

# =============================
# Page configuration
# =============================
st.set_page_config(
    page_title="CyberGuardML — SOC Dashboard",
    layout="wide"
)

st.title("CyberGuardML — SOC Dashboard")
st.caption(
    "Hybrid IDS: XGBoost (known attacks) + Isolation Forest (zero-day) "
    "→ Risk Score & Alert Priorities"
)

# =============================
# Load data (robust path)
# =============================
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "processed" / "soc_alerts.csv"

@st.cache_data
def load_alerts(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

alerts = load_alerts(DATA_PATH)

# =============================
# KPIs
# =============================
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total events", f"{len(alerts):,}")
c2.metric("P1 (Critical)", f"{(alerts['priority'] == 'P1').sum():,}")
c3.metric("P2 (Suspicious)", f"{(alerts['priority'] == 'P2').sum():,}")
c4.metric("P3 (Low)", f"{(alerts['priority'] == 'P3').sum():,}")

st.divider()

# =============================
# Filters
# =============================
st.subheader("Filters")

col1, col2 = st.columns(2)

with col1:
    priorities = st.multiselect(
        "Priority",
        ["P1", "P2", "P3"],
        default=["P1", "P2"]
    )

with col2:
    risk_min, risk_max = st.slider(
        "Risk score range",
        0, 100, (60, 100)
    )

filtered = alerts[
    (alerts["priority"].isin(priorities)) &
    (alerts["risk_score"] >= risk_min) &
    (alerts["risk_score"] <= risk_max)
].copy()

st.write(f"Filtered rows: **{len(filtered):,}**")

st.divider()

# =============================
# Top Risk Alerts
# =============================
st.subheader("Top Risk Alerts")

top_n = st.slider("Top N alerts", 10, 200, 50)
top_alerts = filtered.sort_values("risk_score", ascending=False).head(top_n)

st.dataframe(top_alerts, use_container_width=True)

st.divider()

# =============================
# Charts
# =============================
st.subheader("Distributions")

left, right = st.columns(2)

with left:
    st.write("Priority distribution")
    st.bar_chart(alerts["priority"].value_counts())

with right:
    st.write("Risk score distribution")

    # ✅ PERFECT bins (no Altair error)
    labels = ["0–20", "20–40", "40–60", "60–80", "80–100"]
    bins = pd.cut(
        alerts["risk_score"],
        bins=[0, 20, 40, 60, 80, 100],
        labels=labels,
        include_lowest=True
    )

    bin_counts = bins.value_counts().reindex(labels)
    st.bar_chart(bin_counts)

st.divider()

# =============================
# Download section
# =============================
st.subheader("Download filtered alerts")

csv_data = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="filtered_soc_alerts.csv",
    mime="text/csv"
)

st.success("SOC Dashboard ready ")