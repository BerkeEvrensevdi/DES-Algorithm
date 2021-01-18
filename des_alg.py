
hexa_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
              13: 'd', 14: 'e', 15: 'f'}


first_key_permutation_table = [57, 49, 41, 33, 25, 17,  9,
                               1, 58, 50, 42, 34, 26,  18,
                               10,  2, 59, 51, 43, 35, 27,
                               19, 11,  3, 60, 52, 44, 36,
                               63, 55, 47, 39, 31, 23, 15,
                               7, 62, 54, 46, 38, 30,  22,
                               14,  6, 61, 53, 45, 37, 29,
                               21, 13,  5, 28, 20, 12,  4]

sub_key_perm_table = [14, 17, 11, 24,  1,  5,
                      3,  28, 15,  6, 21, 10,
                      23, 19, 12,  4, 26,  8,
                      16,  7, 27, 20, 13,  2,
                      41, 52, 31, 37, 47, 55,
                      30, 40, 51, 45, 33, 48,
                      44, 49, 39, 56, 34, 53,
                      46, 42, 50, 36, 29, 32]

left_shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

msg_perm_table = [58, 50, 42, 34, 26, 18, 10, 2,
                  60, 52, 44, 36, 28, 20, 12, 4,
                  62, 54, 46, 38, 30, 22, 14, 6,
                  64, 56, 48, 40, 32, 24, 16, 8,
                  57, 49, 41, 33, 25, 17,  9, 1,
                  59, 51, 43, 35, 27, 19, 11, 3,
                  61, 53, 45, 37, 29, 21, 13, 5,
                  63, 55, 47, 39, 31, 23, 15, 7]


e_bit_selection_table = [32,  1,  2,  3,  4,  5,
                         4,   5,  6,  7,  8,  9,
                         8,   9, 10, 11, 12, 13,
                         12, 13, 14, 15, 16, 17,
                         16, 17, 18, 19, 20, 21,
                         20, 21, 22, 23, 24, 25,
                         24, 25, 26, 27, 28, 29,
                         28, 29, 30, 31, 32,  1]


sub_box_table = [[[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
                  [0,  15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
                  [4,   1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
                  [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]],
                 [[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
                  [3,  13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
                  [0,  14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
                  [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]],
                 [[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
                  [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
                  [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
                  [1,  10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]],
                 [[7,  13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
                  [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
                  [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
                  [3,  15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]],
                 [[2,  12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
                  [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
                  [4,   2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
                  [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]],
                 [[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
                  [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13,  14, 0, 11,  3,  8],
                  [9,  14, 15,  5,  2,  8, 12,  3,  7,  0,  4,  10, 1, 13, 11,  6],
                  [4,   3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]],
                 [[4,  11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
                  [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
                  [1,   4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
                  [6,  11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]],
                 [[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
                  [1,  15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
                  [7,  11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
                  [2,   1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]]


last_func_perm_table = [16,  7, 20, 21,
                        29, 12, 28, 17,
                        1,  15, 23, 26,
                        5,  18, 31, 10,
                        2,   8, 24, 14,
                        32, 27,  3,  9,
                        19, 13, 30,  6,
                        22, 11,  4, 25]


rev_msg_perm_table = [40, 8, 48, 16, 56, 24, 64, 32,
                      39, 7, 47, 15, 55, 23, 63, 31,
                      38, 6, 46, 14, 54, 22, 62, 30,
                      37, 5, 45, 13, 53, 21, 61, 29,
                      36, 4, 44, 12, 52, 20, 60, 28,
                      35, 3, 43, 11, 51, 19, 59, 27,
                      34, 2, 42, 10, 50, 18, 58, 26,
                      33, 1, 41,  9, 49, 17, 57, 25]


def ascii_to_binary(x):
    result = []
    for t in range(8):
        n = x % 2
        result.append(n)
        x = x//2

    result.reverse()
    return result


def binary_to_hex(x):
    result = []
    temp = []
    for i in range(len(x) - 1, -1, -1):
        temp.append(x[i])
        if i % 4 == 0:
            temp.reverse()
            p = binary_to_dec(temp)
            m = hexa_table[p]
            result += m

            temp = []
    result.reverse()

    return result


def binary_to_dec(x):
    result = 0

    for i in range(len(x)-1, -1, -1):
        result += x[i]*pow(2, ((len(x)) - (i + 1)))

    return result


def binary_to_str(x):
    arr = ''
    temp = []
    for i in range(len(x)):
        temp.append(x[i])
        if i % 8 == 7:
            decimal = binary_to_dec(temp)
            c = chr(decimal)
            arr += c
            temp = []

    return arr


def message_to_blocks(msg):
    msg_blocks = []
    k = []

    for i in range(len(msg)):

        k = k + ascii_to_binary(ord(msg[i]))
        if i % 8 == 7:
            msg_blocks.append(k)
            k = []

    if k:  # if k is not empty then the last block is not 64-bit

        empty_bytes = (64 - len(k)) // 8  # a char is 8 bit
        y = ascii_to_binary(empty_bytes)
        for i in range(empty_bytes):
            k += y
        msg_blocks.append(k)

    return msg_blocks


def key_to_binary(key):
    binary = []

    for i in range(len(key)):

        k = ascii_to_binary(ord(key[i]))
        binary += k

    return binary


def xor(x1, x2):

    result = []
    for i in range(len(x1)):
        if x1[i] != x2[i]:
            result.append(1)
        else:
            result.append(0)

    return result


def convert_with_permutation(original, perm_table):
    permutated = []
    for i in range(len(perm_table)):
        permutated.append(original[perm_table[i] - 1])
    return permutated


def left_round_shift(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = temp


def create_keys(key64b, shift_number_arr):
    keyb = key_to_binary(key64b)

    key = convert_with_permutation(keyb, first_key_permutation_table)  # 64 biti perm table ile 56 bite indirdik

    key1 = key[:len(key)//2]  # first half

    key2 = key[len(key)//2:]  # second half

    key_list = []
    for i in range(len(shift_number_arr)):

        for j in range(shift_number_arr[i]):
            left_round_shift(key1)
            left_round_shift(key2)  # left-shift for two halves

        merged_key = key1 + key2  # merge left shifted halves

        key_result = convert_with_permutation(merged_key, sub_key_perm_table)
        key_list.append(key_result)

    return key_list


def func(r, key_index):

    r_expanded = convert_with_permutation(r, e_bit_selection_table)  # we expanded right half to 48-bit, now we xor it with subkey1

    r_expanded_xor_subkey = xor(r_expanded, key_table[key_index])  # we xored expanded 48-bit key with subkey-i

    temp = []
    shrinked = []

    for i in range(len(r_expanded_xor_subkey)):
        temp.append(r_expanded_xor_subkey[i])

        if i % 6 == 5:
            row = [temp[0], temp[5]]
            col = temp[1:5]

            row_dec = binary_to_dec(row)

            col_dec = binary_to_dec(col)

            data = sub_box_table[i // 6][row_dec][col_dec]

            shrinked_data = ascii_to_binary(data)  # 6 bit to 4 bit
            shrinked_data = shrinked_data[4:]  # 6 bit to 4 bit

            shrinked += shrinked_data

            temp = []

    func_output = convert_with_permutation(shrinked, last_func_perm_table)

    return func_output


def des(msg_block):

    g = convert_with_permutation(msg_block, msg_perm_table)  # convert message block acc to perm table

    for i in range(16):

        left = g[:len(g) // 2]  # first half
        right = g[len(g) // 2:]  # second half and we will expand this to 48-bit

        func_out = func(right, i)

        new_right = xor(left, func_out)

        new_left = right

        g = new_left + new_right

    left = g[:len(g) // 2]
    right = g[len(g) // 2:]
    g = right + left
    result = convert_with_permutation(g, rev_msg_perm_table)

    return result


key64 = 'hello123'
z = key_to_binary(key64)

key_table = create_keys(key64, left_shift_table)

message = 'hello teacher!'

blocks = message_to_blocks(message)
end = []
for n in blocks:

    end += des(n)

end_str = binary_to_str(end)

print(end_str)

end_hex = binary_to_hex(end)

print('HEX VAL IS:')
hex_val = ""
for i in range(len(end_hex)):
    hex_val += end_hex[i]
    if i % 2 == 1:
        hex_val += ' '

print(hex_val)
