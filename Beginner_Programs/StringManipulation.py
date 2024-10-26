def reverseString(word):
        if type(word) is not str:
            word=str(word)
        reversedWord=word[::-1]
        return f"The reversed version of \"{word}\" is \"{reversedWord}\""
# print(reverseString(25))

def isPalindromeString(word):
    if type(word) is not str:
        word=str(word)
    w="".join([letter for letter in word if letter.isalnum()]).lower()
    return w==w[::-1]
# print(isPalindromeString("A man, a plan, a canal: Panama"))
# print(isPalindromeString("race a care"))
# print(isPalindromeString(212))