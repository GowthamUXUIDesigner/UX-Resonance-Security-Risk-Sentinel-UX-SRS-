import streamlit as st
import pandas as pd
from transformers import pipeline
import re

# ---------------------------------------------------------
# CACHING ENGINE: This is the "Professional" way to load AI
# It prevents the app from re-loading the model on every click.
# ---------------------------------------------------------
@st.cache_resource
def load_engine():
    # Progress bar for visual feedback
    with st.spinner("🤖 Initializing Neural Engine (DistilBERT)..."):
        return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Initialize the model
try:
    analyzer = load_engine()
except Exception as e:
    st.error("Engine Initialization Failed. Please check internet connectivity.")

def detect_ux_friction(text):
    friction_keywords = ['confusing', 'slow', 'crash', 'difficult', 'hidden', 'hard to find', 'cluttered']
    security_keywords = ['password', 'login', 'leak', 'scam', 'unauthorized', 'privacy', 'hacked']
    found_friction = [word for word in friction_keywords if word in text.lower()]
    found_security = [word for word in security_keywords if word in text.lower()]
    return found_friction, found_security

# UI LAYOUT
st.set_page_config(page_title="Gowtham | UX-SRS Sentinel", page_icon="🛡️")

st.title("🛡️ UX Resonance & Security Risk Sentinel (UX-SRS)")
st.caption("Developed by Gowtham • Multidisciplinary Systems Researcher")

user_input = st.text_area("Analyze User Feedback:", height=150, placeholder="Paste user reviews or interview notes here...")

if st.button("Generate Intelligence Report"):
    if user_input:
        res = analyzer(user_input)[0]
        friction, security = detect_ux_friction(user_input)
        
        # Dashboard Grid
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Sentiment Score", res['label'], f"{res['score']:.2%}")
        with c2:
            st.metric("Friction Points", len(friction))
        with c3:
            risk = "CRITICAL" if security else "STABLE"
            st.metric("Risk Status", risk)

        # Stakeholder Summary
        st.subheader("Analysis Summary")
        if res['label'] == "NEGATIVE":
            st.error(f"High Friction Detected. Specific triggers: {', '.join(friction) if friction else 'General Dissatisfaction'}")
        else:
            st.success("Positive user resonance detected. Current design patterns are effective.")
