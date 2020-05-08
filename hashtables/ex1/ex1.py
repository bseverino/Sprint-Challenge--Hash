def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    for i in range(len(weights)):
        if limit - weights[i] in cache:
            print([i, cache[limit - weights[i]]])
            return [i, cache[limit - weights[i]]]
        if weights[i] not in cache:
            cache[weights[i]] = i

    return None

print(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21))