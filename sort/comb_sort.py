'''
comb -> クシ
gap = x / 1.3
gapを小さくしていく
'''


import random
from typing import List


def comb_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    swapped = True
    gap = len_numbers

    while gap != 1 or swapped:

        swapped = False
        gap = int(gap / 1.3)

        if gap < 1:
            gap = 1

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i], numbers[i+gap] = numbers[i+gap], numbers[i]
                swapped = True

    return numbers


if __name__ == '__main__':

    N = 10
    nums = [random.randint(0, 1000) for i in range(N)]
    print(f'generate nums: {nums}')
    print(f'nums is sorted by comb sort: {comb_sort(nums)}')
