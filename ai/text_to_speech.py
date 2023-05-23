import json
import uuid

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.tts.v20190823 import tts_client, models

from common_config import *
from utils import wav_util


def text_to_wav(Text, output_file):
    try:
        cred = credential.Credential(TCLOUD_SECRET_ID, TCLOUD_SECRET_KEY)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tts.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = tts_client.TtsClient(cred, "ap-beijing", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.TextToVoiceRequest()
        params = {
            "Text": Text,
            "SessionId": "novelai",
            "Volume": 0,
            "Speed": 0,
            "ProjectId": 0,
            "ModelType": 1,
            "VoiceType": 101054,
            "PrimaryLanguage": 1,
            "SampleRate": 16000,
            "Codec": "wav",
            "EnableSubtitle": False,
            "SegmentRate": 0,
            "EmotionCategory": "story",
            "EmotionIntensity": 100
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个TextToVoiceResponse的实例，与请求对象对应
        resp = client.TextToVoice(req)

        wav_util.write_wav_from_json(resp.Audio, output_file)

    except TencentCloudSDKException as err:
        print(err)
