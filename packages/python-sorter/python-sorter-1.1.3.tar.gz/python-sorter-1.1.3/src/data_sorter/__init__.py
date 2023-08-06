import sys
from typing import Optional

from data_sorter.algos import *

sys.setrecursionlimit(10 ** 6)

g_algo_name: list = [
    'brick_sort',
    'bubble_sort',
    'comb_sort',
    'cycle_sort',
    'gnome_sort',
    'heap_sort',
    'insertion_sort',
    'intro_sort',
    'merge_sort',
    'quick_sort',
    'selection_sort',
    'stooge_sort',
    'strand_sort',
    'tree_sort'
]

def get_comparision(arr: list, algo_names: Optional[list]=[]) -> dict:
    if not algo_names:
        algo_names = g_algo_name
    result: dict = {}
    for algo_name in algo_names:
        result[algo_name] = getattr(sys.modules[__name__], algo_name)(arr)
    return result

# if __name__=='__main__':
#     arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # print(get_comparision(arr))
#     print(get_comparision(arr, ['bubble_sort', 'insertion_sort']))
#     print(get_comparision(arr, ['bubble_sort', 'insertion_sort', 'selection_sort']))