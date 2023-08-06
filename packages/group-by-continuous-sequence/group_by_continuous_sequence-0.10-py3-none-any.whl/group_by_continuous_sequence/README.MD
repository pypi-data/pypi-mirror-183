# Group lists/NumPy arrays by continuous sequence

```python
$pip install group-by-continuous-sequence
import numpy as np
import random
from group_by_continuous_sequence import search_sequence_in_list, search_sequence_in_list_with_repeated_numbers, find_sequence_in_np_array

iterable = random.choices(range(2, 6), k=1000)


# Out[4]: [4, 3, 4, 2, 3, 2, 3, 3, 4, 5, 2, 5, 2, 2, 2, 3, 4, 4, 4, 2, 3, 3, 5, 4, 4, 2, 5, 4 ...]

# Find groups of consecutive items. (no difference between the numbers in this case) - first number in the tuple is the index, the second is the value
#
a1 = search_sequence_in_list(
    iterable, difference=0, return_index=True, return_values=True
)
# [[(0, 4)],
#  [(1, 3)],
#  [(2, 4)],
#  [(3, 2)],
#  [(4, 3)],
#  [(5, 2)],
#  [(6, 3), (7, 3)],
#  [(8, 4)],
#  [(9, 5)],
#  [(10, 2)],
#  [(11, 5)],
#  [(12, 2), (13, 2), (14, 2)],
#  [(15, 3)],
#  [(16, 4), (17, 4), (18, 4)],
#  [(19, 2)],
#  [(20, 3), (21, 3)],
#  [(22, 5)],
#  [(23, 4), (24, 4)],
#  [(25, 2)],
#  [(26, 5)],
#  [(27, 4), (28, 4)],
#  [(29, 3)],
#  [(30, 2)],
#  [(31, 4)],
#  [(32, 5), (33, 5)],
#  [(34, 2)],
#  [(35, 4), (36, 4)]
#  ...


# (difference of 1 between consecutive numbers) - only index

a2 = search_sequence_in_list(
    iterable, difference=1, return_index=True, return_values=False
)
# [[0],
#  [1, 2],
#  [3, 4],
#  [5, 6],
#  [7, 8, 9],
#  [10],
#  [11],
#  [12],
#  [13],
#  [14, 15, 16],
#  [17],
#  [18],
#  [19, 20],
#  [21],
#  [22],
#  [23],
#  [24],
#  [25],
#  [26],
#  [27],
#  [28],
#  [29],
#  [30],
#  [31, 32],
#  ...


# (difference of 2 between consecutive numbers) - only values

a3 = search_sequence_in_list(
    iterable, difference=2, return_values=True, return_index=False
)
# ...
# [4],
# [4],
# [2],
# [3],
# [3, 5],
# [4],
# [4],
# [2],
# [5],
# [4],
# [4],
# [3],
# [2, 4],
# [5],
# [5],
# [2, 4],
# [4],
# [2],
# [5],
# [3],
# [2, 4],
# [3, 5],
# [2],
# [5],
# [5],
# [2, 4],
# ...


# (difference of 3 between consecutive numbers) - only values

a4 = search_sequence_in_list(
    iterable, difference=3, return_values=True, return_index=False
)
# [[4],
#  [3],
#  [4],
#  [2],
#  [3],
#  [2],
#  [3],
#  [3],
#  [4],
#  [5],
#  [2, 5],
#  [2],
#  [2],
#  [2],
#  [3],
#  [4],
#  [4],
#  [4],
#  [2],
#  [3],
#  [3],
#  [5],
#  [4],
#  [4],
#  [2, 5],
#  [4],
#  [4],
#  [3],
#  [2],
#  [4],
#  [5],
#  [5],
#  [2],
#  [4],
#  [4],
#  [2, 5] ...]


# ((19, 2), (20, 3), (21, 3)) # Includes repeated numbers
# if ignore_only_repeated is True: Matches like: [(1,4), (1,4)] will be ignored, because there
# is only one hit (4)

a21 = search_sequence_in_list_with_repeated_numbers(
    iterable,
    difference=1,
    return_index=True,
    return_values=True,
    ignore_only_repeated=True,
)

# [(0, 4),
#  ((1, 3), (2, 4)),
#  ((3, 2), (4, 3)),
#  ((5, 2), (6, 3), (7, 3), (8, 4), (9, 5)),
#  (10, 2),
#  (11, 5),
#  ((12, 2), (13, 2), (14, 2), (15, 3), (16, 4), (17, 4), (18, 4)),
#  ((19, 2), (20, 3), (21, 3)),
#  (22, 5),
#  (23, 4),
#  (24, 4),
#  (25, 2),
#  (26, 5),
#  (27, 4),
#  (28, 4),
#  (29, 3),
#  (30, 2),
#  ((31, 4), (32, 5), (33, 5)),
#  (34, 2), ...
#

# difference of 2 between consecutive numbers), accepting a repeated unique number  ([2, 2, 2], [4, 4, 4] ...)
a31 = search_sequence_in_list_with_repeated_numbers(
    iterable,
    difference=2,
    return_index=False,
    return_values=True,
    ignore_only_repeated=False,
)

# [3, 3],
# [4],
# [5],
# [2],
# [5],
# [2, 2, 2],
# [3],
# [4, 4, 4],
# [2],
# [3, 3, 5],
# [4, 4],
# [2],
# [5],
# [4, 4],
# [3],
# [2, 4],
# [5, 5],
# [2, 4, 4],
# [2],
# [5],
# [3],
# [2, 4],
# [3, 5],
# [2],
# [5, 5],
# [2, 4],
# [2],
# [3],
# [4],
# [3, 3],
# [2, 2, 2],


# difference of 2 between consecutive numbers), not accepting a repeated unique number  ([2, 2, 2], [4, 4, 4] ...)

a41 = search_sequence_in_list_with_repeated_numbers(
    iterable,
    difference=3,
    return_index=True,
    return_values=True,
    ignore_only_repeated=True,
)

# (767, 5),
# ((768, 2), (769, 5), (770, 5)),
# (771, 2),
# (772, 3),
# (773, 2),
# (774, 2),
# (775, 3),
# (776, 3),
# (777, 2),
# (778, 4),
# (779, 5),
# (780, 3),
# (781, 4),
# ((782, 2), (783, 2), (784, 5)),
# (785, 4),
# (786, 5),
# (787, 5),
# (788, 4),
# (789, 4),
# ((790, 2), (791, 5)),
# (792, 3),
# (793, 2),
# (794, 4),
# (795, 4),
# ((796, 2), (797, 5)),
# (798, 2),
# (799, 4),
# (800, 4),
# (801, 2),
# (802, 4),
# ((803, 2), (804, 2), (805, 5)),
# (806, 3),
# (807, 5),
# (808, 4),
# ((809, 2), (810, 2), (811, 5), (812, 5), (813, 5)),
# (814, 4),
# (815, 4),
# (816, 3),

# if inonline is True: all values are in one row [1,2,3,4,5,6,7,8] instead of [[1,2,3,4],[5,6,7,8]]
m = find_sequence_in_np_array(np.asarray(iterable), [3, 4, 5])


# [{'inoneline': True,
#   'location': array([[7],
#          [8],
#          [9]], dtype=int64),
#   'values': [3, 4, 5]},
#  {'inoneline': True,
#   'location': array([[85],
#          [86],
#          [87]], dtype=int64),
#   'values': [3, 4, 5]},
#  {'inoneline': True,
#   'location': array([[176],
#          [177],
#          [178]], dtype=int64), ...

# Works with nested arrays too
m = find_sequence_in_np_array(np.asarray(iterable).reshape((10, 10, 10)), [3, 4, 5])
# m
# Out[28]:
# [{'inoneline': True,
#   'location': array([[0, 0, 7],
#          [0, 0, 8],
#          [0, 0, 9]], dtype=int64),
#   'values': [3, 4, 5]},
#  {'inoneline': True,
#   'location': array([[0, 8, 5],
#          [0, 8, 6],
#          [0, 8, 7]], dtype=int64),
#   'values': [3, 4, 5]},
#  {'inoneline': True,
#   'location': array([[1, 7, 6],
#          [1, 7, 7],
#          [1, 7, 8]], dtype=int64),

# and also with strings
m = find_sequence_in_np_array(
    np.asarray(iterable).reshape((10, 10, 5, 2)).astype(str), ["3", "4", "5"]
)
# [{'inoneline': False,
#   'location': array([[0, 0, 3, 1],
#          [0, 0, 4, 0],
#          [0, 0, 4, 1]], dtype=int64),
#   'values': ['3', '4', '5']},
#  {'inoneline': False,
#   'location': array([[0, 8, 2, 1],
#          [0, 8, 3, 0],
#          [0, 8, 3, 1]], dtype=int64),
#   'values': ['3', '4', '5']},
#  {'inoneline': False,
#   'location': array([[1, 7, 3, 0],
#          [1, 7, 3, 1],
#          [1, 7, 4, 0]], dtype=int64),
#   'values': ['3', '4', '5']},

```
