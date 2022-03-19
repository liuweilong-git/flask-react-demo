from models import CardModel
from exts import db
from common.exception import check
from db_operate.card_db.search import DataSearchRespDto


staffColumns = ("id", "service", "money", "card_number", "name", "phone", "project",\
                "shop_guide", "teacher", "financial", "remarks1", "collect_money", "remarks2")  #id没写可把我害惨了


class CardDateService(object):

    @staticmethod
    def save_card(card_dto):
        card = CardModel()
        CardDateService._update_card(card, card_dto)
        db.session.add(card)
        try:
            db.session.commit()
        except Exception as ex:
            r = check(not ex, u'插入监控任务有误')
            return r

    @staticmethod
    def select_card(card_id):
        if card_id:
            card = CardModel.query.filter_by(id=card_id).filter_by(is_deleted=0)
            return card
        else:
            card = CardModel.query.filter_by(is_deleted=0).order_by(CardModel.id.desc()).all()
            return card

    @staticmethod
    def format_card_resp(card_list):
        """
        获取全量card列表，打包展示
        :param card_list:
        :return:
        """
        dto_list = []
        for card in card_list:
            dto = DataSearchRespDto()
            dto.id = card.id
            dto.service = card.service
            dto.money = card.money
            dto.card_number = card.card_number
            dto.name = card.name
            dto.phone = card.phone
            dto.project = card.project
            dto.shop_guide = card.shop_guide
            dto.teacher = card.teacher
            dto.financial = card.financial
            dto.remarks1 = card.remarks1
            dto.collect_money = card.collect_money
            dto.remarks2 = card.remarks2
            dto_list.append(dto.__dict__)  # 关键：讲类属性以字典的形式存储，不写这个传递的是dto是一个对象，后面序列化不能成功
        return dto_list

    @staticmethod
    def _update_card(card, save_dto):
        """
        对于card的字段进行保存， 用于创建和更新的场景
        :param card&save_dto:
        :return:
        """
        card.service = save_dto.get('service')
        card.money = save_dto.get('money')
        card.card_number = save_dto.get('card_number')
        card.name = save_dto.get('name')
        card.phone = save_dto.get('phone')
        card.project = save_dto.get('project')
        card.shop_guide = save_dto.get('shop_guide')
        card.teacher = save_dto.get('teacher')
        card.financial = save_dto.get('financial')
        card.remarks1 = save_dto.get('remarks1')
        card.collect_money = save_dto.get('collect_money')
        card.remarks2 = save_dto.get('remarks2')

