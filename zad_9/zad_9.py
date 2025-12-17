def type_hinting(values: list, number: int) -> bool:
    return number in values
numbers = [1, 2, 3, 4, 5]
result = type_hinting(numbers, 3)
print(result)