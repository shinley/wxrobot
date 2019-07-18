import itchat, time
from itchat.content import *
import json


# alert_info = "https://c.m.163.com/news/a/EBAA0QUC0530S72V.html?spss=newsapp&from=singlemessage   投资骗局, 读一读， 增强防骗技能"
alert_info = "测试消息"


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg)
    print(msg['FromUserName'])  # 自已
    print(msg['User']['Self']['UserName'])
    print(msg['Content'])   # 内容
    print(msg['User']['NickName']) # 群名
    if msg['FromUserName'] == msg['User']['Self']['UserName'] and msg['Content'] == 'alert':
        # if "2007" in msg['User']['NickName']:   # 群名
        members = msg['User']['MemberList']
        for member in members:
            # print(member['NickName'])       # 群成员
            msg.user.send(u'@%s\u2005%s' % (member['NickName'], alert_info))

    print("----------------------------------")


itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run(True)
#
# chat_rooms = itchat.get_chatrooms()
# print(chat_rooms)