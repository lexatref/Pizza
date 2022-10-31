import click
import enum
import random


class PizzaSize(enum.Enum):
    l = 3
    xl = 5


class Pizza:
    """Базовый класс для пиццы"""
    receipt = ['tomato sauce', 'mozzarella']
    picture = ''

    def __init__(self, size: PizzaSize = PizzaSize.xl):
        self.size = size

    @classmethod
    def dict(cls):
        """Возвращает рецепт в виде словаря"""
        return {cls.__name__: cls.receipt}

    def __eq__(self, other):
        """Сравнивает пиццы"""
        if type(self) != type(other):
            return False
        return self.size == other.size


class Margherita(Pizza):
    """Пицца Margherita"""
    receipt = ['tomato sauce', 'mozzarella', 'tomatoes']
    picture = '🧀'


class Pepperoni(Pizza):
    """Пицца Pepperoni"""
    receipt = ['tomato sauce', 'mozzarella', 'pepperoni']
    picture = '🍕'


class Hawaiian(Pizza):
    """Пицца Hawaiian"""
    receipt = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
    picture = '🍍'


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    for child in Pizza.__subclasses__():
        if child.__name__.lower() == pizza.lower():
            pizza_instance = child()
            bake(pizza_instance)
            if delivery:
                deliver(pizza_instance)
            else:
                pickup(pizza_instance)
            break


@cli.command()
def menu():
    """Выводит меню"""
    for child in Pizza.__subclasses__():
        receipt = child.dict()
        for r in receipt:
            print(f' - {r} {child.picture}: {",".join(receipt[r])}')


def log(message: str = ''):
    """Декоратор с параметром.
    Если параметр не задан, то выводится имя функции и время исполнения (randint).
    Если параметр задан, то время исполнения подставляется в переданную строку."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if message == '':
                func_time = args[0].size.value * random.randint(1, 10)
                print(f'{func.__name__} - {func_time} c!')
            else:
                func_time = random.randint(1, 10)
                print(message.replace('{}', f'{func_time}'))
        return wrapper
    return decorator


@log()
def bake(pizza: Pizza):
    """Готовит пиццу"""
    pass


@log('🛵 Доставили за {}с!')
def deliver(pizza: Pizza):
    """Доставляет пиццу"""
    pass


@log('🏠 Забрали за {}с!')
def pickup(pizza: Pizza):
    """Самовывоз"""
    pass


if __name__ == '__main__':
    cli()
