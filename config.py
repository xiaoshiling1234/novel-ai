# --*-- coding:utf-8 --*--
import logging
from redis import StrictRedis


class Config(object):
    """应用程序配置类"""
    # 开启调试模式
    DEBUG = True

    # logging等级
    LOGGIONG_LEVEL = logging.DEBUG

    # 配置secret key,简单生成方法，ipthon 中 base64.b64encode(os.urandom(48))
    SECRET_KEY = 'ix4En7l1Hau10aPq8kv8tuzcVl1s2Zo6eA+5+R+CXor8G3Jo0IJvcj001jz3XuXl'

    # orm连接数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/novel'
    # 是否开启追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 显示sql语句
    # SQLALCHEMY_ECHO=True

    # 配置Redis数据库
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_DB = 1

    # 配置session数据存储到redis数据库
    SESSION_TYPE = 'redis'
    # 指定存储session数据的redis的位置
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    # 开启session数据的签名，意思是让session数据不以明文形式存储
    SESSION_USE_SIGNER = True
    # 設置session的会话的超时时长 ：一天,全局指定
    PERMANENT_SESSION_LIFETIME = 3600 * 24
    JSON_AS_ASCII = False


class DevelopConfig(Config):
    """开发阶段下的配置子类"""
    # logging等级
    LOGGIONG_LEVEL = logging.DEBUG


class UnitTestConfig(Config):
    """单元测试配置子类"""
    # logging等级
    LOGGIONG_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/novel_test'


class ProductionConfig(Config):
    """生产环境下配置子类"""
    # logging等级
    LOGGIONG_LEVEL = logging.WARNING
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@fastsay.cn:3306/novel'
    REDIS_HOST = 'fastsay.cn'


# 工厂函数原材料
configs = {
    'default': Config,
    'develop': DevelopConfig,
    'unittest': UnitTestConfig,
    'production': ProductionConfig
}
