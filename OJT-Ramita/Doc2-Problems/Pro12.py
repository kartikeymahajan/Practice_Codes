'''12. Write a function called parse_ranges, which accepts a string containing ranges of
numbers and returns an iterable of those numbers.
Ex: >>> parse_ranges('1-2,4-4,8-13')
[1, 2, 4, 8, 9, 10, 11, 12, 13]'''


def parse_ranges(ranges_string):
    ranges = ranges_string.split(",")
    output = []

    for i in ranges:
        if "-" not in i:
            output.append(int(i))
        else:
            start, stop = i.split("-")
            for x in range(int(start), int(stop)+1):
                output.append(x)
    return output

obj = parse_ranges('1-2,4-4,8-15')
print(obj)