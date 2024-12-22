def sum_of_integers(*args):
    numbers_list = list(args)
    total_sum = sum(numbers_list)
    return numbers_list, total_sum

result_list, result_sum = sum_of_integers(1, 2, 3, 4, 5)
print(f"列表: {result_list}, 和: {result_sum}")