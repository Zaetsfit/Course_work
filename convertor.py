class Convertor:
    def convert(sequence):
        correct = []
        printable = '1234567890'
        nums = ''
        for token in sequence:
            if token in printable:
                nums += token
            elif nums:
                correct.append(int(nums))
                nums = ''
        return correct
