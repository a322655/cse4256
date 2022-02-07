"""Homework 3 Template

This is the template for HW3 in CSE 4256 at The Ohio State University.
"""


# TODO
# Besides the syntax used to create them, what are three fundamental differences
# between a Python \lstinline{set} and a Python \lstinline{list}?
# 1.
# 2.
# 3.

def all_unique(ls: list) -> bool:
    """Reports whether the list contains all unique elements.

    Positional Arguments:
    ls -- A list of hashable items, such as ints.
    """

    return len(set(ls)) == len(ls)


def maybe_apply_all(s: set, f=lambda x: x + 5):
    """Applies function f to each element of s, updating s in place."""

    for x in s:
        x = f(x)


# TODO
# Is this function correct according to the docstring? If not, what's wrong?
# Answer:


def apply_all(s: set, f=lambda x: x + 5):
    """Applies function f to each element of s, updating s in place."""

    s = set(map(f, s))


# TODO
# Does your solution to apply_all(s, f) work for all f?
# Answer:


def subset_sum(s: set, t: int) -> bool:
    """Solves the Subset Sum problem.

    Returns True iff there is a subset of s whose sum is equal to t.

    Positional arguments:
    s -- A set of integers.
    t -- The target sum.
    """

    # TODO
    pass


def is_subset_sum(sub: set, s: set, t: int) -> bool:
    """Checks a proposed solution to the Subset Sum Problem.

    Returns True iff sub is a subset of s and the sum of the elements of s is
    equal to t.

    Positional arguments:
    sub -- A set of integers; the proposed subset.
    s -- A set of integers.
    t -- The target sum.
    """

    # TODO
    pass


# **********************
#  Challenge Activities
# **********************


def subset_sum_approx(s: set, t: int) -> bool:
    """Approximates the Subset Sum problem.

    Returns True iff there is a subset of s whose sum is approximately t.

    Positional arguments:
    s -- A set of integers.
    t -- The target sum.
    """

    # TODO
    pass


def subset_sum_dyn(s: set, t: int) -> bool:
    """Solves the Subset Sum problem using dynamic programming.

    Returns True iff there is a subset of s whose sum is approximately t.
    Implemented using Dynamic Programming.

    Positional arguments:
    s -- A set of integers.
    t -- The target sum.
    """

    # TODO
    pass


def subset_sum_h_s(s: set, t: int) -> bool:
    """Solves the Subset Sum problem using the Horowitz-Sahni algorithm.

    Returns True iff there is a subset of s whose sum is approximately t.
    Implemented using the Horowitz-Sahni algoritm.

    Positional arguments:
    s -- A set of integers.
    t -- The target sum.
    """

    # TODO
    pass
