def type_hinting(number: int) -> bool:
    return number % 2 == 0
result = type_hinting(6)
if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")