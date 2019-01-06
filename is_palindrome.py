def reverse(word):
    """   (srt) -> bool
    Return True if and only if 'word' is a palindrome
    >>> is_palindrome.reverse('kayak')
    True
    """
    s = word
    word = s.strip()
    return word == word[::-1]

    # Option 1
    # for i in range(len(s) // 2 + 1):
    #   if s[i] != s[len(s) - i - 1]:
    #     return False
    #
    # return True

    # Option 2
    # for i in range(len(s) // 2):
    #     if s[i] != s[len(s) - i - 1]:
    #         return False
    #
    # return True

    # Option 3
    j = len(s) - 1
    # for i in range(len(s) // 2):
    #   if s[i] != s[j - i]:
    #     return False
    #
    # return True

    # Option 4 - This does not work
    # for i in range(len(s) // 2):
    #   if s[i] != s[len(s) - i]:
    #     return False
    #
    # return True


def front_back(word):
    """   (srt) -> bool
    Return True if and only if 'word' is a palindrome
    >>> is_palindrome.front_back('kayak')
    True
    """
    word = word.strip()
    l = len(word)
    return word[:l // 2:1] == word[:l // 2 - (l % 2 == 0):-1]


def compare_loop(word):
    """   (srt) -> bool
    Return True if and only if 'word' is a palindrome
    >>> is_palindrome.compare_loop('kayak')
    True
    """
    word = word.strip()
    l = len(word)
    for i in range(len(word)):
        l -= 1 if word[i] == word[len(word)-i-1] else 0
    return l == 0
