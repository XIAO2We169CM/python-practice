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
data = r.json()
print(data["choices"][0]["message"]["content"])

IN_PRICE = 2     # 输入：每百万 token 2 元（flash 高峰价）
OUT_PRICE = 8    # 输出：每百万 token 8 元

u = data["usage"]
inp = u["prompt_tokens"]
out = u["completion_tokens"]
yuan = inp / 1000000 * IN_PRICE + out / 1000000 * OUT_PRICE
print("输入", inp, "输出", out, "合计", u["total_tokens"])
print("这一次", round(yuan, 6), "元")
print("每天 200 次，一个月", round(yuan * 200 * 30, 2), "元")