import itchat
import datetime
import os

itchat.auto_login(hotReload=True)
send_time_hour = 23
to_users = []
today = False
while True:
    if datetime.datetime.now().hour == send_time_hour and not today:
        for user in to_users:
            for i in os.listdir("pic\\"):
                pos = "pic\\" + i
                itchat.send_image(pos, toUserName=itchat.search_friends(name=user)["UserName"])
            today = True
    if not datetime.datetime.now().hour and today:
        today = False
