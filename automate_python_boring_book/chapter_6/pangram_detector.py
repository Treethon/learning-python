def is_pangram(sentence):
    EACH_LETTER = []
    NOT_LETTERS = [' ',',','.']
    for char in sentence:
        if char.upper() not in NOT_LETTERS:
            if char.upper() not in EACH_LETTER:
                EACH_LETTER += char.upper()
    if len(EACH_LETTER) == 26:
        print('Is a pangram.')
    else:
        print('Is not a pangram.')

is_pangram('The quick brown fox jumps over the yellow lazy dog.')
is_pangram('This isnt')