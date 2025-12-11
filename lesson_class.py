from lesson_class_user import User
from lesson_class_card import Card

Vika = User("Vika")

Vika.sayName()
Vika.setAge(23) # создали запрос на изменение возраста
Vika.sayAge() # создали запрос на проверку изменения возраста

card = Card('1234 1234 1234 1234', '11/28', 'Vika M')
card.pay(1000)
