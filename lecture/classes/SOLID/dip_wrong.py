"""
Допустим, вы создаете приложение и у вас есть интерфейсный класс для удобного отображения данных пользователям.
В настоящее время приложение получает свои данные из базы данных
В этом примере класс FrontEnd зависит от класса BackEnd и его конкретной реализации.
Вы можете сказать, что оба класса тесно связаны. Такая связь может привести к проблемам с масштабируемостью.
Например, предположим, что ваше приложение быстро развивается, и вы хотите, чтобы оно могло считывать данные из REST API.
"""


class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)


class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
