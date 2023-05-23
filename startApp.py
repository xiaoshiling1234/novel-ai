# 主应用的根目录
import Flask as Flask
import SQLAlchemy as SQLAlchemy

from application.settings.dev import DevelopmentConfig
from application.settings.prop import ProductionConfig

app = Flask(__name__)
config = {
    'dev': DevelopmentConfig,
    'prop': ProductionConfig,
}
# 设置配置类
Config = config['dev']
# 加载配置
app.config.from_object(Config)
# # 从配置对象中加载配置
# app.config.from_pyfile("config.ini")

# # 从环境变量中加载
# app.config.from_envvar("FLASKCONFIG")
# 创建数据库连接对象
db = SQLAlchemy(app)