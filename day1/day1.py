# Part 1 #
frequency = 0
with open(file='day1_input.txt') as input:
    frequency_changes = input.read().splitlines()
    for change in frequency_changes:
        frequency += int(change)

    print('Parte 1: ' + str(frequency))

# Part 2 #
frequency = 0
frequency_list = [frequency]
with open(file='day1_input.txt') as input:
    frequency_changes = input.read().splitlines()
    is_reached_twice = False
    while not is_reached_twice:
        for change in frequency_changes:
            frequency += int(change)
            if frequency in frequency_list:
                print('Parte 2: ' + str(frequency))
                is_reached_twice = True
                break
            else:
                frequency_list.append(frequency)


