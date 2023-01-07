"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine to find words in a file"""

    def __init__(self, filename):
        """Creates and defines a words attribute that recieves a list from listify function"""
        file = open(filename)
        self.words = self.listify(file)

    def random(self):
        """Finds a random word to print from a list"""
        return random.choice(self.words)

    def listify(self, file):
        """Creates and returns a list that removes invalid items from the file and appends valid items"""
        my_words = []
        for line in file:
            line = line.replace('\n', '')
            line = line.replace('\t', '')
            if line == '':
                continue
            else:
                my_words.append(line.strip())
        self.words = my_words

        return my_words


class SpecialWordFinder(WordFinder):
    """Machine to find valid words in a file"""

    def __init__(self, path):
        super().__init__(path)

    def listify(self, file):
        """Creates and returns a list that removes invalid items from the file and appends valid items"""
        valid_words = []
        for line in file:
            line = line.replace('\n', '')
            line = line.replace('\t', '')
            if "#" in line or line == '':
                continue
            else:
                valid_words.append(line.strip())
        self.words = valid_words
        return valid_words


wf = WordFinder("testwords.txt")
sf = SpecialWordFinder("testwords.txt")


print(wf.random())
print(sf.random())
print(wf.random())
print(wf.random())
