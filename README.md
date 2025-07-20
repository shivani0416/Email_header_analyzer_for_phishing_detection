# ✉️ Email Header Analyzer - Cyber Forensics Tool

## **Project Description**
The **Email Header Analyzer** is a Streamlit-based mini cyber forensic tool that helps detect suspicious or phishing emails by analyzing their headers.  
It extracts key forensic indicators like:
- **Sender IP address**
- **Phishing-related keywords**
- **Safe / Suspicious email status**

This project is ideal for showcasing **cyber forensics concepts** and real-world email security analysis.

---

## **Features**
- Extracts sender IP from email headers.
- Detects common phishing keywords like *"urgent"*, *"verify your account"*, etc.
- Provides a quick analysis result (Safe or Suspicious).
- User-friendly web interface built with **Streamlit**.

---

## **Installation**
1. **Clone this repository:**
   ```bash
   git clone https://github.com/shivani0416/Email_header_analyzer_for_phishing_detection.git

   cd Email_header_analyzer_for_phishing_detection

2. **Install libraries**
   pip install streamlit python-whois ipwhois tldextract dnspython

3. **How to Run**
   Run the Streamlit app with:
   streamlit run app.py

4. **Usage**
   Open any email (e.g., Gmail).
   Copy its raw header (Menu → Show Original → Copy).
   Paste it into the app and click Analyze Header.
   View the result: Sender IP, keywords found, and whether the email is suspicious.

5. **Future Enhancements**
   Add IP geolocation (track the country of the sender).
   WHOIS lookup for domain age verification.
   Advanced SPF/DKIM validation checks.

**Author Declaration**
I, shivani kawade, a student of MSc IT at Pillai College, Panvel, hereby declare that this project titled "Email Header Analyzer for phishing detection – Cyber Forensics Tool" has been developed by me as part of my academic curriculum.
While I have referred to online resources, guidance, and documentation for understanding concepts and coding techniques, the final implementation, testing, and customization of this project have been done solely by me.

This project is created for educational and research purposes only and is not intended for any malicious activity. All references, if any, have been acknowledged in the project report.
