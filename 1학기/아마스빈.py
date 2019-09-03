#아마스빈 주문 앱           1.음료 이름 // 2. 컵 사이즈 // 3. 얼음량 // 4. 당도 // 5. 펄
#Drink <- Coffee    // <- 상속받는다.
#      <- Bubbletea // <- 상속받는다.
#Order
#  메뉴 보여주자.
#  음료 주문하자.
#  주문한 음료 보여주자.
#  총 금액 계산하자.
class Drink:
    _cups = ["레귤러", "점보"] #0 : 레귤러, 1 : 점보
    _ices = ["0%", "50%", "100%", "150%"] #0: 0%, 1: 50%, 2: 100%, 3: 150% . . .
    _sugars = ["0%", "50%", "100%", "150%"] #0: 0%, 1: 50%, 2: 100%, 3: 150% . . .

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0         #기본값
        self.ice = 2         #기본값
        self.sugar = 2       #기본값
    
    def __str__(self):   #이름 : self.name\t가격 : self.price원\t컵 : self.cup"
        return "이름: "+self.name+"\t가격: "+str(self.price)\
            +"원\t컵: "+Drink._cups[self.cup]\
            +"\t얼음량: "+Drink._ices[self.ice]\
            +"\t당도: "+Drink._sugars[self.sugar]
    
    def set_cup(self):
        self.cup = input("컵을 선택하세요(0 : 레귤러, 1: 점보)")
        if self.cup == "":   #사용자가 엔터만 치면 기본값 0을 넣자.
            self.cup = 0
        else:
            self.cup = int(self.cup)

        #점보면 300원 추가
        if self.cup == 1:
            self.price += 300

    def set_ice(self):
        self.ice = input("얼음량을 선택하세요.(0: 0%, 1: 50%, 2: 100%, 3: 150%)")
        if self.ice == "":
            self.ice = 2
        else:
            self.ice = int(self.ice)

    def set_sugar(self):
        self.sugar = input("당도를 선택하세요.(0:0%, 1:50%, 2:100%, 3:150%)")
        if self.sugar == "":
            self.sugar = 2
        else:
            self.sugar = int(self.sugar)

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

class Coffee(Drink): #Drink를 상속하는 커피
    pass

class Bubbletea(Drink): #Drink를 상속하는 버블티
    _pearls = ["타피오카", "코코", "젤리", "알로에"]

    def __init__(self, name, price):
        super().__init__(name, price)
        self.pearl = 0

    def set_pearl(self):
        self.pearl = input("펄을 선택하세요.(0:타피오카, 1:코코, 2:젤리, 3:알로에)")
        if self.pearl == "":
            self.pearl = 0
        else:
            self.pearl = int(self.pearl)

    def __str__(self):
        return super().__str__() + "\t펄: "+Bubbletea._pearls[self.pearl] #상속받은 부모를 부르는 문장

    def order(self): #상속 받은 것에서 중복된 것이 있다면 부모 걸 불러오는 게 더 이득!
        super().order()
        self.set_pearl()

class Order:
    _menus = [Coffee("아메리카노", 1800), Bubbletea("딸기요거트", 3500)]

    def __init__(self):
        self.order_menu = []
        self.order = None #자바에서 NULL과 같은 의미 - 딱히 넣을 값이 없을 때 사용.
    
    def show_menu(self):
        print("0: 아메리카노 1800원, 1: 딸기요거트 3500원")
    
    def sum_price(self):
        sum = 0
        for drink in self.order_menu:
            sum += drink.price
            
        return sum
    
    def order_drink(self):
        #반복▼
        while True:
            #   메뉴 보여주자
            self.show_menu()
            #   주문 받자.
            #   음료 선택하자.
            self.order = input("음료를 선택하세요: ")
            #       음료 객체 생성하자
            #0 -> Coffee("아메리카노", 1800)
            #1 -> Bubbletea("딸기요거트", 3500)
            if self.order == "":    #메뉴 선택안하고 그냥 엔터치면 주문 끝
                break
            drink = Order._menus[int(self.order)]
            #       음료 옵션 정하자.
            drink.order()
            #   주문한 음료 리스트에 추가하자.
            self.order_menu.append(drink)
            #반복▲
            #주문한 음료 출력하자.
            for drink in self.order_menu:
                print(drink)
            #   금액 합계 구하자.
            print("총금액: "+str(self.sum_price())+"원")

                  
o = Order()
o.order_drink()

#아메리카노 = Coffee("아메리카노", 1800)
#아메리카노.oder() #oder로 묶어준것. 아메리카노.set_cup() 아메리카노.set_ice() 아메리카노.set_sugar으로 나눌 수도 있다.
#print(아메리카노)   #이름 : 아메리카노\t가격 : 1800원
#타로밀크티 = Bubbletea("타로밀크티", 3500)
#타로밀크티.order() #타로밀크티.set_cup() 타로밀크티.set_ice() 타로밀크티.set_sugar() 타로밀크티.set_pearl()로 나눌 수 있다.
#print(타로밀크티)