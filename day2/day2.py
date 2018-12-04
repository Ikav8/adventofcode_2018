# Part 1 #
def count_chars_in_id(id):
    char_count_list = []
    for char in set(id):
        char_count_list.append(id.count(char))
    return char_count_list


with open(file='day2_input.txt') as input:
    id_list = input.read().splitlines()
    id_with_char_twice_exactly = 0
    id_with_char_three_times_exactly = 0
    for id in id_list:
        char_count_for_id = count_chars_in_id(id)
        if 2 in char_count_for_id:
            id_with_char_twice_exactly += 1
        if 3 in char_count_for_id:
            id_with_char_three_times_exactly += 1

    print('Parte 1: ' + str(id_with_char_twice_exactly * id_with_char_three_times_exactly))

# Part 2 #
def count_differences_in_ids(id_list):
    for id1 in id_list:
        for id2 in id_list:
            if id1 != id2:
                number_of_differences = 0
                id_without_different_char = ''
                for char_id1, char_id2 in zip(list(id1), list(id2)):
                    if char_id1 != char_id2:
                        number_of_differences += 1
                    else:
                        id_without_different_char += char_id1
                    if number_of_differences > 1:
                        break
                if number_of_differences == 1:
                    print('Parte 2: ' + id_without_different_char)
                    return -1



with open(file='day2_input.txt') as input:
    id_list = input.read().splitlines()
    count_differences_in_ids(id_list)


