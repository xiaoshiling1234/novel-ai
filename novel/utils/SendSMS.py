# -*- coding: UTF-8 -*-

from novel.libs.yuntongxun.CCPRestSDK import REST

accountSid = '8a216da8627648690162843e217602d5'

accountToken = ''

appId = '8a216da8627648690162843e21d002db'
serverIP = 'app.cloopen.com'

serverPort = '8883'

softVersion = '2013-12-26'


class CCP(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 娌¤瀹炰緥鍖栵紝璁板綍绗竴娆″疄渚嬪璞?
            cls.__instance = super(CCP, cls).__new__(cls, *args, **kwargs)

            # 鍒濆鍖朢EST SDK
            cls.__instance.rest = REST(serverIP, serverPort, softVersion)
            cls.__instance.rest.setAccount(accountSid, accountToken)
            cls.__instance.rest.setAppId(appId)
        return cls.__instance

    def send_sms(self, to, datas, tempId):

        result = self.rest.sendTemplateSMS(to, datas, tempId)
        if result.get('statusCode') == '000000':
            return 1
        else:
            return 0
