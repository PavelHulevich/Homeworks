"""
Принцип разделения интерфейсов (ISP) исходит из того же принципа, что и принцип единой ответственности.
Основная идея этого принципа заключается в том, что - клиенты не должны быть вынуждены зависеть от методов, которые
они не используют. Принцип разделения интерфейсов говорит о том, что слишком «толстые» интерфейсы необходимо разделять
на более маленькие и специфические, чтобы клиенты маленьких интерфейсов знали только о методах, которые необходимы им в
работе. В итоге, при изменении метода интерфейса не должны меняться клиенты, которые этот метод не используют.
"""

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class ModernPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


"""
Теперь принтер, факс и сканер являются базовыми классами, которые предоставляют определенные интерфейсы с единой
ответственностью каждый. Чтобы создать старый принтер, вы наследуете только интерфейс принтера. Таким образом, у
класса не будет неиспользуемых методов. Чтобы создать класс ModernPrinter, вам нужно наследовать от всех интерфейсов.
Короче говоря, вы выделили интерфейс принтера.
Дизайн этого класса позволяет вам создавать различные машины с различными наборами функциональных возможностей, делая
ваш дизайн более гибким и расширяемым.
"""
