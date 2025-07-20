import streamlit as st
from analyzer import analyze_header

# Title and intro
st.set_page_config(page_title="Email Header Analyzer", page_icon="✉️")
st.title("✉️ Email Header Analyzer - Cyber Forensics Tool")
st.write("Paste your email header below to analyze and detect suspicious content.")

# Text area for input
header_input = st.text_area("Email Header", height=300, placeholder="Paste the raw email header here...")

# Analyze button
if st.button("Analyze Header"):
    if header_input.strip():
        report = analyze_header(header_input)

        st.subheader("Analysis Report")
        st.write(f"**Sender IP:** {report['ip']}")
        st.write(f"**Phishing Keywords Found:** {', '.join(report['keywords']) if report['keywords'] else 'None'}")
        st.write(f"**Result:** :red[{report['result']}]"
                 if report['result'] == "Suspicious Email" else f"**Result:** :green[{report['result']}]")
    else:
        st.warning("Please paste an email header before analyzing.")
