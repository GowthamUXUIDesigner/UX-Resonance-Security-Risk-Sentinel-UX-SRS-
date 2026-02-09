import streamlit as st
import pandas as pd
from transformers import pipeline
import plotly.express as px
import re

# --- SYSTEM INITIALIZATION ---
st.set_page_config(page_title="Gowtham | UX-SRS Sentinel", page_icon="🛡️", layout="wide")

@st.cache_resource
def load_engine():
    with st.spinner("🤖 Initializing Neural Engine (DistilBERT)..."):
        return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

analyzer = load_engine()

def calculate_resonance(text, sentiment_label, confidence):
    """
    Mathematical Model for User Resonance
    R = (Confidence * Direction) - (Friction * 0.15)
    """
    friction_keywords = ['confusing', 'slow', 'crash', 'difficult', 'hidden', 'hard to find', 'cluttered']
    security_keywords = ['password', 'login', 'leak', 'scam', 'unauthorized', 'privacy', 'hacked']
    
    f_found = [w for w in friction_keywords if w in text.lower()]
    s_found = [w for w in security_keywords if w in text.lower()]
    
    # Logic: Negative sentiment is -1, Positive is 1
    direction = 1 if sentiment_label == "POSITIVE" else -1
    score = (confidence * direction) - (len(f_found) * 0.15)
    
    return round(score, 3), f_found, s_found

# --- UI LAYOUT ---
st.title("🛡️ UX Resonance & Security Sentinel (UX-SRS)")
st.caption("Strategic Intelligence System • Multidisciplinary Systems Research")

# Tabs for Stakeholder Flexibility
tab1, tab2 = st.tabs(["Single Entry Triage", "Batch Intelligence (CSV)"])

with tab1:
    user_input = st.text_area("Analyze Individual Feedback:", placeholder="Enter user quote...")
    if st.button("Generate Triage Report"):
        if user_input:
            res = analyzer(user_input)[0]
            r_score, friction, security = calculate_resonance(user_input, res['label'], res['score'])
            
            # Metric Row
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Sentiment", res['label'])
            c2.metric("Neural Confidence", f"{res['score']:.2%}")
            c3.metric("Friction Count", len(friction))
            c4.metric("Resonance Score", r_score)
            
            if security: st.error(f"🚨 SECURITY RISK DETECTED: {', '.join(security)}")

with tab2:
    st.subheader("Enterprise Batch Processing")
    uploaded_file = st.file_uploader("Upload User Research CSV (First column must be text)", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if st.button("Run Batch Analysis"):
            with st.spinner("Analyzing high-dimensional data..."):
                # Analysis Logic
                df['Analysis'] = df.iloc[:, 0].apply(lambda x: analyzer(str(x)[:512])[0])
                df['Sentiment'] = df['Analysis'].apply(lambda x: x['label'])
                df['Confidence'] = df['Analysis'].apply(lambda x: x['score'])
                
                # Visual Analytics
                st.divider()
                col_a, col_b = st.columns([1, 2])
                
                with col_a:
                    st.write("### Distribution")
                    fig = px.pie(df, names='Sentiment', hole=0.4, color_discrete_map={'POSITIVE':'#00cc96', 'NEGATIVE':'#ef553b'})
                    st.plotly_chart(fig, use_container_width=True)
                
                with col_b:
                    st.write("### Raw Intelligence Data")
                    st.dataframe(df[['Sentiment', 'Confidence', df.columns[0]]], height=300)
                
                # Download Result
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Download Analyzed Dataset", data=csv, file_name="UX_SRS_Report.csv")

st.sidebar.markdown("---")
st.sidebar.write("**System Status:** Operational")
st.sidebar.caption("© 2026 Gowtham | Neural-Heuristic Integration")
