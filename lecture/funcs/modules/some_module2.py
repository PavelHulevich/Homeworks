__all__ = (
    'func',
    'func2',
)


def func():
    ...


def func2():
    def func4():
        ...

    func4()
    ...


def func3():
    ...
