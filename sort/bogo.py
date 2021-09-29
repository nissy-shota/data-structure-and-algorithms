'''
適当に並べ替えてソートする．結構雑なSort？
非常に時間のかかるアルゴリズム．ランダムに並び替えるだけなので．．．
'''
import random
from typing import List

def in_order(numbers: List[int]) -> bool:
    # for i in range(len(numbers) - 1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))

def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

if __name__ == '__main__':
    numbers = [random.randint(0,1000) for _ in range(10)]
    print(f'input numbers: {numbers}')
    print(f'bogo sorted: {bogo_sort(numbers)}')