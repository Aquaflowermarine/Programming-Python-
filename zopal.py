import sys
import random
class Dkstjekd:
    _whdfbs=["핀버튼", "포스터", "쿠션", "파일"]
    def __init__(self, name, price):
        self.name=name;
        self.price=price
        self.whdfb=0

    def __str__(self):
        return "애니: "+self.name+"\t가격: "+str(self.price)+"원\t 종류: "+Dkstjekd._whdfbs[self.whdfb]

    def set_whdfb(self):
        self.whdfb=input("종류를 선택하시오.(0: 핀버튼(5000원), 1: 포스터(8000원), 2: 쿠션(15000원), 3: 파일(7000원)): ")
        if self.whdfb=="":
            sys.exit()
        else:
            self.whdfb=int(self.whdfb)
    
    def order(self):
        self.set_whdfb()

class GPinbutton(Dkstjekd):
    _gpins=["본고레 핀버튼", "바리아 핀버튼", "캬발로네 핀버튼"]

    def __init__(self, name, price):
        super().__init__(name, price)
        self.gpinbutton=0
    
    def set_gpinbutton(self):
        self.gpinbutton=input("굿즈를 선택하십시오.(0: 본고레 핀버튼, 1: 바리아 핀버튼, 2: 캬발로네 핀버튼")
        if self.gpinbutton=="":
            sys.exit()
        else:
            self.gpinbutton=int(self.gpinbutton)
    def __str__(self):
        return super().__str__()+"굿즈: "+GPinbutton._gpins[self._gpinbutton]
    
    def order(self):
        super().order()
        self.set_gpinbutton()

class NPinbutton(Dkstjekd):
    _npins=["나츠메 핀버튼", "야옹 선생 핀버튼"]

    def __init__(self, name, price):
        super().__init__(name, price)
        self.npinbutton=0
    
    def set_npinbutton(self):
        self.npinbutton=input("굿즈를 선택하십시오.(0: 본고레 핀버튼, 1: 바리아 핀버튼, 2: 캬발로네 핀버튼) : ")
        if self.npinbutton=="":
            sys.exit()
        else:
            self.npinbutton=int(self.npinbutton)
    def __str__(self):
        return super().__str__()+"굿즈: "+NPinbutton._npins[self._npinbutton]
    
    def order(self):
        super().order()
        self.set_gpinbutton()

class Cuji(Dkstjekd):
    _cuji=["가정교사 히트맨 리본", "문호스트레이 독스"]
    _cuji1=["Last one : 본고레 대형 쿠션", "A : 사와다 츠나요시&리본 쿠션", "B : 고쿠데라 하야토&야마모토 타케시 쿠션", "C : 히바리 쿄야&로쿠도 무크로 쿠션", "D : 본고레 담요", "E : 바리아 담요", "F : 핀버튼"]
    _cuji2=["Last one : 데드애플 대형 쿠션", "A : 다자이 오사무&나카하라 츄야 쿠션", "B : 나카지마 아츠시&아쿠타카와 류노스케 쿠션", "C : 무장탐정사 담요", "D : 포트마피아 담요", "E : 암흑시대 담요 ", "F : 핀버튼"]

    def __init__(self, name, price):
        super().__init__(name, price)
        self.cuji=0
    
    def set_cuji(self):
        self.cuji=input("뽑고 싶은 제일 복권을 선택하십시오.(0: 가정교사 히트맨 리본, 1: 문호스트레이 독스) : ")
        if self.cuji=="":
            sys.exit()
        else:
            self.cuji=int(self.cuji)
    
    def __str_Cuji(self):
        if self.cuji==0:
            random.choice(cuji1)
        elif self.cuji==1:
            random.choice(cuji2)
    
    def __str__(self):
        if self.cuji==0:
            return super().__str__+"\t선택한 제일복권 : "+Cuji._cuji1[self.cuji]
        elif self.cuji==1:
            return super().__str__+"\t선택한 제일복권 : "+Cuji._cuji1[self.cuji]
    
    def order(self):
        super().order()
        self.set_cuji()

class Order:
    _menus = [Cuji("가정교사 히트맨 리본", 12000), GPinbutton("본고레 핀버튼", 5000), GPinbutton("바리아 핀버튼", 5000), GPinbutton("캬발로네 핀버튼", 5000), NPinbutton("나츠메 핀버튼", 5000), NPinbutton("야옹선생 핀버튼", 5000)]

    def __init__(self):
        self.order_menu=[]
        self.order=None
    
    def show_menu(self):
        print("0: 가정교사 히트맨 리본, 1: 나츠메 우인장, 2: 제일복권")

    def sum_price(self):
        sum=0
        for dkstjekd in self.order_menu:
            sum+=dkstjekd.price
        return sum
    
    def order_dkstjekd(self):
        while True:
            self.show_menu()
            self.order=input("애니를 선택하십시오. : ")

            if self.order=="":
                sys.exit()
            dkstjekd = Order._menus[int(self.order)]
            dkstjekd.order()
            self.order_menu.append(dkstjekd)
            for dkstjekd in self.order_menu:
                print(dkstjekd)
            print("총금액 : "+str(self.sum_price())+"원")

o=Order()
o.order_dkstjekd()