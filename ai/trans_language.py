import requests
import json


def translate(text):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    data = {
        'i': text,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1527087647645',
        'sign': 'a7d7f3b7f7d9f7d9f7d9f7d9f7d9f7d9',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
    }
    response = requests.post(url, headers=headers, data=data)
    result = json.loads(response.text)
    return result['translateResult'][0][0]['tgt']
