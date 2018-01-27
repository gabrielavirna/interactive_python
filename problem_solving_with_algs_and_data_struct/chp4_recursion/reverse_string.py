"""
Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
"""


def reverse_string(old_string):
    # base case: an one-character string/ empty string
    if old_string == "":
        # if base case, stop recursing & return the string
        return ""
    else:
        # making the recursive call & reducing the problem size using the last-character.
        return old_string[len(old_string)-1] + reverse_string(old_string[:len(old_string)-1])


def main():
    print(reverse_string("holla"))
    print(reverse_string("h"))
    print(reverse_string(""))
    print(reverse_string("follow"))


if __name__ == "__main__":
    main()