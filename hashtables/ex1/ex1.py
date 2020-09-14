def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    w_dict = {} # setting up my dictionary

    for i, weight in enumerate(weights):
        if weight not in w_dict:
            w_dict[weight] = i

        else:
            if weight + weight == limit:
                return (i, w_dict[weight])

    for weight in weights:
        diff = limit - weight
        if diff in w_dict:
            return (w_dict[diff], w_dict[weight])

    return None

#* ALL TESTS PASSED
