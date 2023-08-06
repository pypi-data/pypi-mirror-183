# Drops duplicates from nested list 

```python
$pip install drop-duplicates-nested-list

from drop_duplicates_nested_list import drop_duplicates
L = ['a', ['aa', 'a'] ,'a',['aa', 'a'] ,['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h',['bb', ['ccc', 'ddd'], 'ee', 'ff']]

print(drop_duplicates(L))
['a', ['aa', 'a'], ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']

```




