import random
from typing import List


def selection_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i+1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers


if __name__ == '__main__':

    N = 10
    nums = [random.randint(0,1000) for i in range(N)]
    print(f'generated nums: {nums}')
    print(f'nums is sorted by selection sort: {selection_sort(nums)}')
