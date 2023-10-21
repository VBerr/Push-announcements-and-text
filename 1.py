import requests
import json
from bs4 import BeautifulSoup
data = {"id":"27y10AW"}
headers = {
    "Content-Type" : "application/json"
}
responce = requests.post("https://api.aichaoliuapp.cn/aiera/v2/hotdog/notice/article/view",headers=headers,data=json.dumps(data))
post = responce.text #获得网页文本
datadict = json.loads(post) #载入为字典
content = datadict["data"]["content"] #获取网页正文部分

soup = BeautifulSoup(content, 'html.parser')
#pattern = re.compile(r'[\u4e00-\u9fa5]')

span_tags = soup.find_all('span')
if len(span_tags) > 1:
    for findspan in span_tags:
        print(findspan.text)