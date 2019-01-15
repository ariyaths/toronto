def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
    from math import ceil
    return ceil(n/50)


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    return sum(i for i in price_changes if i > 0), sum(j for j in price_changes
                                                       if j < 0)


def swap_k(L, k):
    """ (list, int) -> list

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> nums = swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [1, 2, 3, 4, 5, 6, 7]
    >>> nums = swap_k(nums, 3)
    >>> nums
    [5, 6, 7, 4, 1, 2, 3]
    """
    # return *L[len(L)-k:], *L[k:(len(L)-k)], *L[:k]
    list2 = []
    for a in range(len(L)-k, len(L)):
        list2.append(L[a])
    for b in range(k, (len(L)-k)):
        list2.append(L[b])
    for c in range(k):
        list2.append(L[c])
    return list2


if __name__ == '__main__':
    import doctest
    doctest.testmod()