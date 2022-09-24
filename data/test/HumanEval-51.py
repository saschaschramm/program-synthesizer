def remove_vowels(text):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        text = text.replace(vowel, "")
    return text


METADATA = {}


def check(candidate):
    assert candidate('') == ''
    assert candidate("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert candidate('fedcba') == 'fdcb'
    assert candidate('eeeee') == ''
    assert candidate('acBAA') == 'cB'
    assert candidate('EcBOO') == 'cB'
    assert candidate('ybcd') == 'ybcd'


check(remove_vowels)