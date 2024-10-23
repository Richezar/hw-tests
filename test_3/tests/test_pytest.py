import pytest

from test_3.main import check_age, solution, solve

@pytest.mark.parametrize(
    'a,expected',
    (
        (18, 'Доступ разрешeн'),
        (17, 'Доступ запрещeн'),
        (19, 'Доступ разрешeн'),
        (35, 'Доступ разрешeн'),
    )
)
def test_check_age(a, expected):
    result = check_age(a)
    assert result == expected


@pytest.mark.parametrize(
    'a,b,c,expected',
    (
            (1, 8, 15, (-3.0, -5.0)),
            (1, -13, 12, (12.0, 1.0)),
            (-4, 28, -49, 3.5),
            (1, 1, 1, 'корней нет'),
    )
)
def test_solution(a, b, c, expected):
    result = solution(a, b, c)
    assert result == expected


@pytest.mark.parametrize(
    'a,expected', [
        (("нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза", "а собака боса", "тонет енот", "карман мрак", "пуст суп"), (['нажал кабан на баклажан', 'рвал дед лавр', 'азот калий и лактоза', 'а собака боса', 'тонет енот', 'пуст суп']))
    ]
)
def test_solve(a, expected):
    result = solve(a)
    assert result == expected