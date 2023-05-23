from application import db


class Wdtest(db.Model):
    __tablename__ = "wdtest"  # 设置表名
    id = db.Column(db.String(100), primary_key=True, comment="主键ID")
    name = db.Column(db.String(20), index=True, comment="姓名")
    age = db.Column(db.Integer, default=True, comment="年龄")
