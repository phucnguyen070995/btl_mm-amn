from fuction import *
arr = DocFile('plaintext.txt')
algo = int(input('Moi chon giai thuat encrypt (1-Caesar,2-Permutation,3-Mix):'))
if algo ==1:
    n = int(input('Moi nhap do dich chuyen :')) 
    for line in arr:
        # Ma hoa Caesar_cipher_encode
        cipher = Caesar_cipher_encode(line[0], n)
        LuuFile('ciphertext.txt', cipher)
    key = 'Do dich chuyen Caesar cipher la: ' + str(n) 
    LuuFile('key.txt', key)



elif algo ==2:
    permutation_Table = input('Moi nhap day hoan vi cho chuoi 8 ki tu (Ví dụ: 81726354): ')
    for line in arr:
        cut_string = cut_block_8words(line[0])
        # Hoán vị block 8 kí tự
        cipher = permutation_block(cut_string, permutation_Table)
        LuuFile('ciphertext.txt', cipher)
    key = 'Day hoan vi block 8 ki tu la: ' + permutation_Table
    LuuFile('key.txt', key)


elif algo ==3:
    n = int(input('Moi nhap do dich chuyen :')) 
    permutation_Table = input('Moi nhap day hoan vi cho chuoi 8 ki tu (Ví dụ: 81726354): ')
    for line in arr:
        # Ma hoa Caesar_cipher_encode
        cipher = Caesar_cipher_encode(line[0], n)
        cut_string = cut_block_8words(cipher)
        # Hoán vị block 8 kí tự
        cipher = permutation_block(cut_string, permutation_Table)
        LuuFile('ciphertext.txt', cipher)
    key = 'Do dich chuyen Caesar cipher la: ' + str(n) + '; ' + 'Day hoan vi block 8 ki tu la: ' + permutation_Table
    LuuFile('key.txt', key)
else:
    print('Giai thuat ma hoa ban mong muon khong ton tai')


