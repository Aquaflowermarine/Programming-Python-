from bs4 import BeautifulSoup
from urllib.request import urlopen


if __name__ == '__main__':
    response = urlopen("https://www.youtube.com/feed/trendng?gl=KR")
    soup = BeautifulSoup(response, "lxml")
    # print(soup)

    youtube_titles = soup.find_all("a", attrs={"class":"yt-uix-tile-link"})
    for youtube_title in youtube_titles:
        print(youtube_title.text)