from kassa import Kassa                                                 
from person import Person
from ticket import Ticket
from train import Train

print("Главная программа", __name__)

test_man = Person("Ilon Mask", 55)
test_man.earn(27000)
test_man.pay(11111)
test_man.show()


almaty1 = Kassa()
price = almaty1.get_price("Алматы", "Ош")
almaty1.buy_ticket("Алматы", "Сантьяго", test_man)

train = Train(almaty1,"Алматы", "Сантьяго")
train.show()

print(almaty1.tickets)
train.board(test_man)
print(almaty1.tickets)

