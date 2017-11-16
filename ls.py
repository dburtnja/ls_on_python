
files = [
    '0afasfasfsafasfasf',
    '1asdsadsadad',
    '2asdasdadadadsa',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '100'
]

console_width = 1


def get_index(from_list, index):
    try:
        return from_list[index]
    except IndexError:
        return None


def suit_in_console(lines, console_width, column_sizes):
    column_sizes += [max([len(get_index(line, column_number) or "") for line in lines]) + 2 for column_number in range(len(lines[0]))]
    line_size = sum(column_sizes) - 2
    return line_size <= console_width


def print_lines(lines, column_sizes):
    my_string_generator = lambda x, y: "".join(
        [('{:' + str(x[l]) + 's}' if l != len(x) - 1 else "{}") if get_index(y, l) else "" for l in range(len(x))])
    for line in lines:
        print(my_string_generator(column_sizes, line).format(*line))


lines = [files]
nbr_lines = 1

print("#" * console_width)
while True:
    lines = [files[i::nbr_lines] for i in range(nbr_lines)]
    column_sizes = []
    if suit_in_console(lines, console_width, column_sizes) or len(lines[0]) == 1:
        break
    nbr_lines += 1
print_lines(lines, column_sizes)

