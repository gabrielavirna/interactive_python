"""
Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise.
Remember that a string is a palindrome if it is spelled the same both forward and backward. E.g.: radar is a palindrome.

For bonus points palindromes can also be phrases, but you need to remove the spaces and punctuation before checking.
E.g.: madam i’m adam is a palindrome. Other fun palindromes include:

kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami; I’m a lasagna hog.
Able was I ere I saw Elba
Kanakanak – a town in Alaska
Wassamassaw – a town in South Dakota
"""

from string import punctuation


def palindrome_checker(string):
    # base case: if len(old_string) is 0 or 1, the string is palindrome by identity
    if len(string) < 2:
        return True
    # If there is more then one letter in the string compare the first and the last letter
    else:
        if string[0] != string[-1]:
            return False
        # If equal, make a recursive call to the function
        # problem is reduced by using the string without the first and the last letter.
        return palindrome_checker(string[1:-1])


def is_palindrome(phrase):

    p = punctuation
    phrase_letters = ''.join([c for c in phrase.lower() if c not in p]).replace(' ', '')
    if len(phrase_letters) < 2:
        return True
    if phrase_letters[0] != phrase_letters[len(phrase_letters)-1]:
        return False
    return is_palindrome(phrase_letters[1:-1])


def main():

    print(palindrome_checker("kayak"))
    print(palindrome_checker("aibohphobia"))
    print(palindrome_checker(""))
    print(palindrome_checker("p"))

    print(is_palindrome("Madam in Eden I'm Adam"))
    print(is_palindrome("Live not on evil"))


if __name__ == "__main__":
    main()