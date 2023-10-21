import requests
import json
import qqsend
import datetime
import time
import func_timeout
from func_timeout import func_set_timeout
import 获取公告正文

session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Token": "bc4a3b22a953414db2814300a429ed50"
}
while True:
    try:


        @func_set_timeout(2)
        def destinationurl():
            news = requests.post("https://api.aichaoliuapp.cn/aiera/common/banner_index_v2/notice",
                                 headers=headers)  # 获得公告json
            return news


        notice = destinationurl()
        #    print(notice.status_code)  #############打印状态
        newmessage = json.loads(notice.text)  # 载入json为字典

        d = newmessage['d']  # 提取列表需要的部分
        newtitle = d[0]['banner_name'] + "\n" + d[0]['link'] + "\n" + "来自最速公告群314972008" + "\n公告正文推送群933317582"

        # 提取正文部分

        # match = re.search(r'\?id=(\w+)', url)
        # payload_id = match.group(1)
        # print(payload_id)

        with open('newtitle.txt', 'r+') as f:
            oldtitle = f.read()
            if oldtitle != newtitle:
                name = 'HOTDOG信息组'  # QQ聊天窗口的名字
                print('开始')
                qqsend.send(name, newtitle)

                url = d[0]['link']  # 提取URL
                获取公告正文.find_text(url)
                # txt写入最新公告
                f.seek(0)
                f.truncate()
                f.write(newtitle)
                if "突袭" in newtitle:
                    qqsend.send(name, "@全体成员 有突袭")

                # 控制台输出时间
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
