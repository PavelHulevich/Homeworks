"""Задание 1:
Предположим, что у нас есть класс User, который представляет пользователя нашего
приложения. Класс имеет атрибуты name, email, password и role, которые хранят имя,
электронную почту, пароль и роль пользователя соответственно. Класс также имеет методы
register, login, logout, change_password, send_email и generate_report, которые позволяют
регистрировать, входить, выходить, менять пароль, отправлять электронные письма и
генерировать отчеты для пользователя.
class User:

 def __init__(self, name, email, password, role):
 self.name = name
 self.email = email
 self.password = password
 self.role = role

 def register(self):
 print(f"{self.name} is registered with email {self.email} and password {self.password}")

 def login(self):
 print(f"{self.name} is logged in with email {self.email} and password {self.password}")

 def logout(self):
 print(f"{self.name} is logged out")

 def change_password(self, new_password):
 print(f"{self.name} is changed password {self.password} to {new_password}")

 def send_email(self, subject, message, recipients):
 print(f"{self.name} is sent message {message} with {subject} to {recipients}")

 def generate_report(self, data):
 print(f"{self.name} is generated report with data {data}")
Этот класс нарушает принцип единственной ответственности, так как имеет несколько
причин для изменения. Например, если мы захотим изменить способ регистрации или входа,
мы должны изменить методы register и login. Если мы захотим изменить способ отправки
писем или формат отчетов, мы должны изменить методы send_email и generate_report. Это
может привести к ошибкам, несовместимостям или сложности поддержки кода.
Чтобы исправить эту проблему, мы разбейте класс User на несколько маленьких классов,
каждый из которых будет иметь одну ответственность. Например, мы можем создать класс
AuthService, который будет отвечать за регистрацию, вход и выход пользователя. Мы можем
создать класс EmailService, который будет отвечать за отправку писем от имени пользователя.
Мы можем создать класс ReportService, который будет отвечать за генерацию отчетов для
пользователя. Класс User будет иметь только атрибуты, связанные с данными пользователя, и
метод change_password, который будет менять пароль пользователя. Класс User будет
использовать объекты классов AuthService, EmailService и ReportService для выполнения
своих задач"""


class User:
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs

    def register(self) -> None:
        AuthService.register(self)

    def login(self) -> None:
        AuthService.login(self)

    def logout(self) -> None:
        AuthService.logout(self)

    def send_email(self) -> None:
        EmailService.send_email(self)

    def generate_report(self) -> None:
        ReportService.generate_report(self)

    def change_password(self) -> None:
        print(f"{self.name} is changed password {self.password} to {self.other}")


class AuthService:
    def register(self: User) -> None:
        print(f"{self.name} is registered with email {self.email} and password {self.password}")

    def login(self: User) -> None:
        print(f"{self.name} is logged in with email {self.email} and password {self.password}")

    def logout(self: User) -> None:
        print(f"{self.name} is logged out")


class EmailService:
    def send_email(self: User) -> None:
        print(f"{self.name} is sent message {self.other[0]} with {self.other[1]} to {self.other[2]}")


class ReportService:
    def generate_report(self: User) -> None:
        print(f"{self.name} is generated report with data {self.kwargs['data']}")


a = User('Dave', data='54545')
a.generate_report()
# a.send_email()



