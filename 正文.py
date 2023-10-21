from bs4 import BeautifulSoup
import re
html_content = """
<div class="article__content">
<div class="article__title"><span style="font-size: 14px;"><img style="display: block; margin-left: auto; margin-right: auto;" src="http://cdn.aichaoliuapp.cn/hotdog/article_product/228/2023-07-31/1690770703917869830896287181962707504.jpeg" /></span></div>
<div class="article__content">
<div class="article__content">
<div class="article__content">
<div class="article__content">
<div class="article__content">
<div class="article__content">
<div class="article__content">
<div class="article__content">
<div class="article__content">
<div class="article__content">
<div class="article__content">
<div class="article__content">
<div data-page-id="QpNzdcFGWoaX6axQPZscCeL3ngg" data-docx-has-block-data="false">
<div class="ace-line ace-line old-record-id-NJmvdXOI1ous7fxWKfTcBNoRncf">&nbsp;</div>
</div>
<p><span style="font-size: 14px;">「雷鹏」现已移至【市场-推荐】，请需要寄售或购买的玩家可前往【HOTDOG数字艺术-市场】进行交易。</span></p>
<div id="1020718-2546-NFTGoods" class="cangping-jump">
<div style="display: flex; border: 1px solid #eeeeee; padding: 10px; border-radius: 5px; margin: 10px 0px;"><img style="border-radius: 10px; width: 100px; height: 100px; object-fit: cover;" src="http://cdn.aichaoliuapp.cn/hotdog/sale_product/244/2023-09-14/1694682860037231731792314051643814504.jpg" />
<div style="height: 100px; display: flex; flex-direction: column; justify-content: space-around; margin-left: 10px;">
<div style="color: #000; font-weight: bold;">雷鹏</div>
<div>创作者:D&middot;Slayer</div>
</div>
</div>
</div>
<br />
<p><span style="font-size: 14px;"><img src="http://cdn.aichaoliuapp.cn/hotdog/article_product/228/2023-07-31/1690770947773370304896816076746201279.png" /></span></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
"""
soup = BeautifulSoup(html_content, 'html.parser')
#pattern = re.compile(r'[\u4e00-\u9fa5]')

span_tags = soup.find_all('span')
if len(span_tags) > 1:
    for second_span in span_tags:
        print(second_span.text)