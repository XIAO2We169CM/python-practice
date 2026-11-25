import requests

key = open(r"E:\我的密钥\deepseek.txt", encoding="utf-8").read().strip()

r = requests.get("https://api.deepseek.com/user/balance",
                 headers={"Authorization": "Bearer " + key}, timeout=30)
print("状态码", r.status_code)
data = r.json()
print("能用吗", data["is_available"])
info = data["balance_infos"][0]
print("余额", info["total_balance"], info["currency"])