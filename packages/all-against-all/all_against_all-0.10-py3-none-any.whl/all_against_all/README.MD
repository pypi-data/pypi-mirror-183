# Each item of a list against all others

```python
$pip install all-against-all
from all_against_all import all_against_all
import operator

list_ = [1, 2, 3, 4]


e = all_against_all(
    func=operator.add, iterable=list_, ignore_exceptions=True, skip_own=True
)
e = list(e)
for ee in e:
    print(ee)


# [((1, 2), 3), ((1, 3), 4), ((1, 4), 5)]
# [((2, 1), 3), ((2, 3), 5), ((2, 4), 6)]
# [((3, 1), 4), ((3, 2), 5), ((3, 4), 7)]
# [((4, 1), 5), ((4, 2), 6), ((4, 3), 7)]


e = all_against_all(
    func=operator.add, iterable=list_, ignore_exceptions=True, skip_own=False
)
e = list(e)
for ee in e:
    print(ee)


# [((1, 2), 3), ((1, 3), 4), ((1, 4), 5)]
# [((2, 1), 3), ((2, 3), 5), ((2, 4), 6)]
# [((3, 1), 4), ((3, 2), 5), ((3, 4), 7)]
# [((4, 1), 5), ((4, 2), 6), ((4, 3), 7)]
# [((1, 1), 2), ((1, 2), 3), ((1, 3), 4), ((1, 4), 5)]
# [((2, 1), 3), ((2, 2), 4), ((2, 3), 5), ((2, 4), 6)]
# [((3, 1), 4), ((3, 2), 5), ((3, 3), 6), ((3, 4), 7)]
# [((4, 1), 5), ((4, 2), 6), ((4, 3), 7), ((4, 4), 8)]


```
