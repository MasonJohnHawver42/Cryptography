from CaesarCipher2 import CaesarCipher
from Constants import Constants


def test_encode_decode():
    correct_num = 0
    incorrect_num = 0

    for letter in Constants.ALPHABET:
        for shift in range((len(Constants.ALPHABET) * 2) + 1):
            encoded_mesage = CaesarCipher.encode(letter, shift)
            if CaesarCipher.decode(encoded_mesage, shift) == letter:
                correct_num += 1
            else:
                incorrect_num += 1

    return correct_num, incorrect_num

