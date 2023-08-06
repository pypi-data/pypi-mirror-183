import re

def stringContainsLetters(string: str):
    pattern = '[a-zA-Z]'
    answer = False

    if re.findall(pattern, string):
        answer = True

    return answer

def stringContainsNumbers(string: str):
    pattern = '[0-9]'
    answer = False

    if re.findall(pattern, string):
        answer = True

    return answer


def longestString(strings: list):
    previousString = ''
    longestString = ''
    for currentString in strings:
        if not previousString:
            longestString = currentString
            previousString = currentString
            continue

        if len(currentString) > len(longestString):
            longestString = currentString

        previousString = currentString

    return longestString





