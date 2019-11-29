# 터미널 > pip install bs4
# 터미널 > pip install lxml

from bs4 import BeautifulSoup  # html 구조적으로 변환하자   alt + shift + enter
from urllib.request import urlopen

if __name__ == '__main__':
     # 네이버 웹툰 > 신의 탑 제목 가져오자
     #data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=183559")

     #soup = BeautifulSoup(data, "lxml")
     #data.close()

     with urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=183559") as data:
         soup = BeautifulSoup(data, "lxml")

     # print(soup)
     cartoon_titles = soup.find_all("td", attrs={"class":"title"})  # class 가 title 인 것만 출력
     html = "<html><head><meta charset='utf-8'></head><body>"
     for title in cartoon_titles:
         t = title.find("a").text # 제목 가져오자
         link = title.find("a").get("href") # 링크 가져오자
         link = "http://comic.naver.com/" + link
         print(t)
         print(link)
         print("<a href='"+link+"'>"+t+"</a>")
         html += "<a href='"+link+"'>"+t+"</a>"
     html += "</body></html>"
     print(html)