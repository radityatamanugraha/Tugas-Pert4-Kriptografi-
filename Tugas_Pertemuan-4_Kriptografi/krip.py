def scytale_encrypt(text, key):
    text = text.replace(" ", "").upper()
    encrypted = [''] * key
    for i in range(len(text)):
        encrypted[i % key] += text[i]
    return ''.join(encrypted)


def scytale_decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    n = len(ciphertext)
    cols = n // key + (n % key != 0)
    decrypted = [''] * cols
    index = 0

    for i in range(key):
        for j in range(cols):
            if index < n:
                decrypted[j] += ciphertext[index]
                index += 1
    return ''.join(decrypted)


pesan = "HELLO WORLD"
kunci = 3

terenkripsi = scytale_encrypt(pesan, kunci)
terdekripsi = scytale_decrypt(terenkripsi, kunci)

print("Pesan asli   :", pesan)
print("Terenkripsi  :", terenkripsi)
print("Terdekripsi  :", terdekripsi)
