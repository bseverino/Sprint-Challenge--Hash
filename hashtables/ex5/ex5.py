def finder(files, queries):
    cache = {}
    result = []

    for file in files:
        filename = file.split('/')[-1]
        if filename not in cache:
            cache[filename] = [file]
        else:
            cache[filename].append(file)

    for query in queries:
        if query in cache:
            for file in cache[query]:
                result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
