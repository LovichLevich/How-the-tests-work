def capitalize(text):
    if text == '':
        return ''
    first_chair = text[0].upper()
    rest_substring = text[1:]
    return f'{first_chair}{rest_substring}'