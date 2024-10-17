def my_range(start, stop, step=1):
    result = []
    while start < stop:
        result.append(start)
        start += step
    return result

def my_enumerate(iterable, start=0):
    result = []
    i = start
    for value in iterable:
        result.append((i, value))
        i += 1
    return result

def while_enumerate(iterable, start=0):
    result = []
    i = 0
    while i < len(iterable):
        result.append((i + start, iterable[i]))
        i += 1
    return result

def my_zip(*iterables):
    result = []
    for i in range(0, len(iterables)):
        subresult = []
        for value in iterables:
            subresult.append(value[i])
        result.append(tuple(subresult))

    return result

#print(my_range(1, 10, 1))
#print(my_enumerate("ahoj"))
print(list(zip([1, 2, 3], [1, 2, 3], ['a', 'b', 'c'])))
print(my_zip([1, 2, 3], [1, 2, 3], ['a', 'b', 'c']))