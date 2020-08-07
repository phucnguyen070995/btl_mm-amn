from fuction import *
from itertools import permutations
arr = DocFile('ciphertext.txt')
# Giai ma Caesar_cipher_encode
res = []
caesar_key = []
for i in range(63):
    count_space = 0
    sub_res = []
    for line in arr:
        line_plaintext = Caesar_cipher_encode(line[0], i)
        count_space += line_plaintext.count(' ')
        sub_res.append(line_plaintext)
    if count_space > 100:
        caesar_key.append(i)
        for line in sub_res:
            res.append(line)

LuuFile('hack_key.txt', 'Danh sach key Caesar key co the:')
for key in caesar_key:
    LuuFile('hack_key.txt', str(63 - key))
# Lay list common word
arr = DocFile('common_words_list.txt')
word_list = []
for word in arr:
    word_list.append(word[0])

# Hoan vi 8 so tao 40320 key
find_key = []
result = []
permutation_Table_list = list(permutations([1, 2, 3, 4, 5, 6, 7, 8]))
for key in permutation_Table_list:
    key = ''.join(str(a) for a in list(key))
    find_common_word = 0
    sub_res = []
    for line in res:
        cut_string = cut_block_8words(line)
        # Hoán vị block 8 kí tự
        plaintext = permutation_block(cut_string, key)
        plaintext = ''.join(plaintext)
        sub_res.append(plaintext)
        for word in word_list:
            find_common_word += plaintext.count(' ' + word + ' ')

    if find_common_word > 75:
        find_key.append(key)
        for line in sub_res:
            result.append(line)

LuuFile('hack_key.txt', 'Danh sach permutation key co the:')
for key in find_key:
    res_key = ''
    for i in range(1,9):
        res_key += str(key.index(str(i)) + 1)
    LuuFile('hack_key.txt', res_key)
for line in result:
    LuuFile('hack_plaintext.txt', line)