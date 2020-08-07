def LuuFile(path, data):
    file = open(path, 'a', encoding = 'utf-8')
    file.writelines(data)
    file.writelines('\n')
    file.close()

def DocFile(path):
    arrSo = []
    file = open(path, 'r', encoding= 'utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(';')
        arrSo.append(arr)
    file.close()
    return arrSo

def Caesar_cipher_encode(plaintext, n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '
    # for i in range(1, 26):
    cipher = ''
    for a in plaintext:
        cipher += alphabet[(alphabet.index(a) + n) % 63]
    return cipher

def cut_block_8words(s):
    arr = []
    while len(s) != 0:
        block = ''
        if len(s) > 8:
            block = s[:8]
        else: block = s
        s = s[8:]
        arr.append(block)
    return arr

def permutation_block(arr, permutation_Table):
    res = []
    permutation_num = []
    for num in permutation_Table:
        permutation_num.append(int(num))
    for block in arr:
        if (len(block) == 8):
            sub_res = ''
            for i in range(8):
                sub_res += block[permutation_num[i] - 1]
            res.append(sub_res)
        else: res.append(block)
    return ''.join(res)

