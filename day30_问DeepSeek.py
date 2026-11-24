import requests

key = open(r"E:\我的密钥\deepseek.txt", encoding="utf-8").read().strip()

url = "https://api.deepseek.com/chat/completions"
headers = {"Authorization": "Bearer " + key}
body = {
    "model": "deepseek-flash",
    "messages": [
        {"role": "system", "content": "你是注塑车间的质量工程师，回答简短，不超过 60 字。"},
        {"role": "user", "content": "今天注塑3号不良率 3.00%，注塑1号 1.95%，注塑2号 0.90%。给班组长一句提醒。"}
    ],
    "thinking": {"type": "disabled"}
}

r = requests.post(url, headers=headers, json=body, timeout=60)
print("状态码", r.status_code)
data = r.json()
print(data["choices"][0]["message"]["content"])
print("用了", data["usage"]["total_tokens"], "个 token")