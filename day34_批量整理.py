import requests, json

key = open(r"E:\我的密钥\deepseek.txt", encoding="utf-8").read().strip()
url = "https://api.deepseek.com/chat/completions"
headers = {"Authorization": "Bearer " + key}
system = """你是注塑车间的质检记录员。把用户的一句话整理成 json，只输出 json。
格式样例：
{"机台": "注塑5号", "缺陷": "飞边", "数量": 8}
数量必须是数字；没有缺陷时，缺陷写"无"，数量写 0。"""

def parse(text):
    body = {"model": "deepseek-flash",
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": text}],
            "thinking": {"type": "disabled"},
            "response_format": {"type": "json_object"},
            "max_tokens": 200}
    r = requests.post(url, headers=headers, json=body, timeout=60)
    content = r.json()["choices"][0]["message"]["content"]
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("解析失败：", repr(content))
        return None

notes = ["注塑3号早班缩痕12个",
         "5号机飞边，挑出来7个",
         "注塑1号今天一切正常"]
total = 0
for text in notes:
    d = parse(text)
    if d is None:
        continue
    print(d["机台"], d["缺陷"], d["数量"])
    total = total + d["数量"]
print("今天不良合计", total, "个")