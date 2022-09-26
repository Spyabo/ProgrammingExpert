def get_n_longest_unique_words(words, n):
    uniqueWords = set(words)
    
    #search the list for unique words
    notUnique = notUnique.union(uniqueWords)
    uniqueWords.remove(notUnique)


        
    #sort the unique words longest to shortest
    #return the n number of unique words

# This suite of tests is written to run against your code
# so that we can check its correctness.

import unittest

import program


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        words = ["Longer", "Whatever", "Longer",
                 "Ball", "Rock", "Rocky", "Rocky"]
        n = 3
        expected = ["Whatever", "Ball", "Rock"]
        self.assertCountEqual(
            program.get_n_longest_unique_words(words, n), expected)

    def test_case_2(self):
        words = ["Longer", "Whatever", "Longer",
                 "Ball", "Rock", "Rocky", "Rocky"]
        n = 1
        expected = [
            "Whatever",
        ]
        self.assertCountEqual(
            program.get_n_longest_unique_words(words, n), expected)

    def test_case_3(self):
        words = ["Longer", "Whatever", "Longer",
                 "Ball", "Rock", "Rocky", "Rocky"]
        n = 0
        expected = []
        self.assertCountEqual(
            program.get_n_longest_unique_words(words, n), expected)

    def test_case_4(self):
        words = [
            "Hello",
            "AlgoExpert",
            "Algo",
            "Testing",
            "Programming",
            "Programming",
            "Coding",
            "Python",
            "JavaScript",
            "Coding",
            "Ruby",
        ]
        n = 5
        expected = ["AlgoExpert", "JavaScript", "Testing", "Python", "Hello"]
        self.assertCountEqual(
            program.get_n_longest_unique_words(words, n), expected)

    def test_case_5(self):
        words = ["Hello", "Hello", "Hello", "Abcd", "bcd", "a", "ab"]
        n = 2
        expected = ["Abcd", "bcd"]
        self.assertCountEqual(
            program.get_n_longest_unique_words(words, n), expected)
