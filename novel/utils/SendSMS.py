#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from novel.libs.yuntongxun.CCPRestSDK import REST

#涓诲笎鍙?
accountSid= '8a216da8627648690162843e217602d5'

#涓诲笎鍙稵oken
accountToken= ''

#搴旂敤Id
appId='8a216da8627648690162843e21d002db'

#璇锋眰鍦板潃锛屾牸寮忓涓嬶紝涓嶉渶瑕佸啓http://
serverIP='app.cloopen.com'

#璇锋眰绔彛 
serverPort='8883'

#REST鐗堟湰鍙?
softVersion='2013-12-26'

class CCP(object):
    """鑷畾涔夊崟渚嬬被锛岀敤浜庡彂鐭俊"""
    #鐢ㄤ簬璁板綍瀹炰緥
    __instance=None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            #娌¤瀹炰緥鍖栵紝璁板綍绗竴娆″疄渚嬪璞?
            cls.__instance=super(CCP, cls).__new__(cls,*args, **kwargs)

            # 鍒濆鍖朢EST SDK
            cls.__instance.rest = REST(serverIP, serverPort, softVersion)
            cls.__instance.rest.setAccount(accountSid, accountToken)
            cls.__instance.rest.setAppId(appId)
        return cls.__instance

    def send_sms(self,to, datas, tempId):
        """鍙戦?佹秷鎭帴鍙?"""
        # 璋冪敤鍙戦?佹秷鎭帴鍙ｈ繑鍥炵殑锛氬彂閫佹秷鎭殑缁撴灉
        result = self.rest.sendTemplateSMS(to, datas, tempId)
        if result.get('statusCode') == '000000':   # 鍙戦?佹垚鍔熻繑鍥炵殑鐘舵?佺爜
            return 1
        else:
            return 0

  # 鍙戦?佹ā鏉跨煭淇?
  # @param to 鎵嬫満鍙风爜
  # @param datas 鍐呭鏁版嵁 鏍煎紡涓烘暟缁? 渚嬪锛歿'12','34'}锛屽涓嶉渶鏇挎崲璇峰～ ''
  # @param $tempId 妯℃澘Id

# def sendTemplateSMS(to,datas,tempId):
#
#     #鍒濆鍖朢EST SDK
#     rest = REST(serverIP,serverPort,softVersion)
#     rest.setAccount(accountSid,accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to,datas,tempId)
#     for k,v in result.iteritems():
#
#         if k=='templateSMS' :
#                 for k,s in v.iteritems():
#                     print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)
#
   
#sendTemplateSMS(鎵嬫満鍙风爜,鍐呭鏁版嵁,妯℃澘Id)
