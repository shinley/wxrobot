import itchat, time
from itchat.content import *

alert_info = "https://c.m.163.com/news/a/EBAA0QUC0530S72V.html?spss=newsapp&from=singlemessage   投资骗局, 读一读， 增强防骗技能"


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg.ActualNickName)
    if "珍珍呀" in msg.ActualNickName:
        msg.user.send(alert_info)

    if "王重阳" in msg.ActualNickName:
        msg.user.send(alert_info)


itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run(True)
