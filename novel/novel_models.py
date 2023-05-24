from datetime import datetime

from novel import constants
from novel import db
from novel.utils.string_util import generate_uuid


class BaseModel(object):
    """模型基类"""
    create_time = db.Column(db.DateTime, default=datetime.now())  # 记录模型类创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now())  # 记录模型类更新时间


class NovelTask(BaseModel, db.Model):
    """AI绘画任务"""

    __tablename__ = 'novel_task'

    id = db.Column(db.String(16), default=generate_uuid(), primary_key=True)  # 任务id，16位uuid
    story = db.Column(db.String(3000), nullable=False)  # 故事内容，暂时限定长度不超过3000字
    category = db.Column(db.Integer, nullable=False)  # 故事分类
    story_name = db.Column(db.String(512), nullable=False)  # 故事名称
    status = db.Column(db.String(512), default='未完成', nullable=False)  # 任务状态
    video_path = db.Column(db.String(128), default='')  # 生成视频存放路径

    def to_dict(self):
        return {
            'id': self.id,
            'story': self.story,
            'category': self.category,
            'story_name': self.story_name,
            'status': self.status,
            'video_path': self.video_path,
            'create_time': self.create_time.strftime("%Y-%m-%d"),
            'update_time': self.update_time.strftime("%Y-%m-%d"),
        }


class NovelSubTask(BaseModel, db.Model):
    """AI绘画子任务-拆分到每一段话"""

    __tablename__ = 'novel_sub_task'

    id = db.Column(db.String(16), default=generate_uuid(), primary_key=True)  # 子任务id，16位uuid
    novel_id = db.Column(db.String(16), db.ForeignKey('novel_task.id'), nullable=False)  # 小说id
    order = db.Column(db.Integer, nullable=False)  # 排序
    prompt = db.Column(db.String(512))  # 绘画关键词
    negative = db.Column(db.String(512), nullable=False)  # 绘画负面词
    video_path = db.Column(db.Integer, nullable=False)  # 视频片段路径
    prompt_status = db.Column(db.Integer, nullable=False)  # 关键词状态:0未生成 1已生成
    picture_status = db.Column(db.Integer, nullable=False)  # AI绘图状态:0未生成 1已生成
    audio_status = db.Column(db.Integer, nullable=False)  # 语音状态:0未生成 1已生成
    video_status = db.Column(db.Integer, nullable=False)  # 视频状态:0未生成 1已生成

    def to_dict(self):
        return {
            'id': self.id,
            'novel_id': self.novel_id,
            'order': self.order,
            'prompt': self.prompt,
            'negative': self.negative,
            'video_path': self.video_path,
            'prompt_status': self.prompt_status,
            'picture_status': self.picture_status,
            'audio_status': self.audio_status,
            'video_status': self.video_status,
            'create_time': self.create_time.strftime("%Y-%m-%d"),
            'update_time': self.update_time.strftime("%Y-%m-%d"),
        }
