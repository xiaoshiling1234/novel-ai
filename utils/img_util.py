import os
import io
import base64
from PIL import Image


# 存储stable diffision返回的图片
def save_sd_img(res, out_path):
    directory = os.path.dirname(out_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in res['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))
        image.save(out_path)
