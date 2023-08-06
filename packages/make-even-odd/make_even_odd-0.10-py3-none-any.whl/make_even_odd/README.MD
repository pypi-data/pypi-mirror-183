# Make numbers even/odd

```python

from make_even_odd import make_even_ceil, make_even_floor, make_odd_ceil, make_odd_floor
print(list(make_even_ceil(*[198, 7, 12, 3])))
print(list(make_even_floor(*[198, 7, 12, 2, 1])))
print(list(make_odd_ceil(*[198, 7, 12, 3])))
print(list(make_odd_floor(*[198, 7, 12, 2, 1])))

[198, 8, 12, 4]
[198, 6, 12, 2, 0]
[199, 7, 13, 3]
[197, 7, 11, 1, 1]


```


