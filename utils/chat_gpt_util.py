# -*- coding: utf-8 -*-
from common_config import *


def api_2D_openai_chat(prompt, model="gpt-3.5-turbo", role="user"):
    import requests

    url = API_2D_OPENAI_CHAT_URL
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_2D_FORWARD_KEY
    }

    data = {
        "model": model,
        "messages": [{"role": role, "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()


def chat_model_prompt_1(prompt):
    prompt_model = f"用英文给我的文案写一句镜头描述,{prompt},格式是（镜头画面细节）+故事内容的画面描述"
    res = api_2D_openai_chat(prompt_model)
    describe = res['choices'][0]['message']['content']
    print("prompt:{}\ndescribe:{}".format(prompt, describe))
    return res['choices'][0]['message']['content']

# if __name__ == '__main__':
#     response = chat_model_prompt_1(
#         "首先根据小说中的说法，师徒五人取经共用14年，在凡人看来，这个过程简直太漫长了，可对于那帮神仙来说，一共也才过了两周的时间")
#     print(response)
#     print(response['choices'][0]['message']['content'])
