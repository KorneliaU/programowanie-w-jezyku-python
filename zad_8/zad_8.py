def type_hinting(a: int, b: int, c: int) -> bool:
    return a + b >= c
result = type_hinting(3, 4, 7)
print(result)