from utils import get_frequency_dict, get_tree_hufman_and_encoded_bin, decode
import pytest

@pytest.fixture
def encoded_text_target():
    e = "1000011101001000110010011101100111001001000111110010011111011111100010001111110100111001001011111011101000111111001"
    return e

@pytest.fixture
def huffman_dict_target():
    h = {'_': '00', 'D': '01', 'A': '10', 'E': '110', 'C': '1110', 'B': '1111'}
    return h



def test_example(huffman_dict_target, encoded_text_target):
    text = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
    freq = get_frequency_dict(text)
    tree, huffman_dict, encoded_text = get_tree_hufman_and_encoded_bin(text, freq)
    # Decode is terribly slow
    decoded_text = decode(encoded_text,tree)
    assert decoded_text == text, "Original text and decoded are not equal"
    for k,v in huffman_dict.items():

        assert v == huffman_dict_target[k], f"The Huffman dict is constructed differently in {k}"
    assert encoded_text == encoded_text_target, "Encoding does not match"