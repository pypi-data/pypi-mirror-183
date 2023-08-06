from check_if_nan import is_nan
import numpy as np

rng = np.random.default_rng()


def get_random_items_from_list(lst, size, replace=False, p=None, replace_raise=False):
    if len(lst) < size:
        if replace_raise is False:
            replace = True
        else:
            raise ValueError("len(lst) < size!!")
    if is_nan(p):
        fin = rng.choice(lst, size=size, replace=replace)
    else:
        fin = rng.choice(lst, size=size, replace=replace, p=p)
    return fin


def get_random_ints(low, high, size):
    return rng.integers(low, high, size=size)


def get_random_floats(low, high, size):
    return rng.uniform(low, high, size=size)


