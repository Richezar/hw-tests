def check_age(age):
    if age >= 18:  # Введите условие для проверки возраста
        result = 'Доступ разрешeн'
    else:
        result = 'Доступ запрещeн'

    return result

def solution(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return 'корней нет'
    elif d == 0:
        return -b / (2 * a)
    elif d > 0:
        x_1 = (-b + d ** 0.5) / 2 * a
        x_2 = (-b - d ** 0.5) / 2 * a
        return (x_1, x_2)

def solve(phrases):
    result = [] # список палиндромов
    for phrase in phrases: # пройдите циклом по всем фразам
        clear_probel = phrase.replace(' ', '') # сохраните фразу без пробелов
        if clear_probel == phrase.replace(' ', '')[::-1]: # сравните фразу с ней же, развернутой наоборот (через [::-1])
            result.append(phrase)
    return result

