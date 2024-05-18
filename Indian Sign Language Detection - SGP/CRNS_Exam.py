def decrypt_rail_fence(ciphertext, key):
    rail = [['\n' for j in range(len(ciphertext))] for i in range(key)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(ciphertext)):

        if row == 0 or row == key-1:
            dir_down = not dir_down
        rail[row][col] ='*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    index= 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if (rail[i][j] == '*') and (index < len(ciphertext)):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row,col = 0,0
    dir_down = None

    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    return ''.join(result)

ciphertext = "CBOANRELR E EAIEFT"
key = 4
decrypted_message = decrypt_rail_fence(ciphertext, key)
print("Input Text: ", ciphertext)
print("Decrypted message: ", decrypted_message)
