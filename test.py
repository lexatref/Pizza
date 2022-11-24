
from Pizza import PizzaSize, Pizza, Margherita, Pepperoni, cli
from click.testing import CliRunner
import random


def test_pizza():
    p = Pizza()
    receipt = p.dict()
    assert receipt == {'Pizza': ['tomato sauce', 'mozzarella']}


def test_pizza_margherita():
    p = Margherita(PizzaSize.l)
    receipt = p.dict()
    assert receipt == {'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes']}


def test_pizza_pepperoni_class():
    assert Pepperoni.receipt == ['tomato sauce', 'mozzarella', 'pepperoni']


def test_pizza_margherita_size():
    l = Margherita(PizzaSize.l)
    xl = Margherita()
    assert not (l == xl)


def test_pizza_eq():
    m = Margherita()
    p = Pepperoni()
    assert not (m == p)


def test_command_menu():
    runner = CliRunner()
    result = runner.invoke(cli, ['menu'])
    assert result.exit_code == 0
    assert result.output == ' - Margherita 🧀: tomato sauce,mozzarella,tomatoes\n' \
                            ' - Pepperoni 🍕: tomato sauce,mozzarella,pepperoni\n' \
                            ' - Hawaiian 🍍: tomato sauce,mozzarella,chicken,pineapples\n'


def test_command_order_delivery():
    runner = CliRunner()
    random.seed(5)
    result = runner.invoke(cli, ['order', 'pepperoni', '--delivery'])
    assert result.exit_code == 0
    assert result.output == 'bake - 50 c!\n'\
                            '🛵 Доставили за 5с!\n'


def test_command_order_pickup():
    runner = CliRunner()
    random.seed(5)
    result = runner.invoke(cli, ['order', 'pepperoni'])
    assert result.exit_code == 0
    assert result.output == 'bake - 50 c!\n'\
                            '🏠 Забрали за 5с!\n'


def test_command_order_pickup_large():
    runner = CliRunner()
    random.seed(5)
    result = runner.invoke(cli, ['order', 'pepperoni', 'l'])
    assert result.exit_code == 0
    assert result.output == 'bake - 30 c!\n'\
                            '🏠 Забрали за 5с!\n'
