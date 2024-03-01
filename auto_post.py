import requests
import json
import time


url = 'https://wxapp-daidai.uboxs.com/timeline/search'
headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555",
           "referer":"https://servicewechat.com/wxcea4b3296961e4f2/141/page-frame.html"
           }

def work():
    with open('data.json') as f:
        data = json.load(f)

    Data = json.dumps(data)

    req = requests.post(url, data=Data, headers=headers, verify=False)

    print(req.text)

if __name__ == "__main__":
    work()