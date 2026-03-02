def reverse_list(items):
    return items[::-1]

def count_occurrences(items, value):
    return items.count(value)

data = [1, 2, 3, 2, 4, 2]

print("Reversed:", reverse_list(data))
print("Count of 2:", count_occurrences(data, 2))
