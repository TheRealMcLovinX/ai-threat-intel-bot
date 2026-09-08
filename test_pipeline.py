from backend.threat_intel import check_ip
from ai_module.analyzer import analyze_threat

ip = "185.220.101.42"

threat_data = check_ip(ip)

result = analyze_threat(threat_data)

print("IP:", result["ip"])
print("Risk", result["risk"])
print("Detection:", result["detection_percentage"], "%")
print("Country:", result["country"])
print("Tags:", result["tags"])
