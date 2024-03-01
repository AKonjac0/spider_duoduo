import requests
import json
import time
import hashlib
#
token_url = 'https://wxapp-daidai.uboxs.com/timeline/search'
token_headers = {
        'Content-Type': 'application/json'
}
token_data = {
        "page": 1,
        "limit": 20
}

def generate_token(secret_key):
    timestamp = str(1709034563)  # 获取当前时间戳
    message = secret_key + timestamp  # 将密钥和时间戳拼接
    hash_object = hashlib.sha1(message.encode())  # 使用SHA-256哈希函数计算摘要
    token = hash_object.hexdigest()  # 获取摘要的十六进制表示
    return token


def get_train_token():

    post_result = requests.post(token_url, data=json.dumps(token_data), headers=token_headers, verify=False)
    print(post_result.text)
    # token_data = post_result.json()['data']['access_token']
    # return token_data


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
    print(generate_token(str(1709036136848)))