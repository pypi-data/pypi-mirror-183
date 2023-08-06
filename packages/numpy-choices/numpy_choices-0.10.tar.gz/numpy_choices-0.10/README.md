# Some useful np.random functions 

```python


$pip install numpy-choices
from numpy_choices import get_random_floats, get_random_ints, get_random_items_from_list

rand = get_random_items_from_list(
    list(range(1, 20)), size=10, replace=False, p=None, replace_raise=False
)
print(rand)
# [ 6 16 10  2  9  5 12 15  4 19]

print(get_random_ints(low=0, high=20, size=10))
# [ 0 14  3 14  3 11 15  0  4  5]

print(get_random_floats(low=0, high=20, size=10))
# [10.69714652  9.85398014  1.79753204 18.85165542  8.35101616  9.00431022
#   0.04652976  4.05292685 13.6940055   2.25818349]


    
```




