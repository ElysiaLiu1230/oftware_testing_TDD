import bibtex
import pytest

@pytest.fixture
def setup_data():
    return {
        'simple_author_1': "Smith",
        'simple_author_2': "Jones",
        'author_1': "John Smith",
        'author_2': "Bob Jones",
        'author_3': "Justin Kenneth Pearson",
        'surname_first_1': "Pearson, Justin Kenneth",
        'surname_first_2': "Van Hentenryck, Pascal",
        'multiple_authors_1': "Pearson, Justin and Jones, Bob"
    }

def test_author_1(setup_data):
    # Test only surnames.
    (Surname, FirstNames) = bibtex.extract_author(setup_data['simple_author_1'])
    assert (Surname, FirstNames) == ('Smith', '')

    (Surname, FirstNames) = bibtex.extract_author(setup_data['simple_author_2'])
    assert (Surname, FirstNames) == ('Jones', '')
