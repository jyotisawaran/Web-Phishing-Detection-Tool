import requests

print("=" * 50)
print("      WEB PHISHING DETECTION TOOL")
print("=" * 50)

url = input("Enter Website URL (https://example.com): ")

try:
    response = requests.get(url, timeout=5)

    print("\nWebsite Status:", response.status_code)

    suspicious_keywords = [
        "login",
        "verify",
        "secure",
        "update",
        "bank",
        "account"
    ]

    score = 0

    if "@" in url:
        score += 1

    if "-" in url:
        score += 1

    if len(url) > 60:
        score += 1

    for word in suspicious_keywords:
        if word in url.lower():
            score += 1

    print("\nRisk Analysis")

    if score == 0:
        print("✅ Safe Website")

    elif score <= 2:
        print("🟡 Suspicious Website")

    else:
        print("🔴 High Phishing Risk")

except:
    print("Unable to connect to website.")