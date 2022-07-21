from utils import get_probabilities_from_freq, get_encoding_entropy ,information_content, shannon_entropy_vector, shannon_entropy, get_frequency_dict, get_tree_hufman_and_encoded_bin, build_tree, decode
import numpy as np
import json
import pickle
import os

def main():

    # enwik version of only 10e5 bits
    text = open("enwik5").read()
    # Create list of frequencies of chars (tokenization for now is done on char level)
    freq = get_frequency_dict(text)
    tree, huffman_dict, encoded_text = get_tree_hufman_and_encoded_bin(text, freq)
    # Decode is terribly slow
    with open("encoded_text.txt", "w") as f:
        f.write(encoded_text)
    #exit(1)
    decoded_text = decode(encoded_text,tree)

    # Summary
    size_orig_text_bits = len(text.encode("utf-8"))
    probs = get_probabilities_from_freq(freq)
    bits_et = len(encoded_text)
    json.dump(huffman_dict, open("h.json", "w"))
    pickle.dump(tree, open("t.pickle", "wb"))

    print("Orig text: \n", text[:100], "...", text[-100:])
    print("Decoded text \n",decoded_text[:100], " ... ", decoded_text[-100:])
    print("Is text equal:", text==decoded_text)
    print("Size of orig text: ", size_orig_text_bits/1000, "KB", )
    print(f"Size of encoded text:  {bits_et/8/1000} KB ({bits_et} bits)")
    print("Approx size of hufman dict:", os.path.getsize("h.json")/1000, "KB")
    print("Approx size of node dict:", os.path.getsize("t.pickle")/1000, "KB")
    print(f"Compression ratio (no encoding dict): ", size_orig_text_bits/bits_et*8)
    print("Optimal entropy given the split", shannon_entropy(probs))
    print("Encoding entropy", sum(get_encoding_entropy(huffman_dict, freq)))

if __name__ == "__main__":
    main()