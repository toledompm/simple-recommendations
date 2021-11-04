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

    count = 0

    for transaction_items in transactions.values():
        if first_item in transaction_items:
            count += 1

    return __count_frequence(transactions, itemset) / count


def __count_frequence(transactions: dict[int, set[int]], itemset: set[int]):
    count = 0

    for items in transactions.values():
        if itemset.issubset(items):
            count += 1

    return count
