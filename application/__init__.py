import SQLAlchemy as SQLAlchemy
from flask import Flask

from application.settings.dev import DevelopmentConfig
from application.settings.prop import ProductionConfig

# 主应用的根目录
app = Flask(__name__)
config = {
    'dev': DevelopmentConfig,
    'prop': ProductionConfig,
}
# 设置配置类
Config = config['dev']
# 加载配置
app.config.from_object(Config)
# 创建数据库连接对象
db = SQLAlchemy(app)
# todo 注册蓝图
from .apps.novelai import index_blu

app.register_blueprint(index_blu, url_prefix='/index')
