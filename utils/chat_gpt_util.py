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

    response = requests.post(url, headers=headers, json=data, timeout=600)
    return response.json()


def openai_chat(prompt, model="gpt-3.5-turbo", role="user"):
    import requests

    url = OPENAI_CHAT_URL
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + OPEN_AI_SECRET_KEY
    }

    data = {
        "model": model,
        "messages": [{"role": role, "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data, timeout=600)
    return response.json()


def chat_model_prompt_1(prompt):
    prompt_model = f"用英文给我的文案写一句镜头描述,{prompt},格式是（镜头画面细节）+故事内容的画面描述"
    # res = openai_chat(prompt_model)
    res = api_2D_openai_chat(prompt_model)
    describe = res['choices'][0]['message']['content']
    print("prompt:{}\ndescribe:{}".format(prompt, describe))
    return res['choices'][0]['message']['content']


def split_sentences(prompt):
    prompt_model = f"帮我将故事重新断句,每句话尽量长一点，我希望每一行对应一个有意义的画面。{prompt}"
    # res = openai_chat(prompt_model)
    res = api_2D_openai_chat(prompt_model)
    print(res)
    return res['choices'][0]['message']['content']
