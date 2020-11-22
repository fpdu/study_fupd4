import random,pickle,os,pymysql
from packages import cardclass as card
from packages import personclass as person


class Controller():
    # userid_cardid_dict = {}
    # cardid_userobj_dict = {}
    #
    # user_file_url = './databases/user.txt'
    # card_file_url = './databases/card.txt'
    #
    # def __init__(self):
    #     self.__loaddata()
    # def __loaddata(self):
    #     if os.path.exists(self.card_file_url):
    #         with open(self.card_file_url,'rb') as fp:
    #             self.userid_cardid_dict = pickle.load(fp)
    #     if os.path.exists(self.user_file_url):
    #         with open(self.user_file_url) as fp:
    #             self.cardid_userobj_dict = pickle.load(fp)
    #
    # def register(self):
    #     name = self.__getusername()
    #     userid = self.__getuserid()
    #     if userid in self.userid_cardid_dict:
    #         print(f'当前用户已经存在, 卡号为:{self.userid_cardid_dict[userid]}')
    #         # return
    #     phone = self.__getuserphone()
    #     password = self.__getuserpwd()
    #
    #     cardid = random.randint(100000,999999)
    #     cardobj = card.Card(cardid,password)
    #
    #     userobj = person.Person(name,userid,phone,cardobj)
    #     self.userid_cardid_dict[userid] = cardid
    #     self.cardid_userobj_dict[cardid] = userobj
    #
    #     print(f'恭喜{name}开户成功,卡号为:{cardid},余额为:{cardobj.money}元')

    info = []
    def __init__(self):
        self.__loaddata()

    def __loaddata(self):
        db = pymysql.connect('localhost','root','adu0253','tlxy',cursorclass=pymysql.cursors.DictCursor)
        try:
            cursor = db.cursor()
            sql = 'select * from ATM'
            cursor.execute(sql)
            data = cursor.fetchall()
            for i in data:
                self.info.append(i['userid'])
            return self.info
        except Exception as e:
            print(f'出错了:{e}')
        finally:
            db.close()



    def register(self):
        name = self.__getusername()
        print(name,type(name))
        userid = self.__getuserid()
        if userid in self.info:
            print('当前用户已经存在,请重新输入')
        phone = self.__getuserphone()
        password = self.__getuserpwd()
        cardid = random.randint(100000,999999)

        db = pymysql.connect('localhost', 'root', 'adu0253', 'tlxy', cursorclass=pymysql.cursors.DictCursor)
        try:
            cursor = db.cursor()
            sql = f'insert into ATM(name,userid,phone,card_id,pwd) value({name},{userid},{phone},{cardid},{password})'
            cursor.execute(sql)

            db.commit()
        # except Exception as e:
        #     print(f'出错了:{e}')
        finally:
            db.close()

        print(f'开卡成功:姓名{name},卡号:{cardid},余额为:10元')


    def query(self):
        pass



    def __getusername(self):
        while True:
            name = input('请输入您的用户名:')
            if not name:
                print('输入有问题,请重新输入')
                continue
            else:
                return name
    def __getuserid(self):
        while True:
            userid = input('请输入您的身份证号:')
            if not userid:
                print('输入有问题,请重新输入')
                continue
            else:
                return userid

    def __getuserphone(self):
        while True:
            phone = input('请输入您的手机号:')
            if not phone:
                print('输入有问题,请重新输入')
                continue
            else:
                return phone

    def __getuserpwd(self):
        while True:
            pwd = input('请输入您的密码:')
            if  pwd:
                repwd = input('请再次输入确认密码:')
                if pwd == repwd:
                    return pwd
                else:
                    print('两次输入的密码不一致.')
                    continue
