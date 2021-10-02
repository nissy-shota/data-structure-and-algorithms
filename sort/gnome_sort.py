import random
from typing import List


def gnome_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    index = 0

    while index < len_numbers:
        if index == 0:
            index = index + 1
        if numbers[index] >= numbers[index-1]:
            index = index + 1
        else:
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            index = index - 1

    return numbers


if __name__ == '__main__':

    N = 10000000
    nums = [random.randint(0,1000) for i in range(N)]
    print(f'generated nums: {nums}')
    print(f'nums is sorted by gnome sort: {gnome_sort(nums)}')
