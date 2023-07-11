# импортируем метод из модуля
from random import randint

# такая функция называется лямбдой
get_random_int = lambda min, max: randint(min, max)

print(f'Случайное целое число в диапазоне от 0 до 100: {get_random_int(0, 100)}')
