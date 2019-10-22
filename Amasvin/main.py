#main.py
#주문한 음료 보여주자
#총 금액 계산하자
from order import Order
from file_manager import FileManager

#주문내역 불러오고, 보여주자
file_manager = FileManager("history.bin")
#answer = input("주문내역을 볼까요-?(yes of no)")
#if answer == "yes":

try:
    history = file_manager.load()
    for h in history:
        print(h)
except FileNotFoundError:
    print("주문내역이 없습니다.")

o = Order()
o.order_drink()

#주문내역 저장하자
file_manager.save(o.order_menu)