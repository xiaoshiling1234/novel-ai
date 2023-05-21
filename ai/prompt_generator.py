import random
import re
from common_config import *
from torch.cuda import is_available
from transformers import pipeline, set_seed

if is_available():
    gpt2_pipe = pipeline('text-generation', model='Gustavosta/MagicPrompt-Stable-Diffusion', tokenizer='gpt2', device=0)
else:
    gpt2_pipe = pipeline('text-generation', model='Gustavosta/MagicPrompt-Stable-Diffusion', tokenizer='gpt2')


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
        return TAG_PREFIX+response_end
    return ""

# if __name__ == '__main__':
#     print(generate("It's been a long process."))
