from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# 크롬확장프로그램 > json viewer

if __name__ == '__main__':
    # 다음 웹툰 > 어쩌다 발견한 7월
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/findjuly") as response:
        response_byte = response.read()
    response_json = json.loads(response_byte)
    
    cartoon_titles = response_json['data']['webtoon']['webtoonEpisodes']
    print(cartoon_titles)