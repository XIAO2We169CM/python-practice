import requests, json

key = open(r"E:\我的密钥\deepseek.txt", encoding="utf-8").read().strip()
url = "https://api.deepseek.com/chat/completions"
headers = {"Authorization": "Bearer " + key}

system = """你是注塑车间的质检记录员。把用户的一句话整理成 json，只输出 json。
格式样例：
{"机台": "注塑5号", "缺陷": "飞边", "数量": 8}
数量必须是数字；没有缺陷时，缺陷写"无"，数量写 0。"""

text = "今天下午注塑3号机出了12个缩痕，师傅说保压时间可能短了"
body = {
    "model": "deepseek-flash",
    "messages": [
        {"role": "system", "content": system},
        {"role": "user", "content": text}
    ],
    "thinking": {"type": "disabled"},
    "response_format": {"type": "json_object"},
    "max_tokens": 200
}

r = requests.post(url, headers=headers, json=body, timeout=60)
content = r.json()["choices"][0]["message"]["content"]
print("结束原因：", r.json()["choices"][0]["finish_reason"])
print("AI 原样回的：", content)
print("变之前：", type(content))

d = json.loads(content)
print("变之后：", type(d))
print("机台：", d["机台"])
print("缺陷：", d["缺陷"])
if d["数量"] > 10:
    print("超过 10 个，通知班长")