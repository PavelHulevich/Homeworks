"""Задание 4:
Предположим, у нас есть класс Phone, который хранит информацию о телефоне и имеет
методы для разных функций: звонить, отправлять сообщения, снимать фото, играть в игры и
т.д. Класс выглядит примерно так:
class Phone:
 def __init__(self, model, number):
 self.model = model
 self.number = number
 def call(self, other_number):
 print(f"Calling {other_number} from {self.number}")
 def send_message(self, other_number, text):
 print(f"Sending '{text}' to {other_number} from {self.number}")
 def take_photo(self):
 print(f"Taking a photo with {self.model}")
 def play_game(self, game):
 print(f"Playing {game} on {self.model}")
Этот класс нарушает принцип ISP, потому что если мы создадим объект типа Phone, то мы
будем зависеть от всех методов, даже если нам нужна только часть из них. Например, если
мы хотим использовать телефон только для звонков и сообщений, то нам не нужны методы
take_photo() и play_game(). Если мы хотим изменить логику этих методов, то мы можем
повлиять на работу других клиентов, которые используют этот класс.
Чтобы исправить эту проблему, необходимо сделать следующее:
• Создать интерфейс Phone, который будет содержать только общие поля и методы для всех
телефонов, например, model и number.
• Создать интерфейсы CallPhone, MessagePhone, PhotoPhone и GamePhone, которые будут
наследоваться от интерфейса Phone и добавлять методы для конкретных функций, например,
call(), send_message(), take_photo() и play_game().
• Создать классы BasicPhone, CameraPhone и SmartPhone, которые будут реализовывать
разные комбинации интерфейсов в зависимости от их возможностей. Например, BasicPhone
будет реализовывать только CallPhone и MessagePhone, CameraPhone будет реализовывать
CallPhone, MessagePhone и PhotoPhone, а SmartPhone будет реализовывать все интерфейсы"""


class Phone:
    def __init__(self, model, number):
        self.model = model
        self.number = number