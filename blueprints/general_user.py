from flask import Blueprint, request, g, Response
from db_operate.card_db.datacheck import CardDateService
import json

bp = Blueprint("user", __name__, url_prefix="/api/v1/")


def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data


@bp.route('updateStaff', methods=['POST'])
def update_staff():
    """添加或者更新接口"""
    data = request_parse(request)
    re = CardDateService.save_card(data)
    if re:
        return Response(json.dumps({"code": re[0], "msg": str(re[1])}),)
    return Response(json.dumps({"code": 0, "msg": '添加成功'}),)


@bp.route("getStaffList")
def get_staff_list():
    """获取列表接口
    http://127.0.0.1:5000/api/v1/getStaffList?id=1 通过下面这种情况也支持了单条数据的查询
    :return json_staffs：是一个列表类型的数据，里面是所有数据的字典形式。看前端代码这里需要返回一个列表，所以这么写了
    [{"id": 1, "service": "\u65b0\u5f00", "money": "111",
    "card_number": "111", "name": "123123", "phone": "111",
    "project": null, "shop_guide": null, "teacher": null, "financial": null, "remarks1": null,
     "collect_money": null, "remarks2": null},
     {"id": 2, "service": "\u65b0\u5f00", "money": "111", "card_number": "111", "name": "123123",
     "phone": "123123", "project": null, "shop_guide": null, "teacher": null, "financial": null,
     "remarks1": null, "collect_money": null, "remarks2": null}]
    """
    data = request_parse(request)
    card_id = data.get("id")
    card_list = CardDateService.select_card(card_id)
    json_staffs = CardDateService.format_card_resp(card_list)
    return Response(json.dumps(json_staffs))
