"""Задание 4:
Напишите декоратор для функции, выполняющей сетевые запросы. Декоратор должен
ограничивать количество попыток вызова декорируемой функции 3 попытками и увеличивать
время между попытками запросов по формуле = attempt*2 + 3, если второй аргумент
декоратора выставлен в True и делать новый вызов функции немедленно, если второй
аргумент декоратора выставлен в False.
Декоратор должен перехватывать исключения из декорируемой функции и вызывать ее
повторно, если не закончились попытки. Декоратор должен выводить в консоль номер
текущей попытки, статус ответа, наличие или отсутствие ошибки. Если попытки закончились
декоратор должен вернуть исключение, которое было вызвано декорируемой функцией.

import requests
def retry(attempts: int, delayed: bool):
 …
@retry(attempts=3, delayed=True)
def get_python() -> requests.Response:
 return requests.get('https://python.org', timeout=0.05)
respone = get_python()

@retry(attempts=3, delayed=False)
def get_python2() -> requests.Response:
 return requests.get('https://python.org', timeout=0.05)
respone = get_python2()"""

from typing import Callable
import requests
import sys
from time import sleep


def retry(attempts: int, delayed: bool) -> Callable:
    def retry_outer(func: Callable) -> Callable[[], requests.Response]:
        def retry_inner() -> requests.Response:
            answer = ''
            for attempt in range(0, attempts):
                try:
                    print(f'Попытка связи № {attempt + 1} ...   ', end='')
                    answer = func()
                    print(f'Связь установлена. Статус ответа {answer}. ', end='')
                    if answer:
                        print('Ошибок нет. Возвращеен код: ', answer.status_code)
                    else:
                        print('В ответе есть ошибка: ', answer.status_code)
                    break
                except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
                    exept_tmp = sys.exc_info()[0]
                    if attempt < attempts - 1:  # если не достигнут лимит запросов, то сообщение и продолжаем
                        if delayed:  # Если ли задержка
                            print(f'Неудачная попытка связи. Задержка перед следующим запросом:  {attempt * 2 + 3} сек')
                            sleep(attempt * 2 + 3)
                            continue
                        else:
                            print('Неудачная попытка связи.')
                            continue
                print('Связь не удалась. Попытки закончились. ', end='')
                print('Сработало исключение: ', exept_tmp)
                answer = exept_tmp
            return answer
        return retry_inner
    return retry_outer


@retry(attempts=3, delayed=True)
def get_python() -> requests.Response:
    return requests.get('https://python.org', timeout=0.05)


@retry(attempts=3, delayed=False)
def get_python2() -> requests.Response:
    return requests.get('https://python.org', timeout=0.05)


print('\nВызываем функцию "get_python()":')
respone = get_python()
print(respone)

print('\nВызываем функцию "get_python2()":')
respone = get_python2()
print(respone)
