class Convertor(object):
    def convert(sequence):
        big_letters = [chr(letter + 65) for letter in range(26)]
        small_letters = [chr(letter + 97) for letter in range(26)]
        symbols = '}{!@#$%^&(/)-_+=;:]['
        for element in sequence:
            if element in big_letters or element in small_letters or element in symbols:
                return False
        try:
            numbers_sequence = list(map(float, sequence.split(',')))
            return numbers_sequence
        except Exception:
            return False
