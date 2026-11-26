import requests, json

key = open(r"E:\我的密钥\deepseek.txt", encoding="utf-8").read().strip()
url = "https://api.deepseek.com/chat/completions"
headers = {"Authorization": "Bearer " + key}
body = {
    "model": "deepseek-flash",
    "messages": [
        {"role": "system", "content": "你是注塑车间的质量工程师。"},
        {"role": "user", "content": "注塑件出现缩痕，列出 3 个常见原因。"}
    ],
    "thinking": {"type": "disabled"},
    "stream": True
}

r = requests.post(url, headers=headers, json=body, stream=True, timeout=60)
full = ""
for line in r.iter_lines():
    if not line:
        continue
    line = line.decode("utf-8")
    if not line.startswith("data: "):
        continue
    text = line[6:]
    if text == "[DONE]":
        break
    d = json.loads(text)
    piece = d["choices"][0]["delta"].get("content")
    if piece:
        #print(piece)
        print(piece, end="", flush=True)
        full = full + piece
print()
print("一共", len(full), "个字")