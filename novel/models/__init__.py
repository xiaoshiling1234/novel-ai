from novel import db
from datetime import datetime


class BaseModel(object):
    """模型基类"""
    create_time = db.Column(db.DateTime, default=datetime.now())  # 记录模型类创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now())  # 记录模型类更新时间
