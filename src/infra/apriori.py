def support(
    first_item: int, second_item: int, transactions: dict[int, set[int]]
) -> float:
    """
    Returns the support of an itemset in a list of transactions.
    """
    if len(transactions.keys()) == 0:
        return 0

    itemset = set([first_item, second_item])
    return __count_frequence(transactions, itemset) / len(transactions.keys())


def confidence(
    first_item: int, second_item: int, transactions: dict[int, set[int]]
) -> float:
    """
    Returns the confidence of an itemset in a list of transactions.
    """
    if len(transactions.keys()) == 0:
        return 0

    itemset = set([first_item, second_item])

    first_item_frequence = __count_frequence(transactions, set([first_item]))
    
    if first_item_frequence == 0:
        return 0

    return __count_frequence(transactions, itemset) / first_item_frequence


def __count_frequence(transactions: dict[int, set[int]], itemset: set[int]):
    count = 0

    for items in transactions.values():
        if itemset.issubset(items):
            count += 1

    return count
