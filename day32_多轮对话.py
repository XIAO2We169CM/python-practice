import requests

key = open(r"E:\我的密钥\deepseek.txt", encoding="utf-8").read().strip()
url = "https://api.deepseek.com/chat/completions"
headers = {"Authorization": "Bearer " + key}

messages = [
    {"role": "system", "content": "你是注塑车间的质量工程师，回答简短，不超过 60 字。"}
]

while True:
    q = input("你：")
    if q == "q":
        break
    messages.append({"role": "user", "content": q})
    body = {"model": "deepseek-flash", "messages": messages,
            "thinking": {"type": "disabled"}}
    r = requests.post(url, headers=headers, json=body, timeout=60)
    data = r.json()
    a = data["choices"][0]["message"]["content"]
    print("AI：", a)
    messages.append({"role": "assistant", "content": a})
    print("（这次输入", data["usage"]["prompt_tokens"], "token，messages 现在", len(messages), "条）")