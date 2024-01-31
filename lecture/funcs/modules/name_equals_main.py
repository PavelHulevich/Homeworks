"""
идиома if __name__ == "__main__" в Python - это просто обычный условный блок:
if __name__ == "__main__":
    print(1)


"""


#  В этом примере вы определяете функцию echo(), которая имитирует эхо в реальном мире, постепенно выводя все
#  меньше и меньше конечных букв входного текста.
def echo(text: str, repetitions: int = 3) -> str:
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."


#  Код ниже выполнится если запустим его в консоли python name_equals_main.py
#  print выведет __main__, str в случае запуска из консоли
print(__name__, type(__name__))
if __name__ == "__main__":
    text = input("TEXT")
    print(echo(text))
"""
Когда вы запускаете файл как скрипт, передавая объект file своему интерпретатору Python, 
выражение __name__ == "__main__" возвращает значение True. 
Затем выполняется блок кода в if, поэтому Python собирает пользовательский ввод и вызывает echo().
"""


"""
Код в вашем файле не запускается, если вы импортируете свой модуль. В этом случае Python присваивает 
__name__ имени модуля.

from name_equals_main import echo

#  print выведет name_equals_main, str в случае импорта модуля 
print(__name__, type(__name__))
"""