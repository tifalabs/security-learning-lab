url = input("Enter a URL to check: ").lower()

warnings = []

if not url.startswith("https://"):
    warnings.append("URL does not use HTTPS.")

if "@" in url:
    warnings.append("URL contains '@', which can hide the real destination.")

if "-" in url:
    warnings.append("URL contains hyphens, often used in fake domains.")

if url.count(".") > 3:
    warnings.append("URL has many dots/subdomains.")

suspicious_words = ["login", "verify", "free", "gift", "urgent", "account", "password"]

for word in suspicious_words:
    if word in url:
        warnings.append(f"URL contains suspicious word: {word}")

print("\nPhishing Checklist Result:")

if warnings:
    print("Potential warning signs found:")
    for warning in warnings:
        print(f"- {warning}")
else:
    print("No basic warning signs found. Still verify the website manually.")