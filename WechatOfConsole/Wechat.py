# Authro     : ThreeDog
# Data       : 2019-04-29
# Thanks     : 底层使用itchat ：https://github.com/littlecodersh/itchat
# Function   : 在控制台使用微信，通过接口调用，接收并发送消息。 接收端需要一个线程来itchat.run()执行。
# Remark     : 仅支持文字消息，尽可能保持微信的用户体验
    # 'ls': 显示所有未读消息,
    # 'ls -f':显示所有的好友|群聊列表,
    # 'find XXX':通过姓名查找模糊查找好友或群聊,
    # 'cd {id}':进入与id为{id}的用户或群聊聊天,
    # 'cd ..':退出当前聊天返回上一级,
    # 'cls'：清空屏幕
    # 'exit'：退出程序,,
# Requests：
    # 待开发需求：
    # １、中文删除存在BUG
    # ２、上下左右光标不能移动
    # 3、文字编辑过程中，新来的消息会干扰输入
    # 4、添加设置模块
    #   1、设置中英文切换
    #   2、用文件保存设置
    #   3、
    # 5、新开发自动回复功能

from User import Users

# 主程序
if __name__ == '__main__':
    users = Users.instance()            # 初始化好友列表 (单例模式)
    users.exec()                        # 进入users的事件循环    



'''

itchat.send("Hello World!"，toUserName=None) # 讲信息发送给user
ithcat.send("@fil@%s" % '/tmp/test.text')
ithcat.send("@img@%s" % '/tmp/test.png')
ithcat.send("@vid@%s" % '/tmp/test.mkv')

@itchat.msg_register(TEXT)   #这里的TEXT表示如果有人发送文本消息，那么就会调用下面的方法
def simple_reply(msg):
    #这个是向发送者发送消息
    itchat.send_msg('已经收到了文本消息，消息内容为%s'%msg['Text'],toUserName=msg['FromUserName'])
    return "T reveived: %s" % msg["Text"]     #返回的给对方的消息，msg["Text"]表示消息的内容

itchat.get_friends()  返回完整的好友列表、
每个好友为一个字典, 其中第一项为本人的账号信息;
传入 update=True, 将更新好友列表并返回, get_friends(update=True)

# 获取任何一项等于name键值的用户
itchat.search_friends(name='autolife')
获取备注,微信号, 昵称中的任何一项等于name键值的用户. (可以与下一项配置使用.)

get_mps
将返回完整的工作号列表
每个公众号为一个字典,
传入 update=True 将更新公众号列表, 并返回.

get_chatrooms : 返回完整的群聊列表.
search_chatrooms : 群聊搜索.
update_chatroom : 获取群聊用户列表或更新该群聊.
memberList = itchat.update_chatroom('@@abcdefg1234567', detailedMember=True)

msg:
{'Type': 'Picture', 'HasProductId': 0, 'OriContent': '', 'ImgStatus': 2, 'Content': '<msg><emoji fromusername = "xxx" tousername = "xxx" type="2" idbuffer="media:0_0" md5="391aa301610adfb09f68b2018c16d1d5" len = "799676" productid="" androidmd5="391aa301610adfb09f68b2018c16d1d5" androidlen="799676" s60v3md5 = "391aa301610adfb09f68b2018c16d1d5" s60v3len="799676" s60v5md5 = "391aa301610adfb09f68b2018c16d1d5" s60v5len="799676" cdnurl = "http://emoji.qpic.cn/wx_emoji/4oib4WffkLFyKSDg81pBGyGibJvmhTwibzKID4l2qH1Y8m2d7LLc7BS3jaYZXSW18rA/" designerid = "" thumburl = "" encrypturl = "http://emoji.qpic.cn/wx_emoji/4oib4WffkLFyKSDg81pBGyGibJvmhTwibzKID4l2qH1Y8lC3m353zyDB6Fb6EPfmfRl/" aeskey= "18226a3b5ca16b1fe4cf673a06835c56" externurl = "http://emoji.qpic.cn/wx_emoji/4oib4WffkLFyKSDg81pBGyGibJvmhTwibzKID4l2qH1Y8k5WBC7exHjibjS9wdNKhiaZZ/" externmd5 = "29ed1b37a67292a5c279160ac424a869" width= "246" height= "273" tpurl= "" tpauthkey= "" attachedtext= "" attachedtextcolor= "" lensid= "" ></emoji> <gameext type="0" content="0" ></gameext></msg>', 'ImgWidth': 246, 'FromUserName': '@ac136711fc52d41c28b69e869c0e1ff053f67110699789c7b1ba0d997bc72341', 'StatusNotifyCode': 0, 'NewMsgId': 5287668932617961931, 'MsgId': '5287668932617961931', 'Url': '', 'StatusNotifyUserName': '', 'PlayLength': 0, 'Status': 3, 'VoiceLength': 0, 'AppMsgType': 0, 'CreateTime': 1560522490, 'ForwardFlag': 0, 'RecommendInfo': {'City': '', 'QQNum': 0, 'Content': '', 'AttrStatus': 0, 'Sex': 0, 'NickName': '', 'Province': '', 'Ticket': '', 'UserName': '', 'Alias': '', 'VerifyFlag': 0, 'Scene': 0, 'Signature': '', 'OpCode': 0}, 'FileSize': '', 'MediaId': '', 'AppInfo': {'Type': 0, 'AppID': ''}, 'MsgType': 47, 'Text': <function get_download_fn.<locals>.download_fn at 0x7f5af09fb510>, 'FileName': '190614-222810.gif', 'EncryFileName': '', 'Ticket': '', 'SubMsgType': 0, 'User': <User: {'Statues': 0, 'DisplayName': '', 'UserName': '@ac136711fc52d41c28b69e869c0e1ff053f67110699789c7b1ba0d997bc72341', 'PYQuanPin': 'baoweidewei', 'ChatRoomId': 0, 'StarFriend': 0, 'AttrStatus': 16974271, 'RemarkPYInitial': 'WZ', 'Sex': 1, 'NickName': '保卫的卫', 'Province': '北京', 'AppAccountFlag': 0, 'RemarkName': '卫卓', 'SnsFlag': 17, 'Alias': '', 'UniFriend': 0, 'PYInitial': 'BWDW', 'MemberCount': 0, 'City': '海淀', 'HideInputBarFlag': 0, 'KeyWord': '', 'OwnerUin': 0, 'RemarkPYQuanPin': 'weizhuo', 'MemberList': <ContactList: []>, 'VerifyFlag': 0, 'IsOwner': 0, 'Signature': '行胜于言', 'Uin': 0, 'ContactFlag': 3, 'EncryChatRoomId': '', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=685189850&username=@ac136711fc52d41c28b69e869c0e1ff053f67110699789c7b1ba0d997bc72341&skey=@crypt_126596ce_896f3c253fee022fec26706aac7531de'}>, 'ToUserName': '@5cabecfdc52403c768804bbc7bf006d56aec90943d34cd0c7f5a56d419cf308f', 'ImgHeight': 273}
'''