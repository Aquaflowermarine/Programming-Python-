from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with urlopen("https://movie.daum.net/boxoffice/weekly") as response:
        soup = BeautifulSoup(response, "lxml")

    # print(soup)
    movie_titles = soup.find_all("a", attrs={"class":"link_g"})
    print("다음 영화 박스오피스 주간")
    n = 1
    for movie_title in movie_titles[2:]:
        print(movie_title.text)
        n += 1