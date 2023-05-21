import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models
from common_config import *


def cn_trans_to_en(text):
    try:
        cred = credential.Credential(TCLOUD_SECRET_ID, TCLOUD_SECRET_KEY)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        http_profile = HttpProfile()
        http_profile.endpoint = "tmt.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = tmt_client.TmtClient(cred, "ap-beijing", client_profile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.TextTranslateRequest()
        params = {
            "SourceText": text,
            "Source": "zh",
            "Target": "en",
            "ProjectId": 1317687480
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个TextTranslateResponse的实例，与请求对象对应
        resp = client.TextTranslate(req)
        # 输出json格式的字符串回包
        return resp.TargetText

    except TencentCloudSDKException as err:
        print(err)


if __name__ == '__main__':
    cn_trans_to_en("西游记中竟然有如此低级的漏洞")
