🛡️ UX-SRS Sentinel: Neural-Heuristic Integration Model (NHIM)

Author: Gowtham P
Role: Multidisciplinary Researcher & Systems Designer
Project Timeline: < 24 Hours (Rapid Prototype Sprint)
Core Domain: UX Research | AI Architecture | Cybersecurity Systems

📌 Executive Summary

The UX-SRS Sentinel is not just another sentiment analyzer. It is a specialized Hybrid Intelligence System designed to bridge the gap between raw user data and actionable design strategy.

In a single day, I have engineered a pipeline that takes unstructured human feedback and filters it through a dual-layer process: Neural Interpretation (contextual understanding) and Heuristic Logic (industry-specific risk assessment). This tool allows stakeholders to instantly quantify the "Resonance" of their product—identifying if a user is simply frustrated or if there is a systemic security/usability failure.

🧠 The Architecture: What is happening under the hood?

1. The Neural Layer (The "Brain")
    I chose DistilBERT (a distilled version of the BERT Transformer) over simpler models like VADER or Naive Bayes.
   Why? Traditional models look at words in isolation. DistilBERT understands context. It knows the difference between "The system is down" (Negative) and "I am down to try this new feature" (Positive).
   Performance: It provides 90%+ accuracy on linguistic nuance, which is mandatory for high-level research.

3. The Heuristic Layer (The "Expert")
   While the AI handles the "vibe," my custom-coded logic handles the meaning. I built a proprietary filter that scans for specific UX Friction Points and Cybersecurity Red Flags. This turns a generic "Negative" result into a specific "Security Alert."

📐 The Mathematics of ResonanceTo provide stakeholders with a single, clear number, I developed the Resonance Score ($R_{score}$). We don't just look at sentiment; we look at the weight of the friction.
The model calculates impact using this formula:
$$R_{score} = (S \times w_s) - \sum (f \cdot 0.15)$$

Where:
$S$: The Neural Confidence score ($0.0$ to $1.0$).
$w_s$: The Sentiment Direction ($1$ for Positive, $-1$ for Negative).
$f$: The count of identified friction/security triggers.
$0.15$: The penalty constant for each identified system failure.

Why this math? It ensures that a "Positive" review that still mentions a "security" concern gets a lower score, correctly alerting the team that something is wrong despite the happy tone.

🛠️ Tech Stack & Implementation
Language: Python 3.10
Framework: Streamlit (For professional, code-hidden deployment).
NLP Engine: Hugging Face Transformers (DistilBERT).
Logic Engine: Proprietary Python Heuristics.

⚖️ Problem Framing: What this solves (and what it doesn't)

Problems Solved:
Cognitive Overload: Automates the reading of thousands of reviews so researchers can focus on fixing problems, not finding them.
Subjectivity: Replaces "I think the users are unhappy" with "The Resonance Score is -0.45 due to 3 login-related friction points".
Speed to Insight: Built and deployed in one day, moving from raw data to a live URL.

Limitations (Current Scope):
Deep Sarcasm: While DistilBERT is good, extreme sarcasm (e.g., "Oh great, another update that breaks everything, I love it so much") can still occasionally confuse the model.
Multilingualism: This version is optimized for English-language feedback.

🤝 Collaborative Origins & Intellectual Property

This project was architected and implemented by me, Gowtham, in a high-speed research sprint.
I utilized AI as a high-level collaborator to accelerate the development process. The AI served as a "Technical Peer"—assisting in debugging complex deployment errors, optimizing the math for the Resonance Score, and ensuring the code adhered to production-grade standards. While the AI provided the "scaffolding" and error-correction, the system design, heuristic logic, and multidisciplinary integration are the results of my specific research intent.

This is a human-led, AI-accelerated system.

🚀 How to Run

For stakeholders: Simply access the live URL provided in the repository description. No code setup is required on your end. The backend is fully encapsulated to ensure data integrity and IP protection.

© 2026 Gowtham P. All rights reserved. Registered under Neural-Heuristic Integration Model (NHIM) research.
