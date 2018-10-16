
def nways(text):
    if text == '':
        return 1
    if text.startswith('0'):
        return 0
    if int(text[:2]) > 26:
        return nways(text[1:])
    else:
        return nways(text[1:]) + nways(text[2:])


print(nways('12345'))
