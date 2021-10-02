'''
bubble sortとの違いは，swapフラグがあるので，フラグがFalseになった時点で，sort自体をやめられるので，多少早い可能性がある点．
'''


import random
from typing import List


def cocktail_sort(numbers: List[int]) -> List[int]:

    numbers_length = len(numbers)
    swapped = True
    start = 0
    end = numbers_length - 1

    while swapped:

        swapped = False

        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        if not swapped:
            break

        end = end - 1

        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start = start + 1

    return numbers


if __name__ == '__main__':
    array_length = 10
    nums = [random.randint(0, 1000) for i in range(array_length)]

    print(f'generate numbers:{nums}')
    print(f'nums is sorted by cocktail_sort: {cocktail_sort(nums)}')
