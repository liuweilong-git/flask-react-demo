from flask import Blueprint, request, Response
from db_operate.card_db.datacheck import CardDateService
from common.methods import request_parse
import json

bp = Blueprint("general", __name__, url_prefix="/api/v1/")


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


@bp.route("searchStaff_3")
def search_staff_3():
    data = request_parse(request)
    condition = data.get('where')
    condition = json.loads(condition)
    if condition:
        # 有条件才支持查询。本来想实现有查询条件才可以模糊查询，但是由于前端没有数据模糊查询也有where字段，所以这么判断不行
        array = CardDateService.select_card_like(condition)  # 这里是返回了一条数据而前端只需要其中3个字段
        json_staffs = CardDateService.get_staffs_from_data_3(array)  # 把需要的字段取出来放在一个列表里面
        return Response(json.dumps(json_staffs))
    else:
        return json.dumps(None)
