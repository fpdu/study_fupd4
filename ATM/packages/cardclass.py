
class Card():
    def __init__(self,cardid,pwd,money=10,islock=False):
        self.card_id = cardid
        self.pwd = pwd
        self.money = money
        self.islock = islock