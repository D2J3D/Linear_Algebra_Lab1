import numpy as np
import math
import random


def encrypt_matrix_former(key_word, alphabet):
    m = round(math.sqrt(len(key_word)))  # matrix size
    encrypt_matrix = [[0] * m for i in range(m)]
    j, k = 0, 0
    for i in range(len(key_word)):
        k %= m
        encrypt_matrix[j][k] = alphabet.index(key_word[i])
        if (i + 1) % m == 0:
            j += 1
        k += 1
    return encrypt_matrix


def encrypt_matrix_checker(key_word, alphabet):
    encrypt_matrix = encrypt_matrix_former(key_word, alphabet)
    secret_word_candidate = ""
    n = len(encrypt_matrix)
    for i in range(n):
        for j in range(n):
            secret_word_candidate = secret_word_candidate + alphabet[encrypt_matrix[i][j]]
    return key_word == secret_word_candidate


def key_word_generator(alphabet, n):
    try:
        random_numbers = list(range(0, len(alphabet)))
        random.shuffle(random_numbers)
        key_word = ""
        for i in range(n**2):
            key_word += alphabet[random_numbers[i]]
        return key_word

    except ValueError:
        print(f"Не получится задать ключ длины n = {n}. Выбери меньшее значение n")


def word_to_vectors(word, alphabet, key_word):
    n = round(math.sqrt(len(key_word)))
    word_vectors = [[0]*n for _ in range(math.floor(len(word)/n)+1)]
    j, k = 0, 0
    for i in range(len(word)):
        k %= n
        word_vectors[j][k] = alphabet.index(word[i])
        k += 1
        if (i + 1) % n == 0:
            j += 1
    return word_vectors


def vector_to_word(word_vector, alphabet):
    word = ""
    for i in range(len(word_vector)):
        for j in range(len(word_vector[0])):
            word += alphabet[word_vector[i][j]]
    return word


def mod(vector, n):
    for i in range(len(vector)):
        vector[i] %= n
    return vector


def encrypt_word(encrypt_matrix, word_vectors, n):
    #print(encrypt_matrix, word_vectors, n)
    encrypt_matrix_arr = np.array(encrypt_matrix)
    word_arr = np.array(word_vectors)
    print("-----")
    print(encrypt_matrix)
    print("----")
    print(word_arr)
    print('-----')
    text_vector = np.zeros(shape=(len(word_arr), encrypt_matrix_arr.shape[1]), dtype=int)
    for i in range(word_arr.shape[0]):
        text_vector[i] = mod(np.dot(word_arr[i], encrypt_matrix_arr), n)
    return text_vector




if __name__ == "__main__":
    # setup
    custom_alphabet = "й ц у к е н г ш щ з х ъ ф ы в а п р о л д ж э я ч с м и т ь б ю , . _ !".split(" ")
    custom_alphabet.append(" ")
    custom_alphabet.sort()
    n = len(custom_alphabet)
    message = "ботай_матан!"
    random_key_word = key_word_generator(custom_alphabet, 3)
    custom_encrypt_matrix = encrypt_matrix_former(random_key_word, custom_alphabet)
    text = word_to_vectors(message, custom_alphabet, random_key_word)
    real_text = vector_to_word(text, custom_alphabet)
    print(encrypt_word(custom_encrypt_matrix, text, n))
