'''
Author: Mason Hawver
Description:
This is a static Class with the purpose to replicate the caesar cipher in python code
'''

from Constants import Constants
ALPHABET = Constants.ALPHABET


class CaesarCipher:

    @staticmethod
    # @message just give it a message you want to encrypt
    # @shift that is the amount each letter is shifted (any int wil work as input)
    def encode(message, shift):
        encoded_message = ""

        # note fixes shift input
        if shift > 26:
            shift = shift - (26 * int(shift/26))

        # note: only encodes letters in alphabet
        for char in message:
            if char.lower() in Constants.ALPHABET:
                encoded_alphabet_index = ALPHABET.find(char.lower()) + shift

                if encoded_alphabet_index >= len(Constants.ALPHABET):
                    encoded_alphabet_index = encoded_alphabet_index - (len(Constants.ALPHABET) * int(encoded_alphabet_index / len(Constants.ALPHABET)))

                encoded_char = ALPHABET[encoded_alphabet_index]

                if char.isupper():
                    encoded_char = encoded_char.upper()

                encoded_message += encoded_char
            else:
                encoded_message += char

        # @ return gives encoded message
        return encoded_message

    @staticmethod
    # @encoded_message give encoded message
    # @shift give the shift you belive the message is encoded with
    def decode(encoded_message, shift):
        message = ""

        if shift > 26:
            shift = shift - (26 * int(shift/26))

        for char in encoded_message:
            if char.lower() in Constants.ALPHABET:

                alphabet_index = ALPHABET.find(char.lower()) - shift

                decoded_char = ALPHABET[alphabet_index]
                if char.isupper():
                    decoded_char = decoded_char.upper()
                message += decoded_char
            else:
                message += char

        # @return gives the message (note the shift may not be right)
        return message

    @staticmethod
    # @encoded_message give encoded message no shift needed
    def brute_force(encoded_message):
        def find_letter_frequency(string):

            letter_frequency = {}
            for letter in string:
                if letter.lower() in Constants.LETTER_FREQUENCY:
                    if letter in letter_frequency:
                        letter_frequency.update({letter: letter_frequency[letter] + 1})
                    else:
                        letter_frequency.update({letter: 1})

            return letter_frequency

        def find_letter_frequency_error(letter_frequency, string):
            error = 0
            for letter in Constants.ALPHABET:
                if letter in letter_frequency:
                    error += abs(((letter_frequency[letter] / len(string)) * 100) - Constants.LETTER_FREQUENCY[letter])

            return error

        possible_messages = {}
        for shift in range(len(Constants.ALPHABET)):
            possible_message = CaesarCipher.decode(encoded_message, shift)
            error = find_letter_frequency_error(find_letter_frequency(possible_message), possible_message)
            possible_messages.update({possible_message: error})

        sorted_possible_messages = {}
        for message in sorted(possible_messages, key=possible_messages.__getitem__):
            sorted_possible_messages.update({message: possible_messages[message]})

        # @return gives a dictionary sorted by there error(the error is the variation of letter frequency)
        return sorted_possible_messages

