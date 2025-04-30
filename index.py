def binary_sum(number_1, number_2):
    number_1 = str(number_1)
    number_2 = str(number_2)
    sum_dec = int(number_1, base=2) + int(number_2, base=2)
    sum_bin = bin(sum_dec)
    result = sum_bin[2:]
    #result_str = str(result)
    return result

# Проверка

number_1 = '1101'
number_2 = '101'

print(binary_sum(number_1, number_2))