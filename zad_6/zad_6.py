def type_hinting(list_one: list, list_two: list) -> list:
    combined_list = list_one + list_two
    unique_list = []

    for value in combined_list:
        if value not in unique_list:
            unique_list.append(value)

    result = []
    for value in unique_list:
        result.append(value ** 3)

    return result
numbers_1 = [1, 2, 3, 4]
numbers_2 = [3, 4, 5, 6]
final_result = type_hinting(numbers_1, numbers_2)
print(final_result)