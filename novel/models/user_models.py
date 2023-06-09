# --*-- coding:utf-8 --*--
from datetime import datetime
from novel import db
from novel import constants
from werkzeug.security import generate_password_hash, check_password_hash

from novel.models import BaseModel


class User(BaseModel, db.Model):
    """用户模型类"""
    __tablename__ = 'ih_user_profile'

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password = db.Column(db.String(128), nullable=False)  # 加密的密码
    phone_num = db.Column(db.String(11), unique=True, nullable=False)  # 手机号
    real_name = db.Column(db.String(32))  # 真实姓名
    id_card = db.Column(db.String(20))  # 身份证号
    avatar_url = db.Column(db.String(128))  # 用户头像路径
    houses = db.relationship('House', backref='user', lazy='dynamic')  # 用户发布的房屋
    orders = db.relationship('Order', backref='user', lazy='dynamic')  # 用户下的订单

    @property
    def password_hash(self):
        raise AttributeError(u'不能访问该属性')

    @password_hash.setter
    def password_hash(self, value):
        # 生成hash密码
        self.password = generate_password_hash(value)

    def check_password(self, password):
        # 校验密码是否正确
        return check_password_hash(self.password, password)

    def to_dict(self):
        # 返回一个用户信息字典接口，使外界方便调用
        user_info = {
            'user_id': self.id,
            'name': self.name,
            'phone_num': self.phone_num,
            'avatar_url': self.avatar_url
        }
        if self.avatar_url:
            user_info['avatar_url'] = constants.QINIU_DOMIN_PREFIX + self.avatar_url
        return user_info

    def to_auth_dict(self):
        """实名认证数据"""
        return {
            'real_name': self.real_name,
            'id_card': self.id_card
        }


class Area(BaseModel, db.Model):
    """城区"""
    __tablename__ = 'ih_area_info'

    id = db.Column(db.Integer, primary_key=True)  # 区域编号
    name = db.Column(db.String(32), nullable=False)  # 区域名字
    houses = db.relationship('House', backref='area')  # 区域的房屋

    def to_dict(self):
        return {
            'aname': self.name,
            'aid': self.id
        }


class Facility(BaseModel, db.Model):
    """房屋设施信息模型类"""
    __tablename__ = 'ih_facility_info'

    id = db.Column(db.Integer, primary_key=True)  # 设施编号
    name = db.Column(db.String(32), nullable=False)  # 设施名字


# 房屋设施表，建立房屋与设施的多对多关系
house_facility = db.Table(
    "ih_house_facility",
    db.Column('house_id', db.Integer, db.ForeignKey('ih_house_info.id'), primary_key=True),  # 房屋编号
    db.Column('facility_id', db.Integer, db.ForeignKey('ih_facility_info.id'), primary_key=True)  # 设施编号
)


class House(BaseModel, db.Model):
    """房屋模型类"""

    __tablename__ = 'ih_house_info'

    id = db.Column(db.Integer, primary_key=True)  # 房屋编号
    user_id = db.Column(db.Integer, db.ForeignKey('ih_user_profile.id'), nullable=False)  # 房屋主人编号
    area_id = db.Column(db.Integer, db.ForeignKey('ih_area_info.id'), nullable=False)  # 房屋地区编号
    title = db.Column(db.String(64), nullable=False)  # 标题
    price = db.Column(db.Integer, default=0)  # 单价 单位：分
    address = db.Column(db.String(512), default='')  # 地址
    room_count = db.Column(db.Integer, default=1)  # 房间数目
    acreage = db.Column(db.Integer, default=0)  # 房间面积
    unit = db.Column(db.String(32), default='')  # 房屋单元,几室几厅
    capacity = db.Column(db.Integer, default=1)  # 房屋能住多少人
    beds = db.Column(db.String(64), default="")  # 房屋床铺的配置
    deposit = db.Column(db.Integer, default=0)  # 房屋押金
    min_days = db.Column(db.Integer, default=1)  # 最少入住天数
    max_days = db.Column(db.Integer, default=0)  # 最多入住天数，0表示不限制
    order_count = db.Column(db.Integer, default=0)  # 预订完成的该房屋的订单数
    index_image_url = db.Column(db.String(256), default="")  # 房屋主图片的路径
    facilities = db.relationship("Facility", secondary=house_facility)  # 房屋的设施
    images = db.relationship("HouseImage")  # 房屋的图片
    orders = db.relationship("Order", backref="house")  # 房屋的订单

    def to_basic_dict(self):
        """房屋基本信息字典"""
        return {
            "house_id": self.id,
            "title": self.title,
            "price": self.price,
            "area_name": self.area.name,
            "img_url": constants.QINIU_DOMIN_PREFIX + self.index_image_url if self.index_image_url else "",
            "room_count": self.room_count,
            "order_count": self.order_count,
            "address": self.address,
            "user_avatar": constants.QINIU_DOMIN_PREFIX + self.user.avatar_url if self.user.avatar_url else "",
            "ctime": self.create_time.strftime("%Y-%m-%d")
        }

    def to_full_dict(self):
        """房屋详细信息字典"""
        house_dict = {
            "hid": self.id,
            "user_id": self.user_id,
            "user_name": self.user.name,
            "user_avatar": constants.QINIU_DOMIN_PREFIX + self.user.avatar_url if self.user.avatar_url else "",
            "title": self.title,
            "price": self.price,
            "address": self.address,
            "room_count": self.room_count,
            "acreage": self.acreage,
            "unit": self.unit,
            "capacity": self.capacity,
            "beds": self.beds,
            "deposit": self.deposit,
            "min_days": self.min_days,
            "max_days": self.max_days,
        }
        # 房屋图片
        img_urls = []
        for image in self.images:
            img_urls.append(constants.QINIU_DOMIN_PREFIX + image.url)
        house_dict["img_urls"] = img_urls

        # 房屋设施
        facilities = []
        for facility in self.facilities:
            facilities.append(facility.id)
        house_dict["facilities"] = facilities

        # 评论信息
        comments = []
        orders = Order.query.filter(Order.house_id == self.id, Order.status == "COMPLETE", Order.comment != None) \
            .order_by(Order.update_time.desc()).limit(constants.HOUSE_DETAIL_COMMENT_DISPLAY_COUNTS)
        for order in orders:
            comment = {
                "comment": order.comment,  # 评论的内容
                "user_name": order.user.name if order.user.name != order.user.mobile else "匿名用户",  # 发表评论的用户
                "ctime": order.update_time.strftime("%Y-%m-%d %H:%M:%S")  # 评价的时间
            }
            comments.append(comment)
        house_dict["comments"] = comments
        return house_dict


class HouseImage(BaseModel, db.Model):
    """房屋图片模型类"""
    __tablename__ = 'ih_house_image'

    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('ih_house_info.id'), nullable=False)
    url = db.Column(db.String(256), nullable=False)  # 图片路径


class Order(BaseModel, db.Model):
    """订单"""

    __tablename__ = "ih_order_info"

    id = db.Column(db.Integer, primary_key=True)  # 订单编号
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"), nullable=False)  # 下订单的用户编号
    house_id = db.Column(db.Integer, db.ForeignKey("ih_house_info.id"), nullable=False)  # 预订的房间编号
    begin_date = db.Column(db.DateTime, nullable=False)  # 预订的起始时间
    end_date = db.Column(db.DateTime, nullable=False)  # 预订的结束时间
    days = db.Column(db.Integer, nullable=False)  # 预订的总天数
    house_price = db.Column(db.Integer, nullable=False)  # 房屋的单价
    amount = db.Column(db.Integer, nullable=False)  # 订单的总金额
    status = db.Column(  # 订单的状态
        db.Enum(
            "WAIT_ACCEPT",  # 待接单,
            "WAIT_PAYMENT",  # 待支付
            "PAID",  # 已支付
            "WAIT_COMMENT",  # 待评价
            "COMPLETE",  # 已完成
            "CANCELED",  # 已取消
            "REJECTED"  # 已拒单
        ),
        default="WAIT_ACCEPT", index=True)
    comment = db.Column(db.Text)  # 订单的评论信息或者拒单原因

    def to_dict(self):
        return {
            "order_id": self.id,
            "title": self.house.title,
            "img_url": constants.QINIU_DOMIN_PREFIX + self.house.index_image_url if self.house.index_image_url else "",
            "start_date": self.begin_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "ctime": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "days": self.days,
            "amount": self.amount,
            "status": self.status,
            "comment": self.comment if self.comment else ""
        }
