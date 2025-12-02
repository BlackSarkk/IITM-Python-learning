def ancestry(P, present, past):
    """
    A recursive function to compute the sequence of ancestors of person

    Arguments:
        P: dict, key and value are strings
        present: string
        past: string
    Return:
        result: list of strings
    """
    # Base case: if the present person *is* the past person
    # return a list with that single name.
    if present == past:
        return [present]

    # Recursive case:
    # Find the father of the current person, then continue upward.
    father = P[present]
    return [present] + ancestry(P, father, past)