from word_frequency_calculator import WordFrequencyCalculator

def test_get_word_frequency():
    document = get_test_document()
    calculator = WordFrequencyCalculator(document, sep=' ')

    word_frequency = calculator.get_word_frequency('you')

    assert word_frequency == 3

def test_get_word_frequency_but_word_not_in_document():
    document = get_test_document()
    calculator = WordFrequencyCalculator(document, sep=' ')

    word_frequency = calculator.get_word_frequency('apple')

    assert word_frequency == 0

def test_get_most_frequently_word():
    document = get_test_document()
    calculator = WordFrequencyCalculator(document, sep=' ')

    max_frequency_word = calculator.get_most_frequently_word()

    assert max_frequency_word == 'you'


def get_test_document():
    return 'Do you want to buy a book I can sell it to you at a low price Because you are handsome'