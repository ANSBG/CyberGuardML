# CyberGuardML 🚨
**Hybrid Intrusion Detection System (Machine Learning & Cybersecurity)**

CyberGuardML is an **academic/personal project** that demonstrates how machine learning can be applied to **network intrusion detection**, inspired by real-world **Security Operations Center (SOC)** workflows.

The project goes beyond model training by focusing on **risk prioritization, explainability, and operational usability**, making it suitable as a **portfolio project** for Data Science and Cybersecurity roles.

---

## 🔍 Project Overview

CyberGuardML implements a **hybrid intrusion detection architecture** combining supervised and unsupervised learning:

- **XGBoost** for detecting known attack patterns  
- **Isolation Forest** for identifying zero-day and anomalous behaviors  
- **SOC-style risk scoring (0–100)** with alert prioritization (**P1 / P2 / P3**)  
- **Model explainability with SHAP** to interpret and justify alerts  
- An **interactive SOC dashboard** built with **Streamlit**

---

## 🧠 System Architecture

1. Network traffic ingestion  
2. Data preprocessing and feature engineering  
3. Known attack detection using XGBoost  
4. Zero-day anomaly detection using Isolation Forest  
5. Risk score computation and alert prioritization  
6. Explainability using SHAP  
7. Visualization and analysis via SOC dashboard  

---

## 📊 Dataset

- **CIC-IDS2017** (network traffic intrusion detection dataset)
- Due to size constraints, **only a small processed sample** is included in this repository for demonstration purposes.
- Raw datasets are intentionally excluded.

---

## 📈 SOC Dashboard (Streamlit)

The Streamlit dashboard enables:
- Monitoring alert distribution by priority (P1 / P2 / P3)
- Filtering alerts by risk score
- Inspecting high-risk security events
- Exporting filtered alerts for further analysis

## 🛠️ Tech Stack

Python

Pandas, NumPy

Scikit-learn

XGBoost

Isolation Forest

SHAP (Explainable AI)

Streamlit

## 👤 Author

ANAS BOUGADOUM
Master’s Student — Data Science & Cybersecurity