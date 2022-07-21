import numpy as np
import sys
from typing import List, Tuple
def shannon_entropy(probabilities):
    """
    $$H(X) = -\sum_{i=1}^{n} P(x_i) \log{P(x_i)$$
    https://en.wikipedia.org/wiki/Entropy_(information_theory)
    Shannon entropy is the optimal value, the resulting value of the encoding can be compute as
    .
    """
    entropy = - sum(probabilities*np.log2(probabilities))
    return entropy
def information_content(probabilities):
    h = np.log2(probabilities**-1)
    return h

def shannon_entropy_vector(probabilities):
    return probabilities*information_content(probabilities)

def get_frequency_dict(text: str, ordered=True)->dict:
    freq = {}
    for char in text:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    if ordered:
        # Ordered list of tuples
        freq = sorted(freq.items(), key=lambda item: item[1], reverse=False)
    return freq

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.char = left[0]+right[0]
        self.value= left[1]+right[1]
    def __repr__(self):
        return f"[({self.char},{self.value}), left={self.left}, right={self.right}]"
    def __getitem__(self, item):
        if item==0:
            return self.char
        if item==1:
            return self.value
def build_tree(queue:list)->Node:
    """Leaf nodes will be tuple type"""
    queue = queue.copy()

    while len(queue)>1:
        nl = queue[0]
        nr = queue[1]
        queue = queue[2:]
        node = Node(left=nl, right=nr)
        queue.append(node)
        # reorder with new node
        queue = sorted(queue, key=lambda item: item[1], reverse=False)
    return queue[0]

def f(node, bit_string=""):
    """Create inbetween hufman dict"""
    if isinstance(node, tuple):
        # Leaf node
        return {node[0]: bit_string}
    # it works because there is always a leaf node in the next level of a non-leaf node?
    d = dict()
    d.update(f(node.left, bit_string+"0"))
    d.update(f(node.right, bit_string+"1"))
    return d
def encode(txt, hufman_dict):
    out = [hufman_dict[char] for char in txt]
    return "".join(out)

def decode(encoded_text:str, tree):
    char = ""
    node = tree
    while True:
        if isinstance(node, tuple):
            # leaf node
            char+=node[0]
            node = tree
            if len(encoded_text)==0:
                
                break
            else:
                continue
        bit = encoded_text[0]
        encoded_text = encoded_text[1:]
        if bit=="0":
            node = node.left
        else:
            node = node.right
    return char
    
def get_tree_hufman_and_encoded_bin(text: str, freq: List[Tuple[str, int]]):
    tree = build_tree(freq.copy())
    hufman_dict = f(tree)
    encoded_text = encode(text, hufman_dict)
    
    return tree, hufman_dict, encoded_text

def get_probabilities_from_freq(freq):
    ocurrences = np.array([value for char,value in freq])
    probs = ocurrences/sum(ocurrences)
    return probs
def get_encoding_entropy(hufman_dict, freq):
    probs = get_probabilities_from_freq(freq)
    l_w = np.array([len(hufman_dict[char])*w for (char, value), w in zip(freq, probs)])
    return l_w


def save_binary(txt: str, bin_filename="byte.bin"):
    """"""
    # Add how many zeros we have to remove at the end of the second to last byte
    num = len(txt)%8
    bit_strings = [
    txt[i:i + 8] if i!=len(txt)-1 else "0"*(8-len(txt[i:]))+txt[i:i + 8]
    for i in range(0, len(txt), 8)]
    
    byte_list = [int(b, 2) for b in bit_strings]
    byte_list.append(num)
    with open(bin_filename, 'wb') as f:
        f.write(bytearray(byte_list))

def load_binary_as_string(bin_filename = "byte.bin"):
    """"""
    with open(bin_filename, 'rb') as f:
        byte_stream = f.read() 
    print(byte_stream)
    num = int(byte_stream[-1])
    if num==0:
        bin_text = "{:08b}".format(int(byte_stream[:-1].hex(),16))
    else:
        bin_text = "{:08b}".format(int(byte_stream[:-2].hex(),16))
        num = int(byte_stream[-1])
        last_byte = "{:08b}".format(int(byte_stream[:-1].hex(),16))
        bin_text.append(last_byte[num:])
    return bin_text

if __name__ == "__main__":
    test_text = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
    # to construct the right hufman tree, it seems we need to add the previous node to the queue
    freq = get_frequency_dict(test_text)
    probs = get_probabilities_from_freq(freq)
    t,h,e = get_tree_hufman_and_encoded_bin(test_text, freq)
    print(e)
    print(decode(e,t))
    print("Optimal entropy given the split", shannon_entropy(probs))
    print("Encoding entropy", sum(get_encoding_entropy(h, freq)))