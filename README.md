# Compression: Huffman encoding
## Intro
In this repo I explore a basic approach for compression: Huffman coding. And test it with a smaller version of [enwik9](http://mattmahoney.net/dc/enwik9.zip) from [Hutter Prize competition](http://prize.hutter1.net/). 

Disclaimer: This is not an attempt whatsoever to create a decent compressor, just exploration.

## Usage
For encoding and decoding enwik5:
```python
python main.py
```
Outputs:
```
Orig text: 
 <mediawiki xmlns="http://www.mediawiki.org/xml/export-0.3/" xmlns:xsi="http://www.w3.org/2001/XMLSch ... utism and as such resist it, dubbed ''anti-cure'', and the many people caught in the middle of the t
Decoded text 
 <mediawiki xmlns="http://www.mediawiki.org/xml/export-0.3/" xmlns:xsi="http://www.w3.org/2001/XMLSch  ...  utism and as such resist it, dubbed ''anti-cure'', and the many people caught in the middle of the t
Is text equal: True
Size of orig text:  100.148 KB
Size of encoded text:  61.032125 KB (488257 bits)
Approx size of hufman dict: 3.712 KB
Approx size of node dict: 8.775 KB
Compression ratio (no encoding dict):  1.640906325971773
Optimal entropy given the split 4.862219963642222
Encoding entropy 4.882569999999999
```
Run tests:
```
pytest test.py
```
## Huffman coding and tree
https://en.wikipedia.org/wiki/Huffman_coding


## Shannon entropy 

Shannon entropy is the theoretical minimum value that a encoding can achieve given certain tokenization. It is defined as
$$H(X) = -\sum_{i=1}^{n} P(x_i) \log{P(x_i)}$$
Entropy of the encoding
$$L(C)= l_i * P(x_i) = l_i*w_i$$
Being $l_i$ the length of the codeword ($l=3$ for $c_i=101$). And $w_i$ is the weight of the character or the probability. $L(C)>=H(X)$

https://en.wikipedia.org/wiki/Entropy_(information_theory)
## Plan
TODO:

- [X] Implement Huffman encoding
- [X] Implement Huffman decoding
- [X] Implement test (both texts equal and huffman and right huffman tree)
- [X] Check entropies are similar
- [ ] Optimize tokenization
- [ ] Use actual bits for encoded text (currently they are chars) 
- [ ] Check why decoding takes so much time?

