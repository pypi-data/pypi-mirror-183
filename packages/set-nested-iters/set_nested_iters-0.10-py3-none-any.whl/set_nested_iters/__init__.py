import numpy as np
import functools


def preparedict(nestedlist):
    return {
        str(ergi) + repr(ergi)
        if not isinstance(ergi, int)
        else str(float(ergi)) + repr(float(ergi)): ergi
        for ergi in nestedlist
    }


def present_only_in_L1_reduce(L1, L2):
    return functools.reduce(
        lambda a, b: present_only_in_L1(a, b, withindex=False), L2, L1
    )


def present_only_in_L1(L1, L2, withindex=False):
    l1 = preparedict(L1)
    l2 = preparedict(L2)
    n1 = np.array(list(l1.keys()))
    n2 = np.array(list(l2.keys()))
    mask = np.isin(n1, n2, invert=True)
    indi = np.nonzero(mask)[0]
    if not withindex:
        return [x[1] for ini, x in enumerate(l1.items()) if np.isin(ini, indi)]
    return [(ini, x[1]) for ini, x in enumerate(l1.items()) if np.isin(ini, indi)]


def unique_in_each_list_reduce(L1, L2):
    return functools.reduce(
        lambda a, b: unique_in_L1_and_L2(a, b, withindex=False), L2, L1
    )


def unique_in_L1_and_L2(L1, L2, withindex=False):
    l1 = preparedict(L1)
    l2 = preparedict(L2)
    n1 = np.array(list(l1.keys()))
    n2 = np.array(list(l2.keys()))
    mask = np.isin(n1, n2, invert=True)
    indi = np.nonzero(mask)[0]
    if not withindex:
        r1 = [x[1] for ini, x in enumerate(l1.items()) if np.isin(ini, indi)]
    else:
        r1 = [(ini, x[1]) for ini, x in enumerate(l1.items()) if np.isin(ini, indi)]
    n1, n2 = n2, n1
    mask = np.isin(n1, n2, invert=True)
    indi = np.nonzero(mask)[0]
    if not withindex:
        r2 = [x[1] for ini, x in enumerate(l2.items()) if np.isin(ini, indi)]
    else:
        r2 = [(ini, x[1]) for ini, x in enumerate(l2.items()) if np.isin(ini, indi)]
    return r1 + r2


def present_in_all_lists_reduce(L1, L2):
    return functools.reduce(
        lambda a, b: present_in_L1_and_L2(a, b, withindex=False), L2, L1
    )


def present_in_L1_and_L2(L1, L2, withindex=False):
    l1 = preparedict(L1)
    l2 = preparedict(L2)
    n1 = np.array(list(l1.keys()))
    n2 = np.array(list(l2.keys()))
    mask = np.isin(n1, n2, invert=False)
    indi = np.nonzero(mask)[0]
    if not withindex:
        r1 = [x[1] for ini, x in enumerate(l1.items()) if np.isin(ini, indi)]
    else:
        r1 = [(ini, x[1]) for ini, x in enumerate(l1.items()) if np.isin(ini, indi)]
    return r1

