import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

r=requests.get("http://example.org", proxies=proxies)
print(r.json())