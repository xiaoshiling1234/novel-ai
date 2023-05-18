import random
import re
from transformers import pipeline, set_seed

gpt2_pipe = pipeline('text-generation', model='Gustavosta/MagicPrompt-Stable-Diffusion', tokenizer='gpt2')
# 绘画关键词前缀
tag_prefix = "best quality ,masterpiece, illustration, an extremely delicate and beautiful, extremely detailed ,CG ,unity ,8k wallpaper, "
# 绘画负面通用词
negative = "NSFW,sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy,(long hair:1.4),DeepNegative,(fat:1.2),facing away, looking away,tilted head, {Multiple people}, lowres,bad anatomy,bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worstquality, low quality, normal quality,jpegartifacts,signature, watermark, username,blurry,bad feet,cropped,poorly drawn hands,poorly drawn face,mutation,deformed,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,extra fingers,fewer digits,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,missing legs,extra digit, extra arms, extra leg, extra foot,"


def generate(starting_text):
    seed = random.randint(100, 1000000)
    set_seed(seed)

    response = gpt2_pipe(starting_text, max_length=(len(starting_text) + random.randint(60, 90)),
                         num_return_sequences=1)
    response_list = []
    for x in response:
        resp = x['generated_text'].strip()
        if resp != starting_text and len(resp) > (len(starting_text) + 4) and resp.endswith((":", "-", "—")) is False:
            response_list.append(resp + '\n')

    response_end = "\n".join(response_list)
    response_end = re.sub('[^ ]+\.[^ ]+', '', response_end)
    response_end = response_end.replace("<", "").replace(">", "")

    if response_end != "":
        return response_end + tag_prefix, negative

    return "", negative
