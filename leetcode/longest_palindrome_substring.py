def find_palindrome_at_index(word, i):
    palindrome = ''
    if i == len(word):
        return palindrome
    epalindrome, opalindrome = '', ''
    if word[i - 1] == word[i]:
        r, epalindrome = 1, word[i - 1:i + 1]
        while i + r < len(word) and i - r > 0:
            if word[i - r - 1] == word[i + r]:
                epalindrome = word[i - r - 1:i + r + 1]
                r += 1
                continue
            break
        # return palindrome
    r = 1
    while i + r < len(word) and i - r >= 0:
        if word[i - r] == word[i + r]:
            opalindrome = word[i - r:i + r + 1]
            r += 1
            continue
        break
    return epalindrome if len(epalindrome) > len(opalindrome) else opalindrome


def solve(word):
    m = int(len(word) / 2)
    longest_palindrome = ''
    for c in range(0, m + 1):
        palindrome = find_palindrome_at_index(word, m + c)
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
        palindrome = find_palindrome_at_index(word, m - c)
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
    print(longest_palindrome)


# solve('aquaabcdefedcba')
# solve('cbbd')
solve('aaaa')
