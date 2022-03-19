from exts import db
from datetime import datetime


class CardModel(db.Model):
    __tablename__ = "card"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service = db.Column(db.String(100), nullable=False, doc=u'业务')
    money = db.Column(db.String(100), nullable=False, doc=u'金额')
    card_number = db.Column(db.String(100), nullable=False, doc=u'卡号')
    name = db.Column(db.String(255), nullable=False, doc=u'姓名')
    phone = db.Column(db.String(255), nullable=False, doc=u'手机号')
    project = db.Column(db.String(255), doc=u'项目')
    shop_guide = db.Column(db.String(255), doc=u'导购员')
    teacher = db.Column(db.String(255), doc=u'老师')
    financial = db.Column(db.String(255), doc=u'财务情况')
    remarks1 = db.Column(db.String(255), doc=u'备注1')
    collect_money = db.Column(db.String(255), doc=u'收钱吧详情')
    remarks2 = db.Column(db.String(255), doc=u'备注2')
    create_time = db.Column(db.DateTime, default=datetime.now)
    modify_time = db.Column(db.DateTime, default=datetime.now)
    is_deleted = db.Column(db.Integer, nullable=False, default=0, doc=u'是否删除：0-未删除，1-已删除')


class SuperUserModel(db.Model):
    __tablename__ = "super_user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True, doc=u'管理员姓名')
    password = db.Column(db.String(200), nullable=False, doc=u'密码')
    create_time = db.Column(db.DateTime, default=datetime.now)
