import re
from termcolor import colored

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

def detectMajorVersionUpdate(currentVersion: str, nextVersion: str):
    answer = ''
    try:
        currentVersionNumber = re.search('\\d+\\.\\d+\\.\\d+', currentVersion).group(0)
        currentMajorVersion = (re.search('\\d+', currentVersionNumber)).group(0)

        nextVersionNumber = (re.search('\\d+\\.\\d+\\.\\d+', nextVersion)).group(0)
        nextMajorVersion = (re.search('\\d+', nextVersionNumber)).group(0)

        if nextMajorVersion != currentMajorVersion:
            answer = '!!! MAJOR VERSION UPDATE DETECTED !!!'
    except AttributeError:
        pass

    return answer
