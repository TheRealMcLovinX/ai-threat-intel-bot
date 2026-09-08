def analyze_threat(threat_data):
    malicious = threat_data["malicious"]
    total = threat_data["total"]

    detection_percentage = (malicious / total) * 100

    if detection_percentage >= 20:
        risk = "HIGH"
    elif detection_percentage >= 5:
        risk = "MEDIUM"
    else:
        risk = "LOW"
    result = {
        "ip": threat_data["ip"],
        "risk": risk,
        "detection_percentage": detection_percentage,
        "country": threat_data["country"],
        "tags": threat_data["tags"]
    }

    return result
