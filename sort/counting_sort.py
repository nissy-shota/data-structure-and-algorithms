import random
from typing import List


def counting_sort(numbers: List[int]) -> List[int]:

    max_num = max(numbers)
    counts = [0] * (max_num + 1)
    results = [0] * len(numbers)

    for num in numbers:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        results[counts[index]-1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return results


if __name__ == '__main__':

    N = 10
    nums = [random.randint(0, 1000) for _ in range(N)]
    print(f'generated nums: {nums}')
    print(f'nums is sorted by counting sort {counting_sort(nums)}')
