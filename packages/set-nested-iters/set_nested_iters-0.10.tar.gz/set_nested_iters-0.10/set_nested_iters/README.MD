# Finds intersections/differences in nested iterables  


```python
# Tested with:
# Python 3.9.13
# Windows 10


$pip install set-nested-iters


from set_nested_iters import (
    present_in_L1_and_L2,
    present_in_all_lists_reduce,
    unique_in_L1_and_L2,
    unique_in_each_list_reduce,
    present_only_in_L1,
    present_only_in_L1_reduce,
)
L0 = [{2, 5}, "a", 44, "jojjo", "xxx", {77: 100}]
L1 = [
    {2, 5},
    "a",
    ["bb", ["ccc", "ddd"], "ee", "ff"],
    "g",
    "h",
    "g",
    "h",
    3,
    4,
    5,
    0.0,
    1,
]
L2 = [
    {2, 5},
    "ac",
    (98, 11),
    ["bb", ["ccc", "ddd"], "ee", "ff"],
    "gc",
    "h",
    "gc",
    "h",
    11,
    2,
    3,
    1.0,
    0.0,
]
L3 = [
    {2, 5},
    "a",
    44,
    ["bb", ["ccc", "ddd"], "ee", "ff"],
    "g",
    "h",
    "g",
    "h",
    3,
    4,
    5,
    0.0,
    1,
]
L4 = [
    {2, 5},
    "ac",
    111112,
    (98, 11),
    ["bb", ["ccc", "ddd"], "ee", "ff"],
    "gc",
    "a",
    "h",
    "gc",
    "h",
    11,
    2,
    3,
    1.0,
    0.0,
]
erg0 = present_only_in_L1(L1, L2, withindex=False)
print(erg0)
erg1 = present_only_in_L1(L2, L1, withindex=False)
print(erg1)
erg2 = unique_in_L1_and_L2(L1, L2, withindex=False)
print(erg2)
erg3 = present_in_L1_and_L2(L1, L2, withindex=False)
print(erg3)
erg0 = present_only_in_L1(L1, L2, withindex=True)
print(erg0)
erg1 = present_only_in_L1(L2, L1, withindex=True)
print(erg1)
erg2 = unique_in_L1_and_L2(L1, L2, withindex=True)
print(erg2)
erg3 = present_in_L1_and_L2(L1, L2, withindex=True)
print(erg3)
print(present_in_all_lists_reduce(L1, [L2, L3, L4]))
print(unique_in_each_list_reduce(L1, [L2, L3, L4, L0]))
print(present_only_in_L1_reduce(L0, [L2, L3, L4, L1]))



['a', 'g', 4, 5]
['ac', (98, 11), 'gc', 11, 2]
['a', 'g', 4, 5, 'ac', (98, 11), 'gc', 11, 2]
[{2, 5}, ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'h', 3, 0.0, 1]
[(1, 'a'), (3, 'g'), (6, 4), (7, 5)]
[(1, 'ac'), (2, (98, 11)), (4, 'gc'), (6, 11), (7, 2)]
[(1, 'a'), (3, 'g'), (6, 4), (7, 5), (1, 'ac'), (2, (98, 11)), (4, 'gc'), (6, 11), (7, 2)]
[(0, {2, 5}), (2, ['bb', ['ccc', 'ddd'], 'ee', 'ff']), (4, 'h'), (5, 3), (8, 0.0), (9, 1)]
[{2, 5}, ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'h', 3, 0.0, 1]
[111112, {2, 5}, 'jojjo', 'xxx', {77: 100}]
['jojjo', 'xxx', {77: 100}]
	
```




