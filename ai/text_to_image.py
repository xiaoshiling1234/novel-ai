import json

import requests

from common_config import *
from utils.img_util import save_sd_img


def text_to_image(prompt, negative_prompt, out_path, steps=SD_DEFAULT_STEPS, batch_size=SD_DEFAULT_BATCH_SIZE):
    url = SD_TXT_TO_IMG_URL
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "batch_size": batch_size,
        "n_iter": SD_DEFAULT_N_ITER,
        "steps": steps,
        "width": SD_DEFAULT_WIDTH,
        "height": SD_DEFAULT_HEIGHT,
        "negative_prompt": negative_prompt,
        "cfg_scale": SD_CFG_SCALE,
        "enable_hr": SD_ENABLE_HR,
        "hr_scale": SD_HR_SCALE,
        "hr_upscaler": SD_HR_UPSCALER,
        "denoising_strength": SD_DENOISING_STRENGTH
    }
    res = requests.post(url, headers=headers, data=json.dumps(data))
    save_sd_img(res.json(), out_path)


# if __name__ == '__main__':
#     text_to_image(
#         "Sun WuKong watched in Heaven for more than half a month.,best quality ,masterpiece, illustration, an extremely delicate and beautiful, extremely detailed ,CG ,unity ,8k wallpaper"
#         , NEGATIVE
#         , r"D:\novel-ai\ai\out.png"
#         , steps=50)
