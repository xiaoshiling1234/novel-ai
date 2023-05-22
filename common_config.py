TCLOUD_APP_ID = 1317687480
TCLOUD_SECRET_ID = "AKIDEONBKYoA5oMiqtskbO1SlxyoTuBRPAoJ"
TCLOUD_SECRET_KEY = "XCnHfs398yNfllcImASjrm9MWUPNLKSJ"
WAV_CONFIG_SAMPLERATE = 16000
WAV_CONFIG_CHANNELS = 1
WAV_CONFIG_BITSPERSAMPLE = 16

SD_TXT_TO_IMG_URL = "http://region-3.seetacloud.com:12744/sdapi/v1/txt2img"
SD_DEFAULT_BATCH_SIZE = 1
SD_DEFAULT_N_ITER = 1
SD_DEFAULT_STEPS = 20
SD_DEFAULT_WIDTH = 512
SD_DEFAULT_HEIGHT = 512
SD_CFG_SCALE = 7  # classifier free guidance scale,控制模型和prompt的匹配程度，1.忽视prompt
SD_ENABLE_HR = True
SD_HR_UPSCALER = "Latent"
SD_HR_SCALE = 2
SD_DENOISING_STRENGTH = 0.7  # 仅用于latent upscalers,该参数与image-to-image含义相同，它控制在之星hires采样步骤之前添加到潜空间中的噪声，必须大于0.5，否则会尝产生模糊的图像，使用latent的好处是没有像esrgan这种一样可能引入放大伪像，sd的解码器生成图像，确保风格一致，缺点是在一定程度改变图像，这取决于去噪强度的值

TASK_PATH = "data/input/tasklist/tasklist.xlsx"
OUT_ROOT_DIR = "data/output/"

# 免费翻译休眠时长
TRANS_SLEEP_TIME = 0.1

# 生成提示词最大重试次数
MAX_RETRY_TIMES = 10

# 绘画关键词前缀
TAG_PREFIX = "best quality ,masterpiece, illustration, an extremely delicate and beautiful, extremely detailed ,CG ,unity ,8k wallpaper, "
# 绘画负面通用词
NEGATIVE = "NSFW,sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy,(long hair:1.4),DeepNegative,(fat:1.2),facing away, looking away,tilted head, {Multiple people}, lowres,bad anatomy,bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worstquality, low quality, normal quality,jpegartifacts,signature, watermark, username,blurry,bad feet,cropped,poorly drawn hands,poorly drawn face,mutation,deformed,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,extra fingers,fewer digits,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,missing legs,extra digit, extra arms, extra leg, extra foot,"
# AI绘画并发度
MAX_WORKERS = 4

# chatgpt
API_2D_OPENAI_CHAT_URL = "https://openai.api2d.net/v1/chat/completions"
API_2D_FORWARD_KEY = "fk200442-MEUXSd5vgIxgF42TJKcOlRO91EMXGHs7"
