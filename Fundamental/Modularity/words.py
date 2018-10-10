#!/ Pyhton3
"""Retrieve and print words from a URL

Usage:
    python words.py <URL>
"""
import sys
from urllib.request import urlopen

#https://google.github.io/styleguide/pyguide.html
def fetch_words(url):
    """Fetch a list of words from a URL
    
    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of string containing the word
        the document.
    """
    with urlopen(url) as story:
        strory_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                strory_words.append(word)
    return strory_words


def print_items(strory_items):
    """Print item one per line

    Args:
        An iterable series of printable items
    """
    for item in strory_items:
        print(item)


def main(url):   
    """Print each word from a text document from URL

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
   main(sys.argv[0]) #The command line argument

#Parser for command-line options, arguments and sub-commands
#https://docs.python.org/3/library/argparse.html
#http://docopt.org/
