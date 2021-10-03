import random
from typing import List


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = temp

    return numbers


def bucket_sort(numbers: List[int]) -> List[int]:

    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    buckets = [[] for _ in range(size)]
    for num in range(numbers):
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[size-1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    results = []

    for i in range(size):
        results[i] += buckets[i]

    return results


if __name__ == '__main__':

    N = 10
    nums = [random.randint(0, 1000) for i in range(N)]
    print(f'generated nums: {nums}')
    print(f'nums is sorted by bucket sort: {bucket_sort(nums)}')
