import requests
import json
import qqsend
import datetime
import time
import func_timeout
from func_timeout import func_set_timeout

session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Token": "93a9ee679c0d4bdeaa081d26a02e3eaa"
}
while True:
    try:
        # print('流程开始')

        @func_set_timeout(2)
        def destinationurl():
            news = requests.post("https://api.aichaoliuapp.cn/aiera/common/banner_index_v2/notice",
                                 headers=headers)  # 获得公告json
            return news


        notice = destinationurl()
        #    print(notice.status_code)  #############打印状态
        newmessage = json.loads(notice.text)
        d = newmessage['d']
        newtitle = d[0]['banner_name'] + "\n" + d[0]['link'] + "\n" + "来自最速公告群314972008"

        with open('newtitle.txt', 'r+') as f:
            oldtitle = f.read()
            if oldtitle != newtitle:
                name = 'HOTDOG信息组'  # QQ聊天窗口的名字
                print('开始')
                qqsend.send(name, newtitle)
                #    print('结束')
                f.seek(0)
                f.truncate()
                f.write(newtitle)
                dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(dt)
        # else:
        # print("无更新")
        # dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(dt)
        time.sleep(1)

    except:
        # print('出现了超时！！！！！！！！！！！！！！！！！！！！！！！！！！！')
        continue
