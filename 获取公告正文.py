import requests
import json
from bs4 import BeautifulSoup
import qqsend
import re
def find_text(url):
    url = url
    match = re.search(r'\?id=(\w+)', url)
    id_part = match.group(1)
    data = {"id": id_part}
    headers = {
        "Content-Type" : "application/json"
    }
    response = requests.post("https://api.aichaoliuapp.cn/aiera/v2/hotdog/notice/article/view",headers=headers,data=json.dumps(data))
    post = response.text #获得网页文本
    datadict = json.loads(post) #载入为字典
    content = datadict["data"]["content"] #获取网页正文部分

    soup = BeautifulSoup(content, 'html.parser')

    span_tags = soup.find_all('span')
    if len(span_tags) > 1:
        all_text = []
        with open("公告正文.txt","w",encoding="utf-8") as f:
            f.seek(0)
            f.truncate()
            for Find_Span_Text in span_tags:
                all_text.append(Find_Span_Text.text)
                f.write(Find_Span_Text.text + "\n")
        all_text_str = '\n'.join(all_text) + "\n最速公告推送群314972008" + "\n公告正文自动推送群933317582"
    name = "信息组-公告正文群"
    qqsend.send(name, all_text_str)


    if "突袭" in all_text_str:
        qqsend.send(name, "@全体成员 有突袭")