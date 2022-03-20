from flask import Blueprint, request, Response
from db_operate.super_user_db.datacheck import UserService
from db_operate.card_db.datacheck import CardDateService
from common.methods import request_parse
import json


bp = Blueprint("super", __name__, url_prefix="/api/v1/")


@bp.route('deleteStaff/<int:card_id>')
def delete_staff(card_id):
    re = CardDateService.delete_staff(card_id)
    return json.dumps(re)


@bp.route('checkPassword', methods=['POST'])
def check_password():
    data = request_parse(request)
    re = UserService.check_password(data)
    return json.dumps(re)


@bp.route('gotoAdmin')  # 进入管理员状态
def goto_admin(data):
    pass
