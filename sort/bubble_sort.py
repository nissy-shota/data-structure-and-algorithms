from typing import List
import random

def bubble_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] < numbers[j+1]:
                # swap
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers

if __name__ == '__name__':

    array_length = 10
    nums = [random.randint(0,1000) for i in range(array_length)]

    print(f'generate numbers:{nums}')
    print(f'sorted by bubble sort:{bubble_sort(nums)}')