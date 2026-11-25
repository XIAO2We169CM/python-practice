#import requests

#def get_mes(url):
 #   try:
  #      r = requests.get(url, timeout=10)
   # except requests.exceptions.RequestException:
    #    print("连不上 MES，检查服务器有没有开")
     #   return None

    #if r.status_code != 200:
     #   print("取数失败，状态码", r.status_code)
      #  return None

    #return r.json()

#url = "https://api.github.com/repos/XIAO2We169CM/python-practice"
#info = get_mes(url)

#url = "https://api.github.com/repos/XIAO2We169CM/python-practice"
#r = requests.get(url, timeout=10)
#print("状态码", r.status_code)
#info = r.json()
#print("仓库名", info["name"])
#print("公开吗", info["visibility"])
#print("描述", info["description"])
#print("标签", info["topics"])

#if info is not None:
 #   print("仓库名", info["name"])
  #  print("公开吗", info["visibility"])
   # print("描述", info["description"])
    #print("标签", info["topics"])

import requests

def get_mes(url):
    try:
        r = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        print("连不上 MES，检查服务器有没有开")
        return None
    if r.status_code != 200:
        print("取数失败，状态码", r.status_code)
        return None
    return r.json()

urls = ["http://127.0.0.1:8000/mes_today.json",
        "http://127.0.0.1:8000/mes_today2.json",
        "http://127.0.0.1:8001/mes_today.json"]
for url in urls:
    data = get_mes(url)
    if data is not None:
        print("取到", len(data["记录"]), "条")