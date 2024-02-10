from math import pi


"""
Инициализатор Shape принимает аргумент shape_type, который может быть либо "прямоугольником", либо "кругом". Он также 
принимает определенный набор аргументов ключевого слова, используя синтаксис **kwargs. Если вы задаете тип фигуры 
"прямоугольник", то вам также следует передать аргументы ключевых слов width и height, чтобы вы могли построить 
правильный прямоугольник.
Напротив, если вы задаете тип фигуры "круг", то вы также должны передать аргумент radius для построения круга.
У Shape также есть метод .calculate_area(), который вычисляет площадь текущей фигуры в соответствии с ее .shape_type
"""


class Shape:

    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2
        elif self.shape_type == "circle":
            return pi * self.radius**2


rectangle = Shape("rectangle", width=10, height=5)
rectangle.calculate_area()

circle = Shape("circle", radius=5)
circle.calculate_area()


"""
Класс работает. Вы можете создавать круги и прямоугольники, вычислять их площадь и так далее. Однако класс выглядит 
довольно плохо. На первый взгляд кажется, что с ним что-то не так.
Представьте, что вам нужно добавить новую фигуру, возможно, квадрат. Как бы вы это сделали? Что ж, вариант здесь состоит
в том, чтобы добавить еще одно предложение elif к .__init__() и to .calculate_area(), чтобы вы могли удовлетворить 
требования к квадратной форме.
Необходимость вносить эти изменения для создания новых фигур означает, что ваш класс открыт для модификации. Это 
нарушает принцип "открыто-закрыто". Как вы можете исправить свой класс, чтобы сделать его открытым для расширения, 
но закрытым для модификации?
"""
