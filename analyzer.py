import re

# List of common phishing keywords
PHISHING_KEYWORDS = [
    "urgent", "verify your account", "password reset",
    "click here", "bank account", "suspended", "login now"
]


def extract_ip(header_text):
    """
    Extracts the first IP address found in the email header.
    """
    match = re.search(r"\[?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]?", header_text)
    return match.group(1) if match else "Not Found"


def check_phishing_keywords(header_text):
    """
    Checks if any phishing-related keywords are present in the email header.
    """
    found_keywords = [kw for kw in PHISHING_KEYWORDS if kw.lower() in header_text.lower()]
    return found_keywords


def analyze_header(header_text):
    """
    Analyzes the email header and returns a report.
    """
    ip = extract_ip(header_text)
    keywords = check_phishing_keywords(header_text)

    result = "Safe Email"
    if keywords or ip == "Not Found":
        result = "Suspicious Email"

    return {
        "ip": ip,
        "keywords": keywords,
        "result": result
    }
