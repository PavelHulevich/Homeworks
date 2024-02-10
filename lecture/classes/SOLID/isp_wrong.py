from abc import ABC, abstractmethod

"""
В этом примере базовый класс Printer предоставляет интерфейс, который должны реализовывать его подклассы. 
Старый принтер наследуется от Printer и должен реализовывать тот же интерфейс. Однако OldPrinter не использует методы 
.fax() и .scan(), поскольку этот тип принтера не поддерживает эти функции.

Чтобы устранить эту проблему, вам следует разделить интерфейсы на более мелкие и специфичные классы. 
Затем вы можете создавать конкретные классы, наследуя от нескольких интерфейсных классов по мере необходимости
"""


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):

    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
