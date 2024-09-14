CODE = {
    ' ':'_',
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..'
}
def convert_to_morse_code(sentence):
    encodedsentence = ''
    sentence = sentence.upper()
    for char in sentence:
        encodedsentence+=CODE[char]
    return encodedsentence
sentence = input('Enter sentence: ')
encodedSentence=convert_to_morse_code(sentence)
print(encodedSentence)