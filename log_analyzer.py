failed_logins = {}

with open("logs/auth.log", "r") as log_file:
    for line in log_file:
        if "Failed login attempt" in line:
            ip = line.split("from")[1].strip()
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

print("Suspicious IP addresses (2+ failed attempts):")
for ip, count in failed_logins.items():
    if count >= 2:
        print(f"{ip} -> {count} failed attempts")
