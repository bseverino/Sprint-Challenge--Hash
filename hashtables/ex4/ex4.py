def has_negatives(a):
    cache = {}
    result = []

    for i in a:
        if i not in cache:
            if i > 0:
                cache[f'positive {i}'] = i
            elif i < 0:
                cache[f'negative {-i}'] = i
        if i > 0:
            if f'negative {i}' in cache:
                result.append(i)
        if i < 0:
            if f'positive {-i}' in cache:
                result.append(cache[f'positive {-i}'])

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
