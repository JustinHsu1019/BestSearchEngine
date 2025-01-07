import requests
import json

# Java API 的 URL
api_url = "http://localhost:8080/api/search"

# 查询参数 (根据需要修改 query 内容)
query = "夜市 美食"

# 请求参数
params = {"query": query}

try:
    # 发送 GET 请求
    response = requests.get(api_url, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析并打印 JSON 响应
        result_json = response.json()
        print(json.dumps(result_json, indent=4, ensure_ascii=False))
    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
