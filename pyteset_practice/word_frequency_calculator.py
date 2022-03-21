class WordFrequencyCalculator:
    def __init__(self, document, sep=' '):
        self.__word_frequency = {}
        for word in document.split(sep):
            if word in self.__word_frequency:
                self.__word_frequency[word] += 1
            else:
                self.__word_frequency[word] = 1

    def get_word_frequency(self, word):
        return self.__word_frequency.get(word, 0)

    def get_most_frequently_word(self):
        sorted_word_frequency = sorted(self.__word_frequency.items(), key=lambda x: -x[1])
        word, frequency = sorted_word_frequency[0]
        return word