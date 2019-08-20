#굿즈 주문 앱 - 애니 종류를 보여주고 그 애니의 여러 굿즈들을 주문 받는 앱입니다.
import sys

class Anseodong:
    _kind=["가정교사 히트맨 리본", "나의 히어로 아카데미아", "문호스트레이 독스", "월간순정 노자키군", "은혼", "제일복권"]

    def __init__(self, name, price):
        self.name=name
        self.price=price

    
    def __str__(self):
        return "애니 : "+self.name+"\t가격: "+str(self.price)+"원"

class Gahiri(Anseodong):
    _goods=["본고레 핀버튼", "바리아 핀버튼", "캬발로네 핀버튼", "본고레 포스터", "바리아 포스터", "캬발로네 포스터", "본고레 스트랩", "바리아 스트랩", "아르꼬발레노 스트랩", "본고레 스티커", "바리아 스티커", "아르꼬발레노 스티커"]

    def __init__(self, name, price):
        super().__init__(name, price)
        self.goods=0
    
    def set_goods(self):
        self.goods=input("굿즈를 선택하십시오.(0: 본고레 핀버튼 1: 바리아 핀버튼 2: 캬발로네 핀버튼 3: 본고레 포스터 4: 바리아 포스터 5: 캬발로네 포스터 6: 본고레 스트랩 7:바리아 스트랩 8: 아르꼬발레노 스트랩 9:본고레 스티커 10: 바리아 스티커 11: 아르꼬발레노 스티커) : ")
        if self.goods=="":
            sys.exit()
        else:
            self.gooods = int(self.goods)
    
    def __str__(self):
        return super().__str__()+"\t굿즈: "+Gahiri._goods[int(self.goods)]
    
    def order(self):
        self.set_goods()


class Hiroaka(Anseodong):
    _goods=["미도리야 이즈쿠 팔찌", "토도로키 쇼토 팔찌", "바쿠고 카츠키 팔찌", "미도리야 이즈쿠 쿠션", "토도로키 쇼토 쿠션", "바쿠고 카츠키 쿠션", "UA 스티커", "빌런 연합 스티커"]

    def __init__(self, name, price):
        super().__init__(name, price)
        self.goods=0
    
    def set_goods(self):
        self.goods=input("굿즈를 선택하십시오.(0: 미도리야 이즈쿠 팔찌 1: 토도로키 쇼토 팔찌 2: 바쿠고 카츠키 팔찌 3: 미도리야 이즈쿠 쿠션 4: 토도로키 쿠션 5: 바쿠고 카츠키 쿠션 6: UA 스티커 7: 빌런 연합 스티커) : ")
        if self.goods=="":
            sys.exit()
        else:
            self.gooods = int(self.goods)
    
    def __str__(self):
        return super().__str__()+"\t굿즈: "+Gahiri._goods[int(self.goods)]
    
    def order(self):
        self.set_goods()


class Order:
    _menus=[Gahiri("가정교사 히트맨 리본", 5000), Gahiri("가정교사 히트맨 리본", 5000), Gahiri("가정교사 히트맨 리본", 5000),\
        Gahiri("가정교사 히트맨 리본", 8000), Gahiri("포스터", 8000),Gahiri("가정교사 히트맨 리본", 8000),\
        Gahiri("가정교사 히트맨 리본", 7000), Gahiri("가정교사 히트맨 리본", 7000), Gahiri("가정교사 히트맨 리본", 7000),\
        Gahiri("가정교사 히트맨 리본", 4000), Gahiri("가정교사 히트맨 리본", 4000), Gahiri("가정교사 히트맨 리본", 4000),\
        Hiroaka("나의 히어로 아카데미아", 9000), Hiroaka("나의 히어로 아카데미아", 9000), Hiroaka("나의 히어로 아카데미아", 9000),/
         Hiroaka("나의 히어로 아카데미아", 15000), Hiroaka("나의 히어로 아카데미아", 15000), Hiroaka("나의 히어로 아카데미아", 15000), Hiroaka("나의 히어로 아카데미아", 4000), Hiroaka("나의 히어로 아카데미아", 4000)]

    def __init__(self):
        self.order_menu=[]
        self.order=None
    
    def show_menu(self):
        print("0: 가정교사 히트맨 리본 1: 나의 히어로 아카데미아 2: 문호스트레이 독스 3: 월간순정 노자키군 4: 은혼 5: 제일복권")

    def sum_price(self):
        sum=0
        for anseodong in self.order_menu:
            sum+=anseodong.price
            
        return sum
        
    def order_anseodong(self):
        while True:
            self.show_menu()
            self.order=input("애니를 선택하십시오. : ")
            if self.order=="":
                sys.exit
            anseodong=Order._menus[int(self.order)]
            anseodong.order()
            self.order_menu.append(anseodong)
            for anseodong in self.order_menu:
                print(anseodong)
            print("총금액: "+str(self.sum_price()+2500)+"원")

o=Order()
o.order_anseodong()