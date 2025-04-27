# Задание 1.
# Вам дана последовательность уникальных чисел и вы должны
# подсчитать число инверсий в этой последовательности.
# Для списка [1, 2, 5, 3, 4, 7, 6] число инверсий равно 3.

def count_inversions(list, min):
    count = 0
    for i, number in enumerate(list, start=min):
        print(i, number)
        if number > i:
            count += number - i
    return f'число инверсий равно {count}'

list = [1, 2, 5, 3, 4, 7, 6]
min = min(list)
print(count_inversions(list, min))